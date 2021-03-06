# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32


class TronLiteError(Exception):
    """A custom core TronLite exception"""

    def __init__(self, message=None):

        message = 'There has been an error' if not message else message

        super(TronLiteError, self).__init__(message)


class TronLiteNotImplemented(TronLiteError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(TronLiteNotImplemented, self).__init__(message)


class TronLiteWarning(Warning):
    """Base warning for TronLite."""


class TronLiteUserWarning(UserWarning, TronLiteWarning):
    """The primary warning class."""
    pass


class TronLiteDeprecationWarning(TronLiteUserWarning):
    """A warning for deprecated features."""
    pass
