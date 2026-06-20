from dataclasses import dataclass

from curvelab.curves.curve import Curve
from curvelab.curves.curve_set import CurveSet


@dataclass(frozen=True)
class PricingContext:
    """
    Pricing context containing curves and curve mappings.
    """

    curve_set: CurveSet
    curve_map: dict[str, str]

    def get_curve(self, index_name: str) -> Curve:
        curve_name = self.curve_map[index_name]
        return self.curve_set.get(curve_name)
