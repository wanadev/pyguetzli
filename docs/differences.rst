Differences With Original Guetzli
=================================

PyGuetzli is and will always be as close as possible to original Guetzli
library from Google, with the exception of two things (patched in the Guetzli
source code):

* We needed to add the ``-fPIC`` flag to the build of the static library to
  allow it to be linked with our code. See `commit 467cb04`_.

* By default Guetzli do not accepts to generates JPEGs with a quality under 84.
  As we needed to generate poor quality JPEGs, we removed this limitation. See
  `commit ebe4840`_.

* Guetzli: Fixed a crash caused by a bad access to a vector revealed when
  compiled with ``-D_GLIBCXX_ASSERTIONS``. See `commit 1c35835`_.

.. _commit 467cb04: https://github.com/wanadev/guetzli/commit/467cb0495caa33b09c79eb1579aeeced60464351
.. _commit ebe4840: https://github.com/wanadev/guetzli/commit/ebe48409fd698e8f4d6996bca2a4b2ce8fc91e6b
.. _commit 1c35835: https://github.com/wanadev/guetzli/commit/1c35835c5acc0274820704c329581f6d7f7a6ecb
