import cv2

def preprocesar_imagen(ruta_imagen):
    # Cargar imagen
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        return None
    
    # Escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Suavizado
    suavizado = cv2.GaussianBlur(gris, (5, 5), 0)
    
    return suavizado

def detectar_rostros(ruta_imagen):
    # Cargar imagen y el clasificador pre-entrenado de OpenCV
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        return None, 0
    
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    clasificador_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    rostros = clasificador_rostros.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    return imagen, len(rostros)
