import pytest
from PIL import Image

from pyguetzli import guetzli


JPEG_PATH = "test/image.jpg"
JPEG_LENGTH = 152485
JPEG_WIDTH = 256
JPEG_HEIGHT = 256
JPEG_PIXEL_COUNT = JPEG_WIDTH * JPEG_HEIGHT


class TestGuetzliImage(object):

    def setup(self):
        self.img = guetzli.GuetzliImage(bytes("\x00\x01\x02\x03"), guetzli.GuetzliImage.TYPE_UNKNOWN)

    def test_length(self):
        assert self.img.length == 4

    def test_type(self):
        assert self.img.type == guetzli.GuetzliImage.TYPE_UNKNOWN

    def test_to_bytes(self):
        assert self.img.to_bytes() == "\x00\x01\x02\x03"


def test_read_file_that_not_exists():
    with pytest.raises(IOError):
        image = guetzli.read_file("this-file-do-not-exists")


def test_read_file_jpeg():
    image = guetzli.read_file(JPEG_PATH)
    assert type(image) is guetzli.GuetzliImage
    assert image.length == JPEG_LENGTH
    assert image.to_bytes().startswith("\xFF\xD8\xFF\xE0\x00\x10JFIF")


def test_image_optimize_jpeg():
    image = guetzli.read_file(JPEG_PATH)
    image_opti = guetzli.image_optimize(image, 100)
    assert type(image) is guetzli.GuetzliImage
    assert image_opti.length < image.length
    assert image_opti.to_bytes().startswith("\xFF\xD8\xFF\xE0\x00\x10JFIF")


class TestGuetzliRgbArray(object):

    def setup(self):
        self.rgb = guetzli.GuetzliRgbArray(bytes("\x00\x01\x02\x0a\x0b\x0c"), 1, 2)

    def test_width(self):
        assert self.rgb.width == 1

    def test_height(self):
        assert self.rgb.height == 2

    def test_length(self):
        assert self.rgb.length == 6

    def test_to_bytes(self):
        assert self.rgb.to_bytes() == "\x00\x01\x02\x0a\x0b\x0c"


def test_rgb_array_new_with_uncoherent_values():
    with pytest.raises(ValueError):
        rgb_array = guetzli.GuetzliRgbArray("0123", 10, 10)


def test_rgb_array_optimize():
    image_pixels = bytes(bytearray([
        0xFF, 0x00, 0x00,   0x00, 0xFF, 0x00,
        0x00, 0x00, 0xFF,   0xFF, 0xFF, 0xFF,
        ]))
    rgb_array = guetzli.GuetzliRgbArray(image_pixels, 2, 2)
    image = guetzli.rgbarray_optimize(rgb_array)
    assert type(image) is guetzli.GuetzliImage
    assert image.length > 0
    assert image.to_bytes().startswith("\xFF\xD8\xFF\xE0\x00\x10JFIF")
