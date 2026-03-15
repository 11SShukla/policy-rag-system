import pytesseract
import cv2
import numpy as np
from PIL import Image


def preprocess_image_for_ocr(image):

    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # noise removal
    gray = cv2.medianBlur(gray, 3)

    # thresholding
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh


def run_ocr(image):

    processed = preprocess_image_for_ocr(image)

    text = pytesseract.image_to_string(processed)

    return text
import pytesseract

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)