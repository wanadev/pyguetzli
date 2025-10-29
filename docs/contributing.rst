Contributing
============

Thank you for your interest in PyGuetzli. You will find here all useful
information to contribute.


Questions
---------

If you have any question about the Python binding itself, you can

* `chat with us <https://discord.gg/BmUkEdMuFp>`__ on Discord,
* or `open an issue <https://github.com/wanadev/pyguetzli/issues>`__ on Github.

If you have a question related to Guetzli, please look at the original Guetzli
repository:

* https://github.com/google/guetzli/


Bugs
----

If you found a bug in the Python binding itself, please `open an issue
<https://github.com/wanadev/pyguetzli/issues>`__ on Github with as much
information as possible:

* How you installed PyGuetzli (Git, PyPI, Static build,...),
* What is your operating system / Linux distribution (and its version),
* All the error messages outputted by pip or by PyGuetzli,
* ...

If you found a bug in Guetzli, please `open an issue
<https://github.com/google/guetzli/issues>`__ on its Github project.


Pull Requests
-------------

Please consider `filing a bug <https://github.com/wanadev/pyguetzli/issues>`__
before starting to work on a new feature. This will allow us to discuss the
best way to do it. This is, of course, not necessary if you just want to fix
some typo in the documentation or small errors in the code.

Please note that your code must pass tests and follow the coding style defined
by the `pep8 <https://pep8.org/>`__.


Installing Development Dependencies
-----------------------------------

You can install PyGuetzli with all its extra and development dependencies using
the following command::

    pip install .[PIL,dev]


Running the Tests
-----------------

You will first have to install `nox <https://nox.thea.codes/>`_::

    pip3 install nox

Then you can check for lint error::

    nox --session lint

or run the tests::

    nox --session test

To run the tests only for a specific Python version, you can use following
commands (the corresponding Python interpreter must be installed on your
machine)::

    nox --session test-3.10
    nox --session test-3.11
    nox --session test-3.12
    nox --session test-3.13
    nox --session test-3.14


Building the Documentation
--------------------------

You will first have to install `nox <https://nox.thea.codes/>`_::

    pip3 install nox

Then you can run the following command::

    nox --session gendoc
