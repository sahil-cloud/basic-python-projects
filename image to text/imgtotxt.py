import pytesseract
import os
from PIL import Image

# path to tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
    img = Image.open("C:\\python\\Basic python projects\\text to speech\\test1.jpg")
    text = pytesseract.image_to_string(img)
    print(text)

convert()
