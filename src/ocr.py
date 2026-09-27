import easyocr
import numpy as np
import cv2
reader = easyocr.Reader(['en'])

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    denoised = cv2.GaussianBlur(gray, (5, 5), 0)
    return denoised

def extract_text(image_bytes: bytes) -> list[str]:
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    preprocessed_image = preprocess_image(image)
    result = reader.readtext(preprocessed_image, detail = 0)
    return result