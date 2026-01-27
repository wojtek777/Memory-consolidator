# app/memory/range.py
from datetime import datetime

class Range:
    def __init__(self, start: datetime, end: datetime | None = None):
        self.start = start
        self.end = end  # None = infinite

    def contains(self, value: datetime) -> bool:
        return self.start <= value and (self.end is None or value <= self.end)

    def overlaps(self, other: "Range") -> bool:
        return self.start <= (other.end or datetime.max) and other.start <= (self.end or datetime.max)

    def __repr__(self):
        return f"Range(start={self.start}, end={self.end})"

