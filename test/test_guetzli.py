import pytest

from pyguetzli import guetzli


class Test_process_jpeg_bytes(object):

    def setup(self):
        self.jpeg_bytes = open("./test/image.jpg", "rb").read()
        self.misc_bytes = b"\x01\x02\x03\x04"

    def test_jpeg_image(self):
        optimized_jpeg_bytes = guetzli.process_jpeg_bytes(self.jpeg_bytes)
        assert isinstance(optimized_jpeg_bytes, bytes)
        assert optimized_jpeg_bytes.startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")
        assert len(optimized_jpeg_bytes) < len(self.jpeg_bytes)

    def test_quality_param(self):
        optimized_jpeg_bytes_q100 = guetzli.process_jpeg_bytes(
                self.jpeg_bytes, 100)
        optimized_jpeg_bytes_q50 = guetzli.process_jpeg_bytes(
                self.jpeg_bytes, 50)
        assert len(optimized_jpeg_bytes_q50) < len(optimized_jpeg_bytes_q100)

    def test_non_jpeg_image(self):
        with pytest.raises(ValueError):
            guetzli.process_jpeg_bytes(self.misc_bytes)

    def test_truncated_jpeg(self):
        with pytest.raises(ValueError):
            guetzli.process_jpeg_bytes(self.jpeg_bytes[:64])


class Test_process_rgb_bytes(object):

    def setup(self):
        self.rgb_bytes = bytes(bytearray([
            0xFF, 0x00, 0x00,   0x00, 0xFF, 0x00,
            0x00, 0x00, 0xFF,   0xFF, 0xFF, 0xFF,
            ]))

    def test_rgb_data(self):
        optimized_jpeg_bytes = guetzli.process_rgb_bytes(self.rgb_bytes, 2, 2)
        assert isinstance(optimized_jpeg_bytes, bytes)
        assert optimized_jpeg_bytes.startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")

    @pytest.mark.skip(reason="we need a larger image to be able to test this")
    def test_quality_param(self):
        optimized_jpeg_bytes_q100 = guetzli.process_rgb_bytes(
                self.rgb_bytes, 2, 2, 100)
        optimized_jpeg_bytes_q50 = guetzli.process_rgb_bytes(
                self.rgb_bytes, 2, 2, 50)
        assert len(optimized_jpeg_bytes_q50) < len(optimized_jpeg_bytes_q100)

    def test_wrong_width_height(self):
        with pytest.raises(ValueError):
            guetzli.process_rgb_bytes(self.rgb_bytes, 4, 4)
