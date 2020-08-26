# tron_lite

[![Versions](https://img.shields.io/badge/python->3.7-blue)](https://docs.python.org/3/)
[![PyPI version](https://badge.fury.io/py/sdss-tron-lite.svg)](https://badge.fury.io/py/sdss-tron-lite)
[![Documentation Status](https://readthedocs.org/projects/sdss-tron-lite/badge/?version=latest)](https://sdss-tron-lite.readthedocs.io/en/latest/?badge=latest)
[![Travis (.org)](https://img.shields.io/travis/sdss/tron_lite)](https://travis-ci.org/sdss/tron_lite)
[![codecov](https://codecov.io/gh/sdss/tron_lite/branch/master/graph/badge.svg)](https://codecov.io/gh/sdss/tron_lite)

A minimal version of the tron message passing system.

## Rationale

`tron_lite` is a rewrite of the SDSS [tron](https://github.com/sdss/tron) product, written in Python 3 and following modern packaging conventions. A significant part of `tron`'s codebase is not used in SDSS and poorly understood. `tron_lite` aims to rebuild the package from the ground up, starting with basic functionality and logging, and adding features as needed, while making sure the code is properly documented.

## Installation

In general you should be able to install ``tron_lite`` by doing

```console
pip install sdss-tron-lite
```

To build from source, use

```console
git clone git@github.com:sdss/tron_lite
cd tron_lite
pip install .[docs]
```

## Development

`tron_lite` uses [poetry](http://poetry.eustace.io/) for dependency management and packaging. To work with an editable install it's recommended that you setup `poetry` and install `tron_lite` in a virtual environment by doing

```console
poetry install
```

Pip does not support editable installs with PEP-517 yet. That means that running `pip install -e .` will fail because `poetry` doesn't use a `setup.py` file. As a workaround, you can use the `create_setup.py` file to generate a temporary `setup.py` file. To install `tron_lite` in editable mode without `poetry`, do

```console
pip install --pre poetry
python create_setup.py
pip install -e .
```
