# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bunch of fixtures to be used across the tests."""

import os
import pytest
import pathlib
from collections import namedtuple
file_parent = pathlib.Path(__file__).parent


@pytest.fixture(scope="function")
def config(request):
    """."""
    good_yaml = "data/config.yaml"
    bad_yaml = "data/wrong_config.yaml"
    good_filepath = os.path.join(file_parent, good_yaml)
    bad_filepath = os.path.join(file_parent, bad_yaml)

    Config = namedtuple("Config", "good_filepath bad_filepath")

    def tear_down():
        pass

    request.addfinalizer(tear_down)
    return Config(good_filepath, bad_filepath)
