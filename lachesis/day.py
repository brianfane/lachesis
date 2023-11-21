r"""
day.py
"""

from collections.abc import Mapping
from datetime import date, datetime
from lachesis.util import create_logger
from .timeslice import Timeslice

class Day(Mapping):
    r"""
    A Day
    """
    def __init__(self, day: date):
        self.day = day
        self.__timeslices = {}

    def __getitem__(self, item_key: datetime) -> Timeslice:
        try:
            return self.__timeslices[item_key]
        except KeyError:
            if self.day.year == item_key.year and \
               self.day.month == item_key.month and \
               self.day.day == item_key.day and \
               item_key.minute % 15 == 0:
                self.__timeslices[item_key] = Timeslice(start_time=item_key)
                return self.__timeslices[item_key]
            raise

    def __iter__(self):
        ...

    def __len__(self):
        return len(self.__timeslices)

    def __str__(self):
        logger = create_logger('Day.__str__')
        logger.debug('starting')
        return self.day.strftime('%c')

    def __eq__(self, other: "Day") -> bool:
        logger = create_logger('Day.__eq__')
        logger.debug('starting')
        return self.day == other.day

    def __neq__(self, other: "Day") -> bool:
        logger = create_logger('Day.__neq__')
        logger.debug('starting')
        return self.day != other.day

    def __lt__(self, other: "Day") -> bool:
        logger = create_logger('Day.__lt__')
        logger.debug('starting')
        return self.day < other.day

    def __le__(self, other: "Day") -> bool:
        logger = create_logger('Day.__le__')
        logger.debug('starting')
        return self.day <= other.day

    def __gt__(self, other: "Day") -> bool:
        logger = create_logger('Day.__gt__')
        logger.debug('starting')
        return self.day > other.day

    def __ge__(self, other: "Day") -> bool:
        logger = create_logger('Day.__ge__')
        logger.debug('starting')
        return self.day >= other.day
