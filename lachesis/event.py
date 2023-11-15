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
                 start: datetime,
                 length: timedelta):
        r"""
        Initialize the event.
        """
        self.name = name
        self.start = start
        self.length = length
