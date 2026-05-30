from datetime import date

from curvelab.core.dates import date_to_internal_date

def test_epoch_date():
    # Test that the epoch date (2000-01-01) converts to 0
    assert date_to_internal_date(date(2000, 1, 1)) == 0

import sys

for p in sys.path:
    print(p)