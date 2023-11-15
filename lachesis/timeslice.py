r"""
Time-slices and functions to support them.
"""

from datetime import datetime, timedelta

class Timeslice:
    r"""
    A slice of time.
    """
    def __init__(self, start_time: datetime, previous: 'Timeslice'=None):
        self.start_time = start_time
        self.previous = previous
        self._next = None

    @property
    def next(self) -> 'Timeslice':
        r"""
        The next timeslice.
        """
        if not self._next:
            next_time = self.start_time + timedelta(minutes=15)
            self._next = Timeslice(start_time=next_time,
                                   previous=self)
        return self._next

    @property
    def is_last(self) -> bool:
        r"""
        Is this the last timeslice in our list?
        """
        return self._next is None

    def __str__(self) -> str:
        return self.start_time.strftime('%c')

    def __repr__(self) -> str:
        return str(self)
