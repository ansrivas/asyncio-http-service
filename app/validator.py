# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize validation utils to read config files."""

import trafaret as tr

config_schema = tr.Dict({
    tr.Key('postgres'):
        tr.Dict({
            'database': tr.String(),
            'user': tr.String(),
            'password': tr.String(),
            'host': tr.String(),
            'port': tr.Int(),
            'poolsize_min': tr.Int(),
            'poolsize_max': tr.Int(),
        }),
})
