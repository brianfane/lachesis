r"""
Time tracking.
"""

import sys
from lachesis.util import load_data, create_logger

def main():
    r"""
    Main program.
    """
    logger = create_logger('main')
    logger.debug('starting')
    logger.debug('attempting to load data')
    _ = load_data()
    logger.debug('ending')

if __name__ == '__main__':
    sys.exit(main())
