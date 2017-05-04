import pytest
from pyguetzli import guetzli


JPEG_PATH = "test/image.jpg"
JPEG_LENGTH = 152485


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
    assert image.length == JPEG_LENGTH
    assert image.to_bytes().startswith("\xFF\xD8\xFF\xE0\x00\x10JFIF")


def test_image_optimize_jpeg():
    image = guetzli.read_file(JPEG_PATH)
    image_opti = guetzli.image_optimize(image, 100)
    assert image_opti.length < image.length
    assert image_opti.to_bytes().startswith("\xFF\xD8\xFF\xE0\x00\x10JFIF")

