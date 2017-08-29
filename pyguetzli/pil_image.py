"""
This modules contain helper function to deal with PIL / Pillow Images.

.. note::
    Please note that the ``[PIL]`` (pillow) extra dependency must be installed
    to allow functions from this module to work.
"""


from . import guetzli


def _to_pil_rgb_image(image):
    """Returns an PIL Image converted to the RGB color space. If the image has
    an alpha channel (transparency), it will be overlaid on a black background.

    :param image: the PIL image to convert

    :returns: The input image if it was already in RGB mode, or a new RGB image
              if converted.

    :raises ImportError: PIL / Pillow cannot be imported.
    """
    if image.mode == "RGB":
        return image

    from PIL import Image

    image.load()
    rgb_image = Image.new("RGB", image.size, (0x00, 0x00, 0x00))
    mask = None

    if image.mode == "RGBA":
        mask = image.split()[3]  # bands: R=0, G=1, B=2, 1=3

    rgb_image.paste(image, mask=mask)

    return rgb_image


def process_pil_image(image, quality=guetzli.DEFAULT_JPEG_QUALITY):
    """Generates an optimized JPEG from a PIL image. If the image has an alpha
    channel (transparency), it will be overlaid on a black background.

    :param image: the PIL image
    :param quality: the output JPEG quality (default 95)

    :returns: Optimized JPEG bytes
    :rtype: bytes

    :raises ImportError: PIL / Pillow cannot be imported.

    .. code:: python

        import pyguetzli
        from PIL import Image

        image = Image.open("./test/image.jpg")
        optimized_jpeg = pyguetzli.process_pil_image(image)
    """
    image_rgb = _to_pil_rgb_image(image)
    image_rgb_bytes = image_rgb.tobytes()
    return guetzli.process_rgb_bytes(
            image_rgb_bytes,
            *image.size,
            quality=quality
            )
