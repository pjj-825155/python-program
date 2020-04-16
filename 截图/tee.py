from PIL import Image
import pytesseract
# 如果没有配置环境变量要加上这句
# pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
text=pytesseract.image_to_string(Image.open('2.jpg'),lang='eng')
print(text)
