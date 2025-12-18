import cv2
import mediapipe as mp
import numpy as np

hands_model = mp.solutions.hands
drawing_utils = mp.solutions.drawing_utils


def is_finger_down(landmarks, finger_tip, finger_mcp):
    return landmarks[finger_tip].y > landmarks[finger_mcp].y

cap = cv2.VideoCapture(0)

with hands_model.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        
        # Logica para procesar la imagen iria aqui
        image = cv2.flip(image, 1)
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                drawing_utils.draw_landmarks(image, hand_landmarks, hands_model.HAND_CONNECTIONS)
            
            finger_down = str(is_finger_down(results.multi_hand_landmarks[0].landmark, hands_model.HandLandmark.INDEX_FINGER_TIP, hands_model.HandLandmark.INDEX_FINGER_MCP))
            if finger_down:
                cv2.putText(
                    image,
                    str(finger_down),
                    (50, 100),                  # posición (x, y)
                    cv2.FONT_HERSHEY_SIMPLEX,   # fuente
                    1,                          # escala
                    (0, 255, 0),                # color (BGR)
                    2,                          # grosor
                    cv2.LINE_AA                 # suavizado
                )     
                


        
           
                

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()