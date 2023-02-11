import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

from PIL import Image

img = Image.open('captured.jpg')
img = Image.open('test_img2.jpg')

print(pytesseract.image_to_string(img, lang='eng', config='--psm 6'))

print(pytesseract.image_to_string(img, lang='eng', config='--psm 7'))

print(pytesseract.image_to_string(img, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789.kw'))

print(pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.kw'))

print(pytesseract.image_to_string(img, lang='osd', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789.kw'))

print(pytesseract.image_to_string(img, lang='lets', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789.kw'))


import cv2

# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

# Perform text extraction
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print(data)

cv2.imshow('thresh', thresh)
cv2.imshow('opening', opening)
cv2.imshow('invert', invert)
cv2.waitKey()