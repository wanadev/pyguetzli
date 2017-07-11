from . import guetzli


def _to_pil_rgb_image(image):
    """Returns an PIL Image converted to the RGB color space. If the image has
    an alpha channel (transparency), it will be overlaid on a black background.

    Arguments:
    image -- the PIL image
    """
    if image.mode == "RGB":
        return image

    from PIL import Image

    image.load()
    rgb_image = Image.new("RGB", image.size, (0x00, 0x00, 0x00))
    rgb_image.paste(image, mask=image.split()[3])  # bands: R=0, G=1, B=2, A=3

    return rgb_image


def process_pil_image(image, quality=guetzli.DEFAULT_JPEG_QUALITY):
    """Generates an optimized JPEG from a PIL image. If the image has an alpha
    channel (transparency), it will be overlaid on a black background.

    Please note that the [PIL] (pillow) extra dependency must be installed to
    allow this function to work.

    Arguments:
    image -- the PIL image

    Keyword Arguments:
    quality -- the output JPEG quality (default 95)
    """
    image_rgb = _to_pil_rgb_image(image)
    image_rgb_bytes = image_rgb.tobytes()
    return guetzli.process_rgb_bytes(
            image_rgb_bytes,
            *image.size,
            quality=quality
            )
