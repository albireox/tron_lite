# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class Tron_liteError(Exception):
    """A custom core Tron_lite exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(Tron_liteError, self).__init__(message)


class Tron_liteNotImplemented(Tron_liteError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(Tron_liteNotImplemented, self).__init__(message)


class Tron_liteAPIError(Tron_liteError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Tron_lite API'
        else:
            message = 'Http response error from Tron_lite API. {0}'.format(message)

        super(Tron_liteAPIError, self).__init__(message)


class Tron_liteApiAuthError(Tron_liteAPIError):
    """A custom exception for API authentication errors"""
    pass


class Tron_liteMissingDependency(Tron_liteError):
    """A custom exception for missing dependencies."""
    pass


class Tron_liteWarning(Warning):
    """Base warning for Tron_lite."""


class Tron_liteUserWarning(UserWarning, Tron_liteWarning):
    """The primary warning class."""
    pass


class Tron_liteSkippedTestWarning(Tron_liteUserWarning):
    """A warning for when a test is skipped."""
    pass


class Tron_liteDeprecationWarning(Tron_liteUserWarning):
    """A warning for deprecated features."""
    pass
