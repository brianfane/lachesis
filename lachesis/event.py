r"""
An event.
"""

from datetime import datetime, timedelta
from lachesis.util import create_logger

class Event:
    r"""
    An event.
    """
    def __init__(self,
                 name: str,
                 start: datetime,
                 length: timedelta):
        r"""
        Initialize the event.
        """
        logger = create_logger('Event.__init__')
        logger.debug('starting')
        self.name = name
        self.start = start
        self.length = length
        logger.debug('ending')
