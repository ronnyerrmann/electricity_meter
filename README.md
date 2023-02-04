# electricity_meter
Log electricity consumption

Accessing the smart meter data seems difficult (which makes sense for security reasons), so this is what I plan to create:

1. Capture image from the HDI (using `fswebcam`)
2. Analyse the image to get the current consumption (see also [ocr])
3. Store the consumption in a database
4. Publish the image on a webserver (using [django])
5. Regularly combine the consumption (e.g. by minute (1440 entries per day), 5 min (9k entries per month), half-hourly (18k entries per year))

## Requirements:
```
sudo apt  install fswebcam v4l-utils
# tesseract
sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel
sudo apt update
sudo apt install tesseract-ocr
```

## Install
Python environment:
```commandline
mkvirtualenv -p python3 electricity_meter
workon electricity_meter
pip install pytesseract django
```

Additional tesseract training data
```
git clone git@github.com:adrianlazaro8/Tesseract_sevenSegmentsLetsGoDigital
cp -p Tesseract_sevenSegmentsLetsGoDigital/Trained\ data/lets.traineddata /usr/share/tesseract-ocr/5/tessdata/
```