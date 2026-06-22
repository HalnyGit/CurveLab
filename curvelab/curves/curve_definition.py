from dataclasses import dataclass

from curvelab.core.dates import (
    add_months,
    date_to_internal_date,
    internal_date_to_date,
)


@dataclass(frozen=True)
class CurveDefinition:
    """
    Defines how a curve is built.
    """

    curve_name: str
    market_keys: list[str]


    def pillar_dates(self, valuation_date: int) -> list[int]:
        return [
            self._pillar_date_from_market_key(market_key, valuation_date)
            for market_key in self.market_keys
        ]

    def _pillar_date_from_market_key(
        self,
        market_key: str,
        valuation_date: int,
    ) -> int:
        parts = market_key.split("_")

        if len(parts) != 3:
            raise ValueError(f"Invalid market key: {market_key}")

        instrument_type = parts[1]
        tenor = parts[2]

        valuation_dt = internal_date_to_date(valuation_date)

        if instrument_type == "DEPO":
            months = self._parse_month_tenor(tenor)
            pillar_dt = add_months(valuation_dt, months)
            return date_to_internal_date(pillar_dt)

        if instrument_type == "FRA":
            end_month = self._parse_fra_end_month(tenor)
            pillar_dt = add_months(valuation_dt, end_month)
            return date_to_internal_date(pillar_dt)

        if instrument_type == "IRS":
            months = self._parse_tenor_to_months(tenor)
            pillar_dt = add_months(valuation_dt, months)
            return date_to_internal_date(pillar_dt)

        raise NotImplementedError(f"Unsupported instrument type: {instrument_type}")

    def _parse_month_tenor(self, tenor: str) -> int:
        if tenor.endswith("M"):
            return int(tenor[:-1])

        raise ValueError(f"Unsupported month tenor: {tenor}")

    def _parse_fra_end_month(self, tenor: str) -> int:
        parts = tenor.upper().split("X")

        if len(parts) != 2:
            raise ValueError(f"Unsupported FRA tenor: {tenor}")

        return int(parts[1])

    def _parse_tenor_to_months(self, tenor: str) -> int:
        if tenor.endswith("M"):
            return int(tenor[:-1])

        if tenor.endswith("Y"):
            return int(tenor[:-1]) * 12

        raise ValueError(f"Unsupported tenor: {tenor}")
