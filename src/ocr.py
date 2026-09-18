import easyocr
import numpy as np
import cv2
reader = easyocr.Reader(['en'])
def extract_text(image_bytes: bytes) -> list[str]:
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    result = reader.readtext(image, detail = 0)
    return result