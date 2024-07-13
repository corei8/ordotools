from ordotools import LiturgicalCalendar
from cProfile import Profile
from pstats import SortKey, Stats

# TODO: we need to add the language

with Profile() as profile:

    data = LiturgicalCalendar(2024, "roman", "la").build()

    (
        Stats(profile)
        .strip_dirs()
        .sort_stats(SortKey.CUMULATIVE)
        .print_stats()
    )
