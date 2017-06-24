#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = 'Lucas Fontaine <iamthe@frenchoverflow.com>'
__copyright__ = 'Copyright (C) 2017 Lucas Fontaine'
__description__ = """Framework for Python-based cryptocurrency trading"""
__license__ = 'GPLv3'
__version__ = '0.1.0'

import sys
import argparse


def parse_arguments(cmdline=""):
    """Parse the arguments"""

    parser = argparse.ArgumentParser(
        description=__description__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__)
    )

    a = parser.parse_args(cmdline)
    return a


def main():
    # Parse arguments
    args = parse_arguments(sys.argv[1:])  # pragma: no cover


if __name__ == '__main__':
    main()  # pragma: no cover
