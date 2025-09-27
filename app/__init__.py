from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("tracker-api")
except PackageNotFoundError:
    __version__ = "0.3.0"
