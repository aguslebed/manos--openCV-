# Reconocimiento de Alfabeto Dactilológico con MediaPipe

Este proyecto utiliza Python, OpenCV y MediaPipe para reconocer gestos del alfabeto dactilológico (lengua de señas) en tiempo real a través de la cámara web.

## 📋 Requisitos e Instalación

Para ejecutar este proyecto, necesitas tener Python instalado. Se recomienda crear un entorno virtual, pero puedes instalar las dependencias directamente.

Las librerías y versiones utilizadas en el desarrollo son:
*   **opencv-python** (v4.12.0): Para la captura de video y procesamiento de imágenes.
*   **mediapipe** (v0.10.31): Para la detección de los puntos de referencia de la mano (landmarks).
*   **numpy** (v2.2.6): Para cálculos matemáticos y vectoriales.

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

**Nota Importante:** Este sistema está diseñado para reconocer letras estáticas del alfabeto dactilológico. Esto significa que **no reconoce gestos con movimiento** (como la 'J' o la 'Z'), sino únicamente las letras que se representan mediante una **posición fija de la mano**.

El sistema reconoce actualmente las siguientes letras y configuraciones:

**Mano Recta (Vertical):**
*   **A**: Puño cerrado con el pulgar pegado al lado.
*   **D**: Índice levantado, resto cerrados, y pulgar tocando el dedo medio.
*   **E**: Todos los dedos flexionados (puntas tocando la palma/nudillos).
*   **I**: Solo el dedo meñique levantado.
*   **L**: Dedo índice y pulgar levantados en forma de 'L'.
*   **O**: Punta del pulgar tocando la punta del índice.
*   **P**: Índice, medio y anular levantados (juntos).
*   **R**: Dedos índice y medio cruzados.
*   **S**: Puño cerrado "apretado".
*   **T**: Dedo pulgar entre el índice y medio (o configuración similar).
*   **U**: Dedos índice y medio levantados y juntos.
*   **V**: Dedos índice y medio levantados y separados.
*   **W**: Índice, medio y anular levantados y separados.

**Mano de Lado:**
*   **B**: Palma abierta vertical o de lado con el pulgar doblado hacia la palma.
*   **CH**: Dedos índice y medio juntos y estirados, resto cerrados.
*   **G**: Dedo índice señalando, resto cerrados.

**Mano Invertida (Hacia abajo):**
*   **M**: Tres dedos centrales (índice, medio, anular) hacia abajo.
*   **N**: Dos dedos (índice y medio) hacia abajo.
*   *(Nota: Es mejor poner la palma mirando hacia la cámara para que el modelo detecte bien el pulgar)*
