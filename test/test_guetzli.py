import pytest

from pyguetzli import guetzli


JPEG_PATH = "test/image.jpg"
JPEG_LENGTH = 152485
JPEG_WIDTH = 256
JPEG_HEIGHT = 256
JPEG_PIXEL_COUNT = JPEG_WIDTH * JPEG_HEIGHT


class TestGuetzliImage(object):

    def setup(self):
        self.img = guetzli.GuetzliImage(b"\x00\x01\x02\x03", guetzli.GuetzliImage.TYPE_UNKNOWN)

    def test_length(self):
        assert self.img.length == 4

    def test_type(self):
        assert self.img.type == guetzli.GuetzliImage.TYPE_UNKNOWN

    def test_to_bytes(self):
        assert self.img.to_bytes() == b"\x00\x01\x02\x03"


class TestGuetzliImageReadFile(object):

    def test_none_existing_file(self):
        with pytest.raises(IOError):
            image = guetzli.guetzli_image_read_file("this-file-do-not-exists")

    def test_jpeg_file(self):
        image = guetzli.guetzli_image_read_file(JPEG_PATH)
        assert type(image) is guetzli.GuetzliImage
        assert image.length == JPEG_LENGTH
        assert image.to_bytes().startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")


class TestGuetzliImageProcess(object):

    def test_jpeg_guetzli_image(self):
        image = guetzli.guetzli_image_read_file(JPEG_PATH)
        image_opti = guetzli.guetzli_image_process(image, 100)
        assert type(image) is guetzli.GuetzliImage
        assert image_opti.length < image.length
        assert image_opti.to_bytes().startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")


class TestGuetzliRgbArray(object):

    def setup(self):
        self.rgb = guetzli.GuetzliRgbArray(b"\x00\x01\x02\x0a\x0b\x0c", 1, 2)

    def test_uncoherent_values(self):
        with pytest.raises(ValueError):
            rgb_array = guetzli.GuetzliRgbArray("0123", 10, 10)

    def test_width(self):
        assert self.rgb.width == 1

    def test_height(self):
        assert self.rgb.height == 2

    def test_length(self):
        assert self.rgb.length == 6

    def test_to_bytes(self):
        assert self.rgb.to_bytes() == b"\x00\x01\x02\x0a\x0b\x0c"


class TestGuetzliRgbArrayProcess(object):

    def test_4px_iamge(self):
        image_pixels = bytes(bytearray([
            0xFF, 0x00, 0x00,   0x00, 0xFF, 0x00,
            0x00, 0x00, 0xFF,   0xFF, 0xFF, 0xFF,
            ]))
        rgb_array = guetzli.GuetzliRgbArray(image_pixels, 2, 2)
        image = guetzli.guetzli_rgb_array_process(rgb_array)
        assert type(image) is guetzli.GuetzliImage
        assert image.length > 0
        assert image.to_bytes().startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")
