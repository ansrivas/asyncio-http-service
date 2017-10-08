# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test modules."""

import os
from app.utils import read_config, read_config_from_env


def test_config_validation(config):
    """Read and validate config files."""
    assert read_config(config.good_filepath)
    assert read_config(config.bad_filepath) is None

    # when
    os.environ['config_path'] = config.good_filepath
    # then
    assert read_config_from_env('config_path')

    # when
    os.environ['config_path'] = config.bad_filepath
    # then
    assert read_config_from_env('config_path') is None
