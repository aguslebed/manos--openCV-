import cv2
import mediapipe as mp
import numpy as np

hands_model = mp.solutions.hands
drawing_utils = mp.solutions.drawing_utils


def is_finger_down(landmarks, finger_tip, finger_pip):
    # Pre-calculamos la orientacion de la mano para no repetirlo por cada dedo
    is_straight = straight_hand(landmarks)
    is_side = side_hand(landmarks)
    is_upside = upside_down_hand(landmarks)
    is_right = fingers_pointing_to_the_right(landmarks)
    is_left = fingers_pointing_to_the_left(landmarks)

    for tip, pip in zip(finger_tip, finger_pip):
        
        # LOGICA UNIVERSAL PARA PULGAR (Basada en distancias, funciona en cualquier rotacion)
        if tip == hands_model.HandLandmark.THUMB_TIP:
            # Comparamos la distancia de la PUNTA al Nudillo Meñique (17) 
            # vs la distancia de la Articulacion (IP) al Nudillo Meñique (17).
            # Si la punta esta mas cerca del meñique que la articulacion, el dedo esta doblandose hacia adentro.
            
            p_tip = np.array([landmarks[tip].x, landmarks[tip].y])
            p_ip = np.array([landmarks[pip].x, landmarks[pip].y])
            p_pinky_mcp = np.array([landmarks[17].x, landmarks[17].y])
            
            dist_tip = np.linalg.norm(p_tip - p_pinky_mcp)
            dist_ip = np.linalg.norm(p_ip - p_pinky_mcp)
            
            if dist_tip < dist_ip:
                return True # Pulgar Cerrado
            continue # Si no esta cerrado, pasamos al siguiente dedo

        # LOGICA PARA LOS DEMAS DEDOS (Basada en orientacion)
        if is_straight:
            if landmarks[tip].y > landmarks[pip].y:
                return True
        elif is_side:
            if is_right and landmarks[tip].x < landmarks[pip].x:
                return True
            if is_left and landmarks[tip].x > landmarks[pip].x:
                return True
        elif is_upside:
            if landmarks[tip].y < landmarks[pip].y:
                return True
                
    return False

def get_finger_status(landmarks):
    finger = []
    
    # Tips y Pips definidos globalmente
    # Iteramos por cada dedo individualmente
    for tip, pip in zip(finger_tips, finger_pips):
        # is_finger_down espera listas, asi que le pasamos listas de 1 elemento
        if is_finger_down(landmarks, [tip], [pip]):
            finger.append(0) # Si esta 'down', el status es 0
        else:
            finger.append(1) # Si no esta 'down', el status es 1 (levantado)
    
    return finger

def distance_between_fingers(finger1,finger2,landmarks):
    return np.sqrt((landmarks[finger1].x - landmarks[finger2].x)**2 + (landmarks[finger1].y - landmarks[finger2].y)**2)

#Dedo 1 cruza al dedo 2
def is_finger_crossed(finger_tip_1,finger_tip_2,landmarks):
    return landmarks[finger_tip_1].x > landmarks[finger_tip_2].x

def thumb_in(landmarks):
    return landmarks[4].x < landmarks[3].x

def tips_over_thumb(landmarks):
    return landmarks[8].x < landmarks[4].x and landmarks[12].x < landmarks[4].x and landmarks[16].x < landmarks[4].x and landmarks[20].x < landmarks[4].x

def upside_down_hand(landmarks):
    # Dy > Dx (Vertical) y Muneca (0) ARRIBA de Nudillo Medio (9) (Menor Y)
    return abs(landmarks[0].y - landmarks[9].y) > abs(landmarks[0].x - landmarks[9].x) and landmarks[0].y < landmarks[9].y

def side_hand(landmarks):
    # Dx > Dy (Horizontal predomina)
    return abs(landmarks[0].x - landmarks[9].x) > abs(landmarks[0].y - landmarks[9].y)

def straight_hand(landmarks):
    # Dy > Dx (Vertical) y Muneca (0) ABAJO de Nudillo Medio (9) (Mayor Y)
    return abs(landmarks[0].y - landmarks[9].y) > abs(landmarks[0].x - landmarks[9].x) and landmarks[0].y > landmarks[9].y

def fingers_pointing_to_the_right(landmarks):
    # El Nudillo del indice (5) esta a la derecha de la Muñeca (0)
    return landmarks[5].x > landmarks[0].x

def fingers_pointing_to_the_left(landmarks):
    # El Nudillo del indice (5) esta a la izquierda de la Muñeca (0)
    return landmarks[5].x < landmarks[0].x

def identify_letter(finger_status):

    if finger_status == [0,0,0,0,0]:
        return 'A'
    
    if finger_status == [0,1,1,1,1]:
        return 'B'
    
    if finger_status == [1,0,0,0,0]:
        return 'E'
    
    if finger_status == [0,1,1,0,0]:
        if is_finger_crossed(hands_model.HandLandmark.INDEX_FINGER_TIP,hands_model.HandLandmark.MIDDLE_FINGER_TIP,results.multi_hand_landmarks[0].landmark):
            return 'R'
        elif distance_between_fingers(hands_model.HandLandmark.INDEX_FINGER_TIP,hands_model.HandLandmark.MIDDLE_FINGER_TIP,results.multi_hand_landmarks[0].landmark) < 0.1:
            return 'V'
        else:
            return 'U'
    return ''

cap = cv2.VideoCapture(0)
finger_tips = [hands_model.HandLandmark.THUMB_TIP,
               hands_model.HandLandmark.INDEX_FINGER_TIP,
               hands_model.HandLandmark.MIDDLE_FINGER_TIP,
               hands_model.HandLandmark.RING_FINGER_TIP,
               hands_model.HandLandmark.PINKY_TIP]

finger_pips = [hands_model.HandLandmark.THUMB_IP,
               hands_model.HandLandmark.INDEX_FINGER_PIP,
               hands_model.HandLandmark.MIDDLE_FINGER_PIP,
               hands_model.HandLandmark.RING_FINGER_PIP,
               hands_model.HandLandmark.PINKY_PIP]

status = [0,0,0,0,0]
with hands_model.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.8, max_num_hands=1) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        
        image = cv2.flip(image, 1)
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                drawing_utils.draw_landmarks(image, hand_landmarks, hands_model.HAND_CONNECTIONS)
                   
            status = get_finger_status(results.multi_hand_landmarks[0].landmark)
            print(status)
            letter = identify_letter(status)
            if letter:
                cv2.putText(image,letter, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
           
           

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()