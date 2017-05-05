import pytest
import pyguetzli


JPEG_PATH = "test/image.jpg"
JPEG_LENGTH = 152485


class TestProcessImageFromFile(object):

    def test_none_existing_file(self):
        with pytest.raises(IOError):
            image = pyguetzli.process_image_from_file("this-file-do-not-exists")

    def test_jpeg_file(self):
        image = pyguetzli.process_image_from_file(JPEG_PATH, 100)
        assert type(image) is pyguetzli.guetzli.GuetzliImage
        assert image.length < JPEG_LENGTH
        assert image.to_bytes().startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")

        image2 = pyguetzli.process_image_from_file(JPEG_PATH, 80)
        assert image2.length < image.length


class TestProcessImageFromBytes(object):

    def test_jpeg_bytes(self):
        data = open(JPEG_PATH, "rb").read()
        image = pyguetzli.process_image_from_bytes(data, 100)
        assert type(image) is pyguetzli.guetzli.GuetzliImage
        assert image.length < JPEG_LENGTH
        assert image.to_bytes().startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")

        image2 = pyguetzli.process_image_from_bytes(data, 80)
        assert image2.length < image.length


class TestProcessRgbBytes(object):

    def test_4px_image(self):
        data = image_pixels = bytes(bytearray([
            0xFF, 0x00, 0x00,   0x00, 0xFF, 0x00,
            0x00, 0x00, 0xFF,   0xFF, 0xFF, 0xFF,
            ]))
        image = pyguetzli.process_rgb_bytes(data, 2, 2, 100)
        assert type(image) is pyguetzli.guetzli.GuetzliImage
        assert image.length > 0
        assert image.to_bytes().startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")

