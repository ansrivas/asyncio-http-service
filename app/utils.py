# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bunch of utility functions."""

import os
from app.validator import config_schema
from trafaret_config import ConfigError, read_and_validate


def read_config(filepath):
    """Read a config file from a given path.

    Args:
        filepath (str)   : filepath to read config path

    Return:
        config json
    """
    try:
        config = read_and_validate(filepath, config_schema)
        return config
    except ConfigError as e:
        e.output()
        return None


def read_config_from_env(key):
    """Read config from a file path in os.env.

    Args:
        key (str)   : Key represents an evironment variable to read config path

    Return:
        config json
    """
    filepath = os.getenv(key)
    return read_config(filepath)
