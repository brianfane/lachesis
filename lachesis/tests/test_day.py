r"""
Tests for the Day objects.
"""

import unittest
from datetime import date, datetime
from lachesis.day import Day
from lachesis.timeslice import Timeslice

class TestDays(unittest.TestCase):
    r"""
    Tests for Day objects.
    """
    def test_days(self):
        r"""
        Test creating and working with Day objects.
        """
        #
        # Initialize some variables.
        start_date = date(year=2023,
                          month=11,
                          day=1)
        #
        # Create the Day object we'll test first.
        test_day = Day(day=start_date)
        self.assertIsInstance(test_day, Day)
        self.assertEqual(str(test_day),
                         start_date.strftime('%c'))

    def test_equal(self):
        r"""
        Test the __eq__() method
        """
        #
        # Initialize some variables.
        date1 = date(year=2023,
                     month=11,
                     day=1)
        date2 = date(year=2023,
                     month=11,
                     day=1)
        #
        # Create slices.
        day1 = Day(day=date1)
        day2 = Day(day=date2)
        #
        # Assertions
        self.assertEqual(day1, day2)
        self.assertTrue(day1 == day2)
        self.assertFalse(day1 < day2)
        self.assertFalse(day1 != day2)

    def test_not_equal(self):
        r"""
        Test the __neq__() method
        """
        #
        # Initialize some variables.
        date1 = date(year=2023,
                     month=11,
                     day=1)
        date2 = date(year=2023,
                     month=11,
                     day=2)
        #
        # Create slices.
        day1 = Day(day=date1)
        day2 = Day(day=date2)
        #
        # Assertions
        self.assertNotEqual(day1, day2)
        self.assertTrue(day1 != day2)
        self.assertFalse(day1 == day2)

    def test_less_than(self):
        r"""
        Test the __lt__() method
        """
        #
        # Initialize some variables.
        date1 = date(year=2023,
                     month=11,
                     day=1)
        date2 = date(year=2023,
                     month=11,
                     day=2)
        #
        # Create slices.
        day1 = Day(day=date1)
        day2 = Day(day=date2)
        #
        # Assertions
        self.assertLess(day1, day2)
        self.assertTrue(day1 < day2)
        self.assertFalse(day1 == day2)

    def test_less_than_equal(self):
        r"""
        Test the __le__() method
        """
        #
        # Initialize some variables.
        date1 = date(year=2023,
                     month=11,
                     day=1)
        date2 = date(year=2023,
                     month=11,
                     day=1)
        date3 = date(year=2023,
                     month=11,
                     day=2)
        #
        # Create slices.
        day1 = Day(day=date1)
        day2 = Day(day=date2)
        day3 = Day(day=date3)
        #
        # Assertions
        self.assertLessEqual(day1, day2)
        self.assertLessEqual(day1, day3)
        self.assertTrue(day1 <= day2)
        self.assertTrue(day1 <= day3)

    def test_greater_than(self):
        r"""
        Test the __gt__() method
        """
        #
        # Initialize some variables.
        date1 = date(year=2023,
                     month=11,
                     day=1)
        date2 = date(year=2023,
                     month=11,
                     day=2)
        #
        # Create slices.
        day1 = Day(day=date1)
        day2 = Day(day=date2)
        #
        # Assertions
        self.assertGreater(day2, day1)
        self.assertTrue(day2 > day1)
        self.assertFalse(day2 == day1)

    def test_greater_than_equal(self):
        r"""
        Test the __ge__() method
        """
        #
        # Initialize some variables.
        date1 = date(year=2023,
                     month=11,
                     day=1)
        date2 = date(year=2023,
                     month=11,
                     day=1)
        date3 = date(year=2023,
                     month=11,
                     day=2)
        #
        # Create slices.
        day1 = Day(day=date1)
        day2 = Day(day=date2)
        day3 = Day(day=date3)
        #
        # Assertions
        self.assertGreaterEqual(day2, day1)
        self.assertGreaterEqual(day3, day1)
        self.assertTrue(day2 >= day1)
        self.assertTrue(day3 >= day1)

    def test_getitem(self):
        r"""
        Test the __getitem__() method
        """
        date1 = date(year=2023,
                     month=11,
                     day=1)
        # pylint: disable=duplicate-code
        datetime1 = datetime(year=2023,
                             month=11,
                             day=1,
                             hour=0,
                             minute=0,
                             second=0)
        datetime2 = datetime(year=2023,
                             month=11,
                             day=1,
                             hour=12,
                             minute=0,
                             second=0)
        datetime3 = datetime(year=2023,
                             month=11,
                             day=2,
                             hour=0,
                             minute=0,
                             second=0)
        datetime4 = datetime(year=2023,
                             month=11,
                             day=1,
                             hour=12,
                             minute=7,
                             second=0)
        #
        day1 = Day(day=date1)
        slice1 = Timeslice(start_time=datetime1)
        slice2 = Timeslice(start_time=datetime2)
        #
        test_slice1 = day1[datetime1]
        test_slice2 = day1[datetime2]
        #
        # Test that we can get specific slices back
        # from a Day object.
        self.assertIsInstance(test_slice1, Timeslice)
        self.assertIsInstance(test_slice2, Timeslice)
        self.assertEqual(test_slice1, slice1)
        self.assertEqual(test_slice2, slice2)
        #
        # Verify that we cannot get slices that belong
        # to a different Day from this Day.
        with self.assertRaises(KeyError):
            _ = day1[datetime3]
        #
        # Verify that the slice starts on a quarter-hour.
        with self.assertRaises(KeyError):
            _ = day1[datetime4]

    def test_len(self):
        r"""
        Test the __len__() method
        """
        date1 = date(year=2023,
                     month=11,
                     day=1)
        # pylint: disable=duplicate-code
        datetime1 = datetime(year=2023,
                             month=11,
                             day=1,
                             hour=0,
                             minute=0,
                             second=0)
        datetime2 = datetime(year=2023,
                             month=11,
                             day=1,
                             hour=12,
                             minute=0,
                             second=0)
        datetime3 = datetime(year=2023,
                             month=11,
                             day=2,
                             hour=0,
                             minute=0,
                             second=0)
        datetime4 = datetime(year=2023,
                             month=11,
                             day=1,
                             hour=12,
                             minute=7,
                             second=0)
        #
        day1 = Day(day=date1)
        #
        self.assertEqual(len(day1), 0)
        #
        _ = day1[datetime1]
        self.assertEqual(len(day1), 1)
        #
        _ = day1[datetime2]
        self.assertEqual(len(day1), 2)
        #
        with self.assertRaises(KeyError):
            _ = day1[datetime3]
        self.assertEqual(len(day1), 2)
        #
        with self.assertRaises(KeyError):
            _ = day1[datetime4]
        self.assertEqual(len(day1), 2)
