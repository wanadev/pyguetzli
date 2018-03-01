import pytest

from pyguetzli import guetzli


JPEG_MAGIC = b"\xFF\xD8\xFF\xE0\x00\x10JFIF"


@pytest.fixture
def jpeg_bytes():
    return open("./test/image.jpg", "rb").read()


@pytest.fixture
def misc_bytes():
    return b"\x01\x02\x03\x04"


@pytest.fixture
def rgb_bytes():
    return bytes(bytearray([
            0xFF, 0x00, 0x00,   0x00, 0xFF, 0x00,
            0x00, 0x00, 0xFF,   0xFF, 0xFF, 0xFF,
            ]))


class Test_process_jpeg_bytes(object):

    def test_jpeg_image(self, jpeg_bytes):
        optimized_jpeg_bytes = guetzli.process_jpeg_bytes(jpeg_bytes)
        assert isinstance(optimized_jpeg_bytes, bytes)
        assert optimized_jpeg_bytes.startswith(JPEG_MAGIC)
        assert len(optimized_jpeg_bytes) < len(jpeg_bytes)

    def test_quality_param(self, jpeg_bytes):
        optimized_jpeg_bytes_q100 = guetzli.process_jpeg_bytes(jpeg_bytes, 100)
        optimized_jpeg_bytes_q50 = guetzli.process_jpeg_bytes(jpeg_bytes, 50)
        assert len(optimized_jpeg_bytes_q50) < len(optimized_jpeg_bytes_q100)

    def test_non_jpeg_image(self, misc_bytes):
        with pytest.raises(ValueError):
            guetzli.process_jpeg_bytes(misc_bytes)

    def test_truncated_jpeg(self, jpeg_bytes):
        with pytest.raises(ValueError):
            guetzli.process_jpeg_bytes(jpeg_bytes[:64])


class Test_process_rgb_bytes(object):

    def test_rgb_data(self, rgb_bytes):
        optimized_jpeg_bytes = guetzli.process_rgb_bytes(rgb_bytes, 2, 2)
        assert isinstance(optimized_jpeg_bytes, bytes)
        assert optimized_jpeg_bytes.startswith(JPEG_MAGIC)

    @pytest.mark.skip(reason="we need a larger image to be able to test this")
    def test_quality_param(self, rgb_bytes):
        optimized_jpeg_bytes_q100 = guetzli.process_rgb_bytes(
                rgb_bytes, 2, 2, 100)
        optimized_jpeg_bytes_q50 = guetzli.process_rgb_bytes(
                rgb_bytes, 2, 2, 50)
        assert len(optimized_jpeg_bytes_q50) < len(optimized_jpeg_bytes_q100)

    def test_wrong_width_height(self, rgb_bytes):
        with pytest.raises(ValueError):
            guetzli.process_rgb_bytes(rgb_bytes, 4, 4)
