import os
import process

from basics import setup_logger

logging = setup_logger(__file__)

class CaptureError(Exception):
    pass


class Capture:
    IMAGE_SIZE = "320x240"
    CAPTURE_SETTINGS = "-i 0 -F 5 --no-banner --greyscale --set brightness=0% --gmt --jpeg 90"

    def __init__(self):
        self.device = None

    def run(self):
        if not self.device:
            self.check_devices()

        if self.device:
            try:
                self.capture()
            except CaptureError:
                # Try again after checking the devices
                self.check_devices()
                self.capture()

    def check_devices(self):
        for device in os.popen("ls /dev/video*"):
            device = device.strip()
            cmd = ["v4l2-ctl", f"--device={device}", "--all"]
            result = process.execute(cmd)
            output = result.stdout.decode()
            if output.find("H264 USB Camera: USB Camera") != -1 and output.find("brightness") != -1:
                self.device = device
                logging.info(f"Using device {device}")
                break
        else:
            self.device = None
            logging.error("No camera found")

    def capture(self):
        cmd = ["fswebcam", "-d", self.device, "-r", self.IMAGE_SIZE] + self.CAPTURE_SETTINGS.split() + ["captured.jpg"]
        result = process.execute(cmd)
        output = result.stdout.decode()
        if output.find("Writing JPEG image to") == -1 or result.returncode != 0 or result.stderr:
            raise CaptureError(f"Image could not be saved. Return code: {result.returncode},\n  stdout:\n{output}\n"
                               f"  stderr:\n{result.stderr}")


def main():
    capture = Capture()
    capture.run()

if __name__ == '__main__':
    main()
