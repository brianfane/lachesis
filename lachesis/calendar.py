r"""
calendar.py
"""

from collections.abc import Mapping
from datetime import date, timedelta
from lachesis.util import create_logger
from lachesis.day import Day

class Calendar(Mapping):
    r"""
    A Calendar object.
    """
    def __init__(self, start_date: date):
        logger = create_logger('Calendar.__init__')
        logger.debug('starting')
        self.start_date = start_date
        self.__days = {}
        self.__days[start_date] = Day(start_date=start_date)
        logger.debug('ending')

    def __getitem__(self, item_key):
        logger = create_logger('Calendar.__init__')
        logger.debug('starting')
        #
        # Verify that item_key is the correct data type.
        if not isinstance(item_key, date):
            logger.debug('item_key must be a date object')
            raise ValueError
        #
        # Try to get a day out of our calendar.
        try:
            logger.debug('attempt to return specific Day')
            return self.__days[item_key]
        except KeyError:
            logger.debug('Day did not exist; creating new one')
            self.__days[item_key] = Day(start_date=item_key)
            return self.__days[item_key]

    def __iter__(self):
        logger = create_logger('Calendar.__iter__')
        logger.debug('starting')
        # Define where this iterator will stop.
        last_day = max(self.__days.keys())
        if last_day < date.today():
            last_day = date.today()
        #
        # Now we'll loop through each day, using the
        # __getitem__() method to get (or create) specific
        # days.
        curr_dt = self.start_date
        logger.debug('starting while-loop')
        while curr_dt <= last_day:
            logger.debug('yielding Day')
            yield self[curr_dt]
            curr_dt += timedelta(days=1)
        logger.debug('ending')

    def __len__(self):
        logger = create_logger('Calendar.__len__')
        logger.debug('starting')
        return len(self.__days)
