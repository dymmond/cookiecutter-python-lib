from distutils.version import LooseVersion

__version__ = "{{ cookiecutter.version }}"
__version_info__ = tuple(LooseVersion(__version__).version)
