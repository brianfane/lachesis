r"""
An event.
"""

from datetime import datetime, timedelta

class Event:
    r"""
    An event.
    """
    def __init__(self,
                 name: str,
                 time_tracking: str,
                 start: datetime,
                 length: timedelta):
        r"""
        Initialize the event.
        """
        self.name = name
        self.time_tracking = time_tracking
        self.start = start
        self.length = length
