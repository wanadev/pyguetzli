from PIL import Image

from pyguetzli import pil_image


class Test_process_pil_image(object):

    def setup(self):
        self.pil_image = Image.open("./test/image.jpg")

    def test_pil_image(self):
        optimized_jpeg_bytes = pil_image.process_pil_image(self.pil_image)
        assert isinstance(optimized_jpeg_bytes, bytes)
        assert optimized_jpeg_bytes.startswith(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")

    def test_quality_param(self):
        optimized_jpeg_bytes_q100 = pil_image.process_pil_image(
                self.pil_image, 100)
        optimized_jpeg_bytes_q50 = pil_image.process_pil_image(
                self.pil_image, 50)
        assert len(optimized_jpeg_bytes_q50) < len(optimized_jpeg_bytes_q100)
