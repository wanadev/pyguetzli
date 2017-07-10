import pytest
import pyguetzli


class Test_pyguetzli_api(object):

    def test_consts(self):
        assert hasattr(pyguetzli, "DEFAULT_JPEG_QUALITY")

    def test_process_jpeg_bytes(self):
        assert hasattr(pyguetzli, "process_jpeg_bytes")

    def test_process_rgb_bytes(self):
        assert hasattr(pyguetzli, "process_rgb_bytes")

