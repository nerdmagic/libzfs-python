__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)

from .manager import default_manager as bindings

__all__ = [
    'bindings',
]
