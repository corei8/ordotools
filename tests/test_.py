from datetime import datetime
from ordotools import LiturgicalCalendar

def test_basic():
    assert LiturgicalCalendar(int(datetime.today().strftime("%Y")), "roman")
    assert LiturgicalCalendar(2024, "roman")
