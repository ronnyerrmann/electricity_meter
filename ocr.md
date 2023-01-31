# Using tesseract

## Install a seven Segment trained data set for LetsGoDigital
e.g. [https://github.com/adrianlazaro8/Tesseract_sevenSegmentsLetsGoDigital]
```
git clone git@github.com:adrianlazaro8/Tesseract_sevenSegmentsLetsGoDigital
cp -p Tesseract_sevenSegmentsLetsGoDigital/Trained\ data/lets.traineddata /usr/share/tesseract-ocr/5/tessdata/
```
Usage:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
from PIL import Image
img = Image.open('test_img_sub.jpg')
print(pytesseract.image_to_string(img, lang='lets', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789.kw'))
```