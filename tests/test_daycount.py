from datetime import date
from curvelab.core.daycount import Act365, Act360, ActActISDA
from curvelab.core.dates import date_to_internal_date


def test_act365_one_year():
    assert Act365().year_fraction(0, 365) == 1.0


def test_act360_one_year():
    assert Act360().year_fraction(0, 360) == 1.0


def test_act_act_isda_same_year_non_leap():
    start = date_to_internal_date(date(2026, 1, 1))
    end = date_to_internal_date(date(2026, 7, 1))
    assert ActActISDA().year_fraction(start, end) == 181 / 365


def test_act_act_isda_full_leap_year():
    start = date_to_internal_date(date(2024, 1, 1))
    end = date_to_internal_date(date(2025, 1, 1))
    assert ActActISDA().year_fraction(start, end) == 1.0


def test_act_act_isda_full_non_leap_year():
    start = date_to_internal_date(date(2025, 1, 1))
    end = date_to_internal_date(date(2026, 1, 1))
    assert ActActISDA().year_fraction(start, end) == 1.0


def test_act_act_isda_across_leap_year():
    start = date_to_internal_date(date(2023, 7, 1))
    end = date_to_internal_date(date(2024, 7, 1))
    expected = (184 / 365 + 182 / 366)
    assert ActActISDA().year_fraction(start, end) == expected


def test_act_act_isda_same_day():
    d = date_to_internal_date(date(2026, 1, 1))
    assert ActActISDA().year_fraction(d, d) == 0.0