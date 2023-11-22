r"""
day.py
"""

from collections.abc import Mapping
from datetime import date, datetime, timedelta
from lachesis.util import create_logger
from .timeslice import Timeslice

class Day(Mapping):
    r"""
    A Day
    """
    def __init__(self, start_date: date):
        logger = create_logger('Day.__init__')
        logger.debug('starting')
        self.start_date = start_date
        self.__timeslices = {}
        logger.debug('ending')

    def __getitem__(self, item_key: datetime) -> Timeslice:
        logger = create_logger('Day.__getitem__')
        logger.debug('starting')
        try:
            logger.debug('attempt to return specific Timeslice')
            return self.__timeslices[item_key]
        except KeyError:
            logger.debug('Timeslice did not exist; creating new one')
            if self.start_date.year == item_key.year and \
               self.start_date.month == item_key.month and \
               self.start_date.day == item_key.day and \
               item_key.minute % 15 == 0:
                self.__timeslices[item_key] = Timeslice(start_time=item_key)
                return self.__timeslices[item_key]
            logger.debug('Timeslice would not be in this Day; error')
            raise

    def __iter__(self):
        logger = create_logger('Day.__iter__')
        logger.debug('starting')
        #
        # Define where this day starts, ...
        first_slice_dt = datetime(year=self.start_date.year,
                                  month=self.start_date.month,
                                  day=self.start_date.day,
                                  hour=0,
                                  minute=0,
                                  second=0)
        # ... where it stops, ...
        last_slice_dt = first_slice_dt + timedelta(days=1)
        # ... and how long each slice is.
        slice_interval = timedelta(minutes=15)
        #
        # Now we'll loop through each slice, using the
        # __getitem__() method to get (or create) specific
        # slices.
        curr_dt = first_slice_dt
        logger.debug('starting while-loop')
        while curr_dt != last_slice_dt:
            logger.debug('yielding Timeslice')
            yield self[curr_dt]
            curr_dt += slice_interval
        logger.debug('ending')

    def __len__(self):
        logger = create_logger('Day.__len__')
        logger.debug('starting')
        return len(self.__timeslices)

    def __str__(self):
        logger = create_logger('Day.__str__')
        logger.debug('starting')
        return self.start_date.strftime('%c')

    def __eq__(self, other: "Day") -> bool:
        logger = create_logger('Day.__eq__')
        logger.debug('starting')
        return self.start_date == other.start_date

    def __neq__(self, other: "Day") -> bool:
        logger = create_logger('Day.__neq__')
        logger.debug('starting')
        return self.start_date != other.start_date

    def __lt__(self, other: "Day") -> bool:
        logger = create_logger('Day.__lt__')
        logger.debug('starting')
        return self.start_date < other.start_date

    def __le__(self, other: "Day") -> bool:
        logger = create_logger('Day.__le__')
        logger.debug('starting')
        return self.start_date <= other.start_date

    def __gt__(self, other: "Day") -> bool:
        logger = create_logger('Day.__gt__')
        logger.debug('starting')
        return self.start_date > other.start_date

    def __ge__(self, other: "Day") -> bool:
        logger = create_logger('Day.__ge__')
        logger.debug('starting')
        return self.start_date >= other.start_date
