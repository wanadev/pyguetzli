import platform

from ._guetzli import lib, ffi


DEFAULT_JPEG_QUALITY = 95


def _str_to_bytes(str):
    if platform.python_version_tuple()[0] == "3":
        return bytes(str, "utf-8")
    return str


class GuetzliImage(object):

    TYPE_JPEG = lib.GUETZLI_IMAGE_TYPE_JPEG
    TYPE_PNG = lib.GUETZLI_IMAGE_TYPE_PNG
    TYPE_UNKNOWN = lib.GUETZLI_IMAGE_TYPE_UNKNOWN

    _cdata = None

    def __init__(self, data, type_):
        guetzli_image_p = lib.guetzliImageNew(type_, len(data))
        ffi.memmove(guetzli_image_p.data, data, len(data))
        guetzli_image_p_gc = ffi.gc(guetzli_image_p, lib.guetzliImageFree)
        self._cdata = guetzli_image_p_gc

    @classmethod
    def from_guetzli_image_p(cls, guetzli_image_p):
        if ffi.typeof(guetzli_image_p).cname != "GuetzliImage *":
            raise ValueError("Expected guetzli_image_p to be a 'GuetzliImage *'")
        image = cls.__new__(cls)
        image._cdata = guetzli_image_p
        return image

    @property
    def length(self):
        return self._cdata.length

    @property
    def type(self):
        return self._cdata.type

    def to_bytes(self):
        return ffi.unpack(self._cdata.data, self._cdata.length)

    def save(self, path):
        lib.guetzliImageWriteFile(_str_to_bytes(path), self._cdata)


class GuetzliRgbArray(object):

    _cdata = None

    def __init__(self, data, width, height):
        data_length = width * height * 3
        if len(data) != data_length:
            raise ValueError("%ix%ipx image, but %i Bytes given. Does the given array contains only rgb data?")
        guetzli_rgb_array_p = lib.guetzliRgbArrayNew(width, height)
        ffi.memmove(guetzli_rgb_array_p.data, data, data_length)
        guetzli_rgb_array_p_gc = ffi.gc(guetzli_rgb_array_p, lib.guetzliRgbArrayFree)
        self._cdata = guetzli_rgb_array_p_gc

    @property
    def width(self):
        return self._cdata.width

    @property
    def height(self):
        return self._cdata.height

    @property
    def length(self):
        return self.width * self.height * 3

    def to_bytes(self):
        return ffi.unpack(self._cdata.data, self.length)


def guetzli_image_read_file(path):
    guetzli_image_p = lib.guetzliImageReadFile(_str_to_bytes(path))

    if guetzli_image_p == ffi.NULL:
        raise IOError("Could not open the file")

    guetzli_image_p_gc = ffi.gc(guetzli_image_p, lib.guetzliImageFree)

    return GuetzliImage.from_guetzli_image_p(guetzli_image_p_gc)


def guetzli_image_process(image, quality=DEFAULT_JPEG_QUALITY):
    opti_guetzli_image_p = lib.guetzliImageProcess(image._cdata, quality)
    opti_guetzli_image_p_gc = ffi.gc(opti_guetzli_image_p, lib.guetzliImageFree)
    return GuetzliImage.from_guetzli_image_p(opti_guetzli_image_p_gc)


def guetzli_rgb_array_process(rgb_array, quality=DEFAULT_JPEG_QUALITY):
    opti_guetzli_image_p = lib.guetzliRgbArrayProcess(rgb_array._cdata, quality)
    opti_guetzli_image_p_gc = ffi.gc(opti_guetzli_image_p, lib.guetzliImageFree)
    return GuetzliImage.from_guetzli_image_p(opti_guetzli_image_p_gc)

