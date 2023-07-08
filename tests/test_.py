from datetime import datetime
from ordotools import LiturgicalCalendar

def test_basic():
    assert LiturgicalCalendar(int(datetime.today().strftime("%Y")), "roman")
    assert LiturgicalCalendar(2024, "roman")
    assert LiturgicalCalendar(2025, "roman")
    assert LiturgicalCalendar(2026, "roman")
    assert LiturgicalCalendar(2027, "roman")
    assert LiturgicalCalendar(2028, "roman")
    assert LiturgicalCalendar(2029, "roman")
    assert LiturgicalCalendar(2030, "roman")
    assert LiturgicalCalendar(2031, "roman")
    assert LiturgicalCalendar(2032, "roman")
    assert LiturgicalCalendar(2033, "roman")
    assert LiturgicalCalendar(2034, "roman")
    assert LiturgicalCalendar(2035, "roman")
    # for x in range(2023, 2050):
    #     assert LiturgicalCalendar(x, "roman")

