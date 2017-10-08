# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize module utils."""


import pytz
import logging
from datetime import datetime


logger = logging.getLogger(__name__)


def tzware_datetime():
    """
    Return a timezone aware datetime.

    :return: Datetime
    """
    return datetime.now(pytz.utc)
