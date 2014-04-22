from ._version import __version__, __version_info__

VERSION = __version__

try:
    from ._zfsversion import libzfs_version
except ImportError:
    from libzfs.utils.version import detect_libzfs_version
    # We default back to the latest libzfs version
    libzfs_version = detect_libzfs_version()


from .bindings import enums
__all__ = [
    'enums',

    'VERSION',
    '__version__',
    '__version_info__',
    'libzfs_version',
]
