import pytest
import pyguetzli


JPEG_PATH = "test/image.jpg"
JPEG_LENGTH = 152485


def test_optimize_from_file_that_not_exists():
    with pytest.raises(IOError):
        image = pyguetzli.optimize_from_file("this-file-do-not-exists")


def test_optimize_from_file_jpeg():
    image = pyguetzli.optimize_from_file(JPEG_PATH, 100)
    assert type(image) is pyguetzli.guetzli.GuetzliImage
    assert image.length < JPEG_LENGTH
    assert image.to_bytes().startswith("\xFF\xD8\xFF\xE0\x00\x10JFIF")

    image2 = pyguetzli.optimize_from_file(JPEG_PATH, 80)
    assert image2.length < image.length


def test_optimize_from_image_bytes_jpeg():
    data = open(JPEG_PATH, "rb").read()
    image = pyguetzli.optimize_from_image_bytes(data, 100)
    assert type(image) is pyguetzli.guetzli.GuetzliImage
    assert image.length < JPEG_LENGTH
    assert image.to_bytes().startswith("\xFF\xD8\xFF\xE0\x00\x10JFIF")

    image2 = pyguetzli.optimize_from_image_bytes(data, 80)
    assert image2.length < image.length

