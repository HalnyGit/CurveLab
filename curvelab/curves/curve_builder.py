from curvelab.core.dates import add_months, date_to_internal_date, internal_date_to_date
from curvelab.core.daycount import Act365
from curvelab.core.schedule import Frequency
from curvelab.curves.curve import Curve
from curvelab.curves.curve_definition import CurveDefinition
from curvelab.marketdata.market_data_set import MarketDataSet


class CurveBuilder:
    """
    Builds curves from market data.

    v1:
    - supports DEPO market keys only
    """

    def build(
        self,
        curve_definition: CurveDefinition,
        market_data_set: MarketDataSet,
    ) -> Curve:
        points: list[tuple[int, float]] = []

        for market_key in curve_definition.market_keys:
            quote = market_data_set.get_quote(market_key)

            if "_DEPO_" not in market_key:
                raise NotImplementedError(
                    f"Unsupported market key: {market_key}"
                )

            tenor = market_key.split("_")[-1]
            months = self._parse_months(tenor)

            valuation_date = internal_date_to_date(
                market_data_set.valuation_date
            )

            maturity_date = add_months(valuation_date, months)
            maturity_internal_date = date_to_internal_date(maturity_date)

            tau = Act365().year_fraction(
                market_data_set.valuation_date,
                maturity_internal_date,
            )

            discount_factor = 1 / (1 + quote.value * tau)

            points.append(
                (maturity_internal_date, discount_factor)
            )

        return Curve(
            curve_name=curve_definition.curve_name,
            valuation_date=market_data_set.valuation_date,
            points=points,
        )

    def _parse_months(self, tenor: str) -> int:
        if tenor.endswith("M"):
            return int(tenor[:-1])

        raise ValueError(f"Unsupported tenor: {tenor}")
