import unittest
from unittest.mock import call, MagicMock, patch, PropertyMock

from capture import Capture, CaptureError


class CaptureTest(unittest.TestCase):

    def setUp(self) -> None:
        self._capture = Capture()


class TestCapture_run(CaptureTest):
    def test_no_device(self):
        self._capture.check_devices = MagicMock()

        self._capture.run()

        self._capture.check_devices.assert_called_once_with()

    def test_ok(self):
        self._capture.device = "/dev/foo"
        self._capture.capture = MagicMock()

        self._capture.run()

        self._capture.capture.assert_called_once_with()

    def test_fail_once(self):
        self._capture.device = "/dev/foo"
        self._capture.capture = MagicMock(side_effect=[CaptureError(), None])

        self._capture.run()

        self.assertEqual([call(), call()], self._capture.capture.call_args_list)

    def test_keep_failing(self):
        self._capture.device = "/dev/foo"
        self._capture.capture = MagicMock(side_effect=CaptureError())

        with self.assertRaises(CaptureError):
            self._capture.run()

        self.assertEqual([call(), call()], self._capture.capture.call_args_list)

@patch("capture.process")
@patch("capture.os")
class TestCapture_check_devices(CaptureTest):
    def test_ok(self, os, process):
        result = MagicMock()
        stdout = PropertyMock(side_effect=[b"Text", b"Text\nH264 USB Camera: USB Camera\nbrightness\n"])
        type(result).stdout = stdout
        process.execute.return_value = result
        os.popen.return_value = ["/dev/videoFoo", "/dev/videoBar"]

        self._capture.check_devices()

        self.assertEqual([call(['v4l2-ctl', '--device=/dev/videoFoo', '--all']),
                          call(['v4l2-ctl', '--device=/dev/videoBar', '--all'])], process.execute.call_args_list)
        self.assertEqual("/dev/videoBar", self._capture.device)

    def test_no_device(self, os, process):
        result = MagicMock()
        result.stdout = b"Text"
        process.execute.return_value = result
        os.popen.return_value = ["/dev/videoFoo"]
        self._capture.device = "bar"

        self._capture.check_devices()

        process.execute.assert_called_once_with(['v4l2-ctl', '--device=/dev/videoFoo', '--all'])
        self.assertIsNone(self._capture.device)


@patch("capture.process")
class TestCapture_capture(CaptureTest):
    def test_ok(self, process):
        result = MagicMock()
        result.stdout = b"bla\nWriting JPEG image to bla"
        result.returncode = 0
        result.stderr = None
        process.execute.return_value = result
        self._capture.device = "/dev/foo"

        self._capture.capture()

        process.execute.assert_called_once_with(
            ["fswebcam", "-d", "/dev/foo", "-r", self._capture.IMAGE_SIZE] + self._capture.CAPTURE_SETTINGS.split() +
            ["captured.jpg"]
        )

    def test_not_right_text(self, process):
        result = MagicMock()
        result.stdout = b"foo bar"
        result.returncode = 1
        result.stderr = None
        process.execute.return_value = result
        self._capture.device = "/dev/foo"

        with self.assertRaises(CaptureError):
            self._capture.capture()

    def test_return_code(self, process):
        result = MagicMock()
        result.stdout = b"bla\nWriting JPEG image to bla"
        result.returncode = 1
        result.stderr = None
        process.execute.return_value = result
        self._capture.device = "/dev/foo"

        with self.assertRaises(CaptureError):
            self._capture.capture()

    def test_error(self, process):
        result = MagicMock()
        result.stdout = b"bla\nWriting JPEG image to bla"
        result.returncode = 0
        result.stderr = "error"
        process.execute.return_value = result
        self._capture.device = "/dev/foo"

        with self.assertRaises(CaptureError):
            self._capture.capture()
