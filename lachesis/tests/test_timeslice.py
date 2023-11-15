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
        start_time = datetime(year=2023,
                              month=11,
                              day=1,
                              hour=0,
                              minute=0,
                              second=0)
        next_time = datetime(year=2023,
                             month=11,
                             day=1,
                             hour=0,
                             minute=15,
                             second=0)
        #
        # Create the Timeslice object we'll test first.
        starting_slice = Timeslice(start_time=start_time)
        self.assertIsInstance(starting_slice, Timeslice)
        # pylint: disable=protected-access
        self.assertIsNone(starting_slice._next)
        self.assertTrue(starting_slice.is_last)
        self.assertEqual(str(starting_slice),
                         start_time.strftime('%c'))
        #
        # Test that we can now get the next slice, and
        # that the date/time matches what we expect.
        self.assertIsInstance(starting_slice.next,
                              Timeslice)
        self.assertEqual(starting_slice.next.start_time,
                         next_time)
        self.assertEqual(starting_slice,
                         starting_slice.next.previous)
        self.assertEqual(str(starting_slice.next),
                         next_time.strftime('%c'))
        #
        # Now that the first slice isn't first, we'll
        # verify that we get the right data back and
        # that the new slice knows that it's last.
        self.assertFalse(starting_slice.is_last)
        self.assertTrue(starting_slice.next.is_last)
