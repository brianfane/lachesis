r"""
Tests for the Timeslice objects.
"""

import unittest
from datetime import datetime
from lachesis.timeslice import Timeslice

class TestTimeslices(unittest.TestCase):
    r"""
    Tests for Timeslice objects.
    """
    def test_timeslices(self):
        r"""
        Test creating and working with Timeslice objects.
        """
        #
        # Initialize some variables.
        slice_time = datetime(year=2023,
                              month=11,
                              day=1,
                              hour=0,
                              minute=0,
                              second=0)
        #
        # Create the Timeslice object we'll test first.
        starting_slice = Timeslice(start_time=slice_time)
        self.assertIsInstance(starting_slice, Timeslice)
        self.assertEqual(str(starting_slice),
                         slice_time.strftime('%c'))

    def test_equal(self):
        r"""
        Test the __eq__() method
        """
        #
        # Initialize some variables.
        slice_time1 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        slice_time2 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        #
        # Create slices.
        slice1 = Timeslice(start_time=slice_time1)
        slice2 = Timeslice(start_time=slice_time2)
        #
        # Assertions
        self.assertEqual(slice1, slice2)
        self.assertTrue(slice1 == slice2)
        self.assertFalse(slice1 < slice2)
        self.assertFalse(slice1 != slice2)

    def test_not_equal(self):
        r"""
        Test the __neq__() method
        """
        #
        # Initialize some variables.
        slice_time1 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        slice_time2 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=15,
                               second=0)
        #
        # Create slices.
        slice1 = Timeslice(start_time=slice_time1)
        slice2 = Timeslice(start_time=slice_time2)
        #
        # Assertions
        self.assertNotEqual(slice1, slice2)
        self.assertTrue(slice1 != slice2)
        self.assertFalse(slice1 == slice2)

    def test_less_than(self):
        r"""
        Test the __lt__() method
        """
        #
        # Initialize some variables.
        slice_time1 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        slice_time2 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=15,
                               second=0)
        #
        # Create slices.
        slice1 = Timeslice(start_time=slice_time1)
        slice2 = Timeslice(start_time=slice_time2)
        #
        # Assertions
        self.assertLess(slice1, slice2)
        self.assertTrue(slice1 < slice2)
        self.assertFalse(slice1 == slice2)

    def test_less_than_equal(self):
        r"""
        Test the __le__() method
        """
        #
        # Initialize some variables.
        slice_time1 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        slice_time2 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        slice_time3 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=15,
                               second=0)
        #
        # Create slices.
        slice1 = Timeslice(start_time=slice_time1)
        slice2 = Timeslice(start_time=slice_time2)
        slice3 = Timeslice(start_time=slice_time3)
        #
        # Assertions
        self.assertLessEqual(slice1, slice2)
        self.assertLessEqual(slice1, slice3)
        self.assertTrue(slice1 <= slice2)
        self.assertTrue(slice1 <= slice3)

    def test_greater_than(self):
        r"""
        Test the __gt__() method
        """
        #
        # Initialize some variables.
        slice_time1 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        slice_time2 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=15,
                               second=0)
        #
        # Create slices.
        slice1 = Timeslice(start_time=slice_time1)
        slice2 = Timeslice(start_time=slice_time2)
        #
        # Assertions
        self.assertGreater(slice2, slice1)
        self.assertTrue(slice2 > slice1)
        self.assertFalse(slice1 == slice2)

    def test_greater_than_equal(self):
        r"""
        Test the __ge__() method
        """
        #
        # Initialize some variables.
        slice_time1 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        slice_time2 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=0,
                               second=0)
        slice_time3 = datetime(year=2023,
                               month=11,
                               day=1,
                               hour=0,
                               minute=15,
                               second=0)
        #
        # Create slices.
        slice1 = Timeslice(start_time=slice_time1)
        slice2 = Timeslice(start_time=slice_time2)
        slice3 = Timeslice(start_time=slice_time3)
        #
        # Assertions
        self.assertGreaterEqual(slice2, slice1)
        self.assertGreaterEqual(slice3, slice1)
        self.assertTrue(slice2 >= slice1)
        self.assertTrue(slice3 >= slice1)
