import pytesseract
import cv2

# links uteis:
# corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# pegar linguas: print(pytesseract.get_languages())

# CMD que vai ler a imagem e o nome da imagem
imagem = cv2.imread("print_magalu.JPG")

path = r"C:\Users\Lucas Oliveira\AppData\Local\Programs\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = path + r'\tesseract.exe'
# Este CMD falar para tesseract converter a imagem em texto
texto = pytesseract.image_to_string(imagem, lang="por")
print(texto)
