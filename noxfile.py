import nox


@nox.session(reuse_venv=True)
def lint(session):
    session.install("flake8")
    session.run("flake8", "pyguetzli", "test", "noxfile.py")


@nox.session(python=["3.9", "3.10", "3.11", "3.12", "3.13"], reuse_venv=True)
def test(session):
    session.install("pytest")
    session.install(".[PIL]")
    session.run("pytest", "-v", "test")


@nox.session(reuse_venv=True)
def gendoc(session):
    session.install("sphinx", "sphinx-rtd-theme")
    session.install(".")
    session.run("sphinx-build", "-M", "html", "docs", "build")
