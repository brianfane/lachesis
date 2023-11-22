r"""
Tests for the Calendar class
"""

import unittest
from datetime import date, timedelta
from lachesis.calendar import Calendar
from lachesis.day import Day

class TestCalendar(unittest.TestCase):
    r"""
    Tests for the Calendar class
    """
    def test_calendar(self):
        r"""
        Test creating a calendar and fetching
        the first day.
        """
        #
        # Initialize the first day.
        start_date = date(year=2023,
                          month=1,
                          day=1)
        cal = Calendar(start_date=start_date)
        self.assertIsInstance(cal, Calendar)
        self.assertIsInstance(cal.start_date, date)

    def test_getitem(self):
        r"""
        Test the __getitem__() method
        """
        #
        # Initialize the some days.
        start_date = date(year=2023,
                          month=1,
                          day=1)
        new_day = date(year=2023,
                       month=11,
                       day=15)
        cal = Calendar(start_date=start_date)
        gotten_day = cal[new_day]
        self.assertIsInstance(gotten_day, Day)
        self.assertEqual(gotten_day.start_date, new_day)
        #
        # Verify that the method returns the proper exception when
        # given the wrong data type as a key.
        with self.assertRaises(ValueError):
            _ = cal[10]

    def test_len(self):
        r"""
        Test the __len__() method
        """
        start_date = date(year=2023,
                          month=1,
                          day=1)
        new_day = date(year=2023,
                       month=11,
                       day=15)
        #
        # Create the calendar and verify that the it has
        # a length of just 1 (the initial day).
        cal = Calendar(start_date=start_date)
        self.assertEqual(len(cal), 1)
        #
        # Get a second day and verify that the length
        # becomes 2.
        _ = cal[new_day]
        self.assertEqual(len(cal), 2)

    def test_iter_1(self):
        r"""
        Test the __iter__() method, case #1: iteration
        ending today.
        """
        start_date = date(year=2023,
                          month=1,
                          day=1)
        cal = Calendar(start_date=start_date)
        for next_day in cal:
            self.assertIsInstance(next_day, Day)
            last_day = next_day
        #
        # The last day in our sequence should today.
        self.assertEqual(last_day.start_date, date.today())

    def test_iter_2(self):
        r"""
        Test the __iter__() method, case #2: iteration
        ending on last created date.
        """
        start_date = date(year=2023,
                          month=1,
                          day=1)
        end_date = date.today() + timedelta(days=14)
        cal = Calendar(start_date=start_date)
        _ = cal[end_date]
        for next_day in cal:
            self.assertIsInstance(next_day, Day)
            last_day = next_day
        #
        # The last day in our sequence should today.
        self.assertEqual(last_day.start_date, end_date)
