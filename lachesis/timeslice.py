r"""
timeslice.py
"""

from datetime import datetime
from lachesis.util import create_logger

class Timeslice:
    r"""
    A 15-minute slice of time.
    """
    def __init__(self, start_time: datetime):
        logger = create_logger('Timeslice.__init__')
        logger.debug('starting')
        self.start_time = start_time
        self.time_category = None
        logger.debug('ending')

    def __str__(self):
        logger = create_logger('Timeslice.__str__')
        logger.debug('starting')
        return self.start_time.strftime('%c')

    def __eq__(self, other: "Timeslice") -> bool:
        logger = create_logger('Timeslice.__eq__')
        logger.debug('starting')
        return self.start_time == other.start_time

    def __neq__(self, other: "Timeslice") -> bool:
        logger = create_logger('Timeslice.__neq__')
        logger.debug('starting')
        return self.start_time != other.start_time

    def __lt__(self, other: "Timeslice") -> bool:
        logger = create_logger('Timeslice.__lt__')
        logger.debug('starting')
        return self.start_time < other.start_time

    def __le__(self, other: "Timeslice") -> bool:
        logger = create_logger('Timeslice.__le__')
        logger.debug('starting')
        return self.start_time <= other.start_time

    def __gt__(self, other: "Timeslice") -> bool:
        logger = create_logger('Timeslice.__gt__')
        logger.debug('starting')
        return self.start_time > other.start_time

    def __ge__(self, other: "Timeslice") -> bool:
        logger = create_logger('Timeslice.__ge__')
        logger.debug('starting')
        return self.start_time >= other.start_time
