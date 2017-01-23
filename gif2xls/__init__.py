#!/usr/bin/env python3

from .version import APP_NAME, APP_VERSION

def main(*args, **kwargs):
    from .__main__ import main
    main(*args, **kwargs)
