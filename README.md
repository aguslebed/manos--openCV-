# Reconocimiento de Alfabeto Dactilológico con MediaPipe

Este proyecto utiliza Python, OpenCV y MediaPipe para reconocer gestos del alfabeto dactilológico (lengua de señas) en tiempo real a través de la cámara web.

## 📋 Requisitos e Instalación

Para ejecutar este proyecto, necesitas tener Python instalado. Se recomienda crear un entorno virtual, pero puedes instalar las dependencias directamente.

Las librerías necesarias son:
*   **opencv-python**: Para la captura de video y procesamiento de imágenes.
*   **mediapipe**: Para la detección de los puntos de referencia de la mano (landmarks).
*   **numpy**: Para cálculos matemáticos y vectoriales.

Puedes instalarlas ejecutando el siguiente comando en tu terminal:

```bash
pip install opencv-python mediapipe numpy
```

## 🚀 Cómo iniciar el proyecto

Sigue estos pasos para ejecutar la aplicación:

1.  Abre una terminal o línea de comandos.
2.  Navega hasta la carpeta donde se encuentra el archivo `app.py`.
3.  Ejecuta el script con Python:

```bash
python app.py
```

4.  Se abrirá una ventana mostrando la cámara. Coloca tu mano frente a la cámara para empezar a detectar letras.
5.  Para salir, presiona la tecla **Esc**.

## ✋ Letras Disponibles

El sistema reconoce actualmente las siguientes letras y gestos, dependiendo de la orientación de la mano:

**Mano Recta (Vertical):**
*   **A**: Puño cerrado con el pulgar pegado al lado.
*   **D**: Dedo índice levantado, resto cerrados, pulgar tocando el dedo medio.
*   **E**: Todos los dedos flexionados (puntas tocando la palma/nudillos).
*   **I**: Solo el dedo meñique levantado.
*   **L**: Dedo índice y pulgar levantados en forma de 'L'.
*   **R**: Dedos índice y medio cruzados.

**Mano de Lado:**
*   **B**: Palma abierta con el pulgar doblado hacia la palma.
*   **CH**: Dedos índice y medio juntos y estirados, resto cerrados.
*   **G**: Dedo índice señalando, resto cerrados (mano de lado).

**Mano Invertida (Hacia abajo):**
*   **M**: Tres dedos centrales (índice, medio, anular) hacia abajo, simulando las patas de la 'M'.
