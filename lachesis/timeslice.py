r"""
Time-slices and functions to support them.
"""

from pprint import pformat
from datetime import datetime, timedelta
from lachesis.util import create_logger

class Timeslice:
    r"""
    A slice of time.
    """
    def __init__(self, start_time: datetime, previous: 'Timeslice'=None):
        logger = create_logger('Timeslice.__init__')
        logger.debug('starting')
        self.start_time = start_time
        self.previous = previous
        self._next = None
        logger.debug('ending')

    @property
    def next(self) -> 'Timeslice':
        r"""
        The next timeslice.
        """
        logger = create_logger('Timeslice.next')
        logger.debug('starting')
        if not self._next:
            logger.debug('self._next not set; creating new Timeslice')
            next_time = self.start_time + timedelta(minutes=15)
            self._next = Timeslice(start_time=next_time,
                                   previous=self)
        logger.debug('ending')
        return self._next

    @property
    def is_last(self) -> bool:
        r"""
        Is this the last timeslice in our list?
        """
        logger = create_logger('Timeslice.is_last')
        logger.debug('starting; returning whether self._next is None')
        return self._next is None

    def __str__(self) -> str:
        logger = create_logger('Timeslice.__str__')
        logger.debug('starting; returning string of timeslice start')
        return self.start_time.strftime('%c')

    def __repr__(self) -> str:
        logger = create_logger('Timeslice.__repr__')
        logger.debug('starting; returning str(self)')
        return str(self)
