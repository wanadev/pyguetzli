import pytest
from PIL import Image

from pyguetzli import pil_image


JPEG_MAGIC = b"\xFF\xD8\xFF\xE0\x00\x10JFIF"


class Test_process_pil_image(object):

    @pytest.mark.parametrize("image_path", [
            "./test/image.jpg",
            "./test/rgb.png",
            "./test/rgba.png",
            "./test/grayscale.png",
            "./test/indexed.png",
        ])
    def test_pil_image(self, image_path):
        image = Image.open(image_path)
        optimized_jpeg_bytes = pil_image.process_pil_image(image)
        assert isinstance(optimized_jpeg_bytes, bytes)
        assert optimized_jpeg_bytes.startswith(JPEG_MAGIC)

    def test_quality_param(self):
        image = Image.open("./test/image.jpg")

        optimized_jpeg_bytes_q100 = pil_image.process_pil_image(
                image, 100)
        optimized_jpeg_bytes_q50 = pil_image.process_pil_image(
                image, 50)
        assert len(optimized_jpeg_bytes_q50) < len(optimized_jpeg_bytes_q100)
