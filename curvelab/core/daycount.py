from abc import ABC, abstractmethod
from datetime import date
from curvelab.core.dates import internal_date_to_date, days_in_year

class DayCount(ABC):
    """Base class for day count conventions."""

    @abstractmethod
    def year_fraction(self, start_date: int, end_date: int) -> float:
        """Return year fraction between two internal dates."""
        raise NotImplementedError


class Act365(DayCount):
    """ACT/365 day count convention."""

    def year_fraction(self, start_date: int, end_date: int) -> float:
        return (end_date - start_date) / 365.0


class Act360(DayCount):
    """ACT/360 day count convention."""

    def year_fraction(self, start_date: int, end_date: int) -> float:
        return (end_date - start_date) / 360.0

class ActActISDA(DayCount):
    """ACT/ACT ISDA day count convention."""

    def year_fraction(self, start_date: int, end_date: int) -> float:
        
        start = internal_date_to_date(start_date)
        end = internal_date_to_date(end_date)
        
        if start > end:
            raise ValueError("start_date must be before or equal to end_date")
        
        if start.year == end.year:
            return (
                (end - start).days
                / days_in_year(start.year)
            )

        result = 0.0

        current = start

        while current.year < end.year:
            next_year = date(current.year + 1, 1, 1)
            result += (
                (next_year - current).days
                / days_in_year(current.year)
            )
            current = next_year

        result += (
            (end - current).days
            / days_in_year(end.year)
        )

        return result




