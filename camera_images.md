# Commands:
- `-D 2` delay 2 seconds
- `-F 31` median over 31 frames
- `-S 2` skip the first 2 frames
- `-r 1920x1080` image resolution (numbers are maximum for current camera)

At the moment the best solution seems:
```
fswebcam -d /dev/video2 --gmt -r 960x540 --jpeg 95 -F 5 -S 2 --no-banner test_img.jpg
```