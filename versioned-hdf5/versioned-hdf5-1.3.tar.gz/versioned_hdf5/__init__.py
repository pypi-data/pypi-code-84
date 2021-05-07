from .api import VersionedHDF5File
from .replay import delete_version, modify_metadata

__all__ = ['VersionedHDF5File', 'delete_version', 'modify_metadata']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
