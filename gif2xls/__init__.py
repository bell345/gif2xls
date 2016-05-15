#!/usr/bin/env python3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from .version import APP_NAME, APP_VERSION

def main(*args, **kwargs):
    from .__main__ import main
    main(*args, **kwargs)
