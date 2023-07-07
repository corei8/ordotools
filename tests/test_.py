from datetime import today
from ordotools import LiturgicalCalendar

def test_basic():
    assert LiturgicalCalendar(today.strftime("%Y"), "roman")

