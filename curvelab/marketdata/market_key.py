from dataclasses import dataclass


@dataclass(frozen=True)
class MarketKey:
    """
    Parsed market key.

    Expected format:
    <CCY>_<INSTRUMENT>_<TENOR>

    Examples:
    PLN_DEPO_3M
    PLN_FRA_1X4
    PLN_IRS_2Y
    """

    raw: str

    @property
    def parts(self) -> list[str]:
        parts = self.raw.split("_")

        if len(parts) != 3:
            raise ValueError(f"Invalid market key: {self.raw}")

        return parts

    @property
    def currency(self) -> str:
        return self.parts[0]

    @property
    def instrument_type(self) -> str:
        return self.parts[1]

    @property
    def tenor(self) -> str:
        return self.parts[2]
