# encoding: utf-8

from sdsstools import get_config, get_logger, get_package_version


# pip package name
NAME = 'sdss-tron-lite'

# Loads config. config name is the package name.
config = get_config('tron_lite')

log = get_logger(NAME)

__version__ = get_package_version(path=__file__, package_name=NAME)
