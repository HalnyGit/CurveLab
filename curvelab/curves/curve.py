from dataclasses import dataclass


@dataclass(frozen=True)
class DiscountCurve:
    curve_name: str
    valuation_date: int
    points: list[tuple[int, float]]

    def discount_factor(self, date: int) -> float:
        for point_date, discount_factor in self.points:
            if point_date == date:
                return discount_factor

        raise KeyError(f"Discount factor not found for date: {date}")
