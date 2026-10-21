# Graph Report - ordotools  (2026-09-26)

## Corpus Check
- 95 files · ~122,931 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 2, .sqlite3 2, .csv 1)

## Summary
- 674 nodes · 1191 edges · 51 communities (39 shown, 12 thin omitted)
- Extraction: 95% EXTRACTED · 4% INFERRED · 1% AMBIGUOUS · INFERRED: 53 edges (avg confidence: 0.91)
- Token cost: 178,833 input · 0 output

## Community Hubs (Navigation)
- YAML to SQLite Build
- Flask Admin Routes
- Temporal Cycle Seasons
- Epact and Date Math
- Temporal YAML Export
- Project Docs and CI
- Liturgical Season Spans
- Legacy Temporal Data
- Australian and Spanish Calendars
- Algorithm Helpers
- Sanctoral Feast Repository
- Optimized Temporal Builder
- Fasting and Abstinence
- Temporal Feast Repository
- Commemoration Handling
- Country Calendar Modules
- Dioceses Repository
- Test Suite and Perf Tracking
- Benchmark Tool
- Easter and Year Marks
- LiturgicalCalendar Core
- Rank and Precedence
- Feasts Repository Resolution
- Legacy Build Pipeline Snippet
- Shell Runner Script
- Bathurst Diocese Module
- Melbourne Diocese Module
- Rockhampton Diocese Module
- Sanctoral Year Cache
- py-spy Profiling
- Lismore Diocese Module
- Maitland Diocese Module
- Roman Sanctoral Module
- Multi-year Profiling
- Rennes Diocese Module
- Diocese Template
- cProfile Runs
- Date Iteration Tests
- Rich Console Runner
- Performance Trend Chart
- Migration Scripts Package
- Repositories Package
- Pylint CI

## God Nodes (most connected - your core abstractions)
1. `day()` - 32 edges
2. `get_connection()` - 31 edges
3. `LiturgicalCalendar` - 26 edges
4. `Feast` - 24 edges
5. `days()` - 23 edges
6. `TemporalData` - 21 edges
7. `weeks()` - 20 edges
8. `Translations` - 20 edges
9. `get_repositories()` - 20 edges
10. `Temporal` - 18 edges

## Surprising Connections (you probably didn't know these)
- `LiturgicalCalendar (legacy snippet)` --semantically_similar_to--> `LiturgicalCalendar`  [AMBIGUOUS] [semantically similar]
  previous_snippets.txt → ordotools/tools/main.py
- `Ordotools (Traditional Catholic Ordo and Calendar)` --semantically_similar_to--> `Ordotools README (reStructuredText)`  [INFERRED] [semantically similar]
  README.md → README.rst
- `LiturgicalCalendar.build()` --conceptually_related_to--> `1950 expected calendar (MM-DD feast names)`  [AMBIGUOUS]
  previous_snippets.txt → test_files/1950.txt
- `test_basic()` --calls--> `LiturgicalCalendar`  [EXTRACTED]
  tests/test_.py → ordotools/tools/main.py
- `PyPI Publish Workflow` --conceptually_related_to--> `Ordotools (Traditional Catholic Ordo and Calendar)`  [INFERRED]
  .github/workflows/python-publish.yml → README.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Flask web admin UI for feast data** — web_interface_templates_browse, web_interface_templates_feasts, web_interface_templates_index, web_interface_api_dioceses [INFERRED 0.85]
- **GitHub Actions CI/CD** — _github_workflows_pylint, _github_workflows_python_publish, _github_workflows_static [INFERRED 0.85]
- **Seasons of the temporal cycle** — data_temporal_temporal_cycle_advent, data_temporal_temporal_cycle_christmastide, data_temporal_temporal_cycle_epiphanytide, data_temporal_temporal_cycle_septuagesima, data_temporal_temporal_cycle_lent, data_temporal_temporal_cycle_eastertide, data_temporal_temporal_cycle_pentecost_season [EXTRACTED 1.00]
- **Feast precedence determination fields** — data_temporal_temporal_cycle_rank_numeric, data_temporal_temporal_cycle_rank_verbose, data_temporal_temporal_cycle_nobility, data_temporal_temporal_cycle_office_type [INFERRED 0.85]
- **St. Patrick elevated to d I cl cum Oct across Australia and its dioceses (overriding Roman d)** — data_countries_australiae_australiapatricii, data_dioceses_bathurstensis_bathpatricii, data_dioceses_lismorensis_lismorenpatricii, data_dioceses_maitlandensis_4500, data_dioceses_melbournensis_melbournenpatricii, data_dioceses_roman_patricii [INFERRED 0.95]
- **Australian dioceses inheriting from australiae country calendar** — data_countries_australiae, data_dioceses_bathurstensis, data_dioceses_lismorensis, data_dioceses_maitlandensis, data_dioceses_melbournensis [EXTRACTED 1.00]

## Communities (51 total, 12 thin omitted)

### Community 0 - "YAML to SQLite Build"
Cohesion: 0.05
Nodes (60): Any, build_from_yaml(), check_duplicates(), # TODO: add a separate module based on language, # TODO: look at the commemorations and search for the feast data, # NOTE: this might be somewhat of a hack..., collections, Connection (+52 more)

### Community 1 - "Flask Admin Routes"
Cohesion: 0.07
Nodes (45): route, browse_countries(), browse_data(), browse_dioceses(), browse_sanctoral(), browse_temporal(), browse_translations(), delete_sanctoral_feast() (+37 more)

### Community 2 - "Temporal Cycle Seasons"
Cohesion: 0.08
Nodes (35): Advent, Ascension, Ash Wednesday, Christ the King, Christmas, Christmastide / Octave of Christmas, Commemoration orations (99901-99915), Corpus Christi (+27 more)

### Community 3 - "Epact and Date Math"
Cohesion: 0.12
Nodes (15): epact(), epact_adjust(), epact_build(), epact_chart(), golden_number(), integer_to_roman(), nth(), This function is guaranteed to be accurate (+7 more)

### Community 4 - "Temporal YAML Export"
Cohesion: 0.10
Nodes (25): BaseModel, clean_mass_dict(), CleanDumper, load_python_file(), migrate_temporal(), Custom dumper to add spacing between feasts for Neovim readability., Recursively renames keys and preserves booleans., CleanDumper (+17 more)

### Community 5 - "Project Docs and CI"
Cohesion: 0.08
Nodes (26): PyPI Publish Workflow, GitHub Pages Deploy Workflow, output/html static site, ordo.media test website, Ordotools (Traditional Catholic Ordo and Calendar), Ordotools README (reStructuredText), run.py demo script, requirements.txt (Flask, PyYAML, pytest, matplotlib) (+18 more)

### Community 6 - "Liturgical Season Spans"
Cohesion: 0.12
Nodes (16): days(), return a timedelta week, with integers as the input, return a timedelta day(s), with integers as the input, weeks(), Epiphany and its Sundays, Calculates the liturgical calendar structure. Returns a map of {datetime:…, All of the Sundays and ferias after Epiphany, Septuagesima to Quinquagesima (+8 more)

### Community 7 - "Legacy Temporal Data"
Cohesion: 0.12
Nodes (9): # TODO: add the Sundays if the fall on St. Thomas or St. Sylvester, # TODO: add the first 4 Sundays after Pentecost (excluding Trinity), This is really rough and might not be too efficient, but it works for now., # NOTE: this is overkill, but it works, and is probably faster than a fix, # TODO: check the verbose rank, # TODO: this day has special rules, # TODO: see if this is right, # TODO: see if the first two ferias are 2 or 3 (+1 more)

### Community 8 - "Australian and Spanish Calendars"
Cohesion: 0.12
Nodes (23): Australiae (country calendar), St. Patrick (Australia, d I cl cum Oct), Hispaniae (country calendar, incomplete stub), D. Bathursten (diocese calendar), St. Patrick (Bathurst), D. Lismoren (diocese calendar), St. Patrick (Lismore), D. Maitlanden (diocese calendar) (+15 more)

### Community 9 - "Algorithm Helpers"
Cohesion: 0.15
Nodes (17): dateutil_easter, functools, Optimized implementation of selected methods from temporal.py This file…, last_sunday(), latex_replacement(), leap_year(), datetime, return the weekday, with datetime as the input (+9 more)

### Community 10 - "Sanctoral Feast Repository"
Cohesion: 0.12
Nodes (11): datetime, Row, Repository for accessing sanctoral feast data from database., Convert database row to feast dictionary format., Save a sanctoral feast (insert or update)., Get a single sanctoral feast by ID., Delete a sanctoral feast., Close database connection. (+3 more)

### Community 11 - "Optimized Temporal Builder"
Cohesion: 0.15
Nodes (10): OptimizedTemporal, datetime, Optimized version of the Temporal class for better performance. Key…, Calculate the number of Sundays after Epiphany, Returns a dictionary of the entire temporal cycle. Optimized version that uses…, Optimized version of return_temporal that reduces redundant lookups and…, Cached version of weekday function, Optimized Advent Season calculation (+2 more)

### Community 12 - "Fasting and Abstinence"
Cohesion: 0.16
Nodes (9): Fasting, friday_abstinence(), # TODO: if the feast is a holyday of obligation, there is no abstinence, # NOTE: all of these should be combined after they are finished, # TODO: days that change according to the locality, # NOTE: how to find all the ember days?, Feast, Determines octave status on the fly. (+1 more)

### Community 13 - "Temporal Feast Repository"
Cohesion: 0.15
Nodes (9): Row, Delete a temporal feast., Close database connection., Get a single temporal feast by ID., Get all temporal feasts., Convert database row to feast dictionary format., Save a temporal feast (insert or update)., Repository for accessing temporal feast data from database. (+1 more)

### Community 14 - "Commemoration Handling"
Cohesion: 0.21
Nodes (12): dataclasses, add_commemorations(), existing_commemoration(), fidelium(), Inserts the commemoration(s) into the Feast object. Expects IDs (strings or…, Adds the Fidelium oration to the Feast object. Must be used after the seasonal…, Finds the number of commemorations that are already in a Feast object., Adds the seasonal commeorations to the Feast object. Each add_commemoration()… (+4 more)

### Community 15 - "Country Calendar Modules"
Cohesion: 0.16
Nodes (8): Country, # NOTE:, Country, Proper days of a country, which are called by the diocese., Country, day(), Return a datetime object for the given date, Circumcision up to Septuagesima, excluding Epiphany

### Community 16 - "Dioceses Repository"
Cohesion: 0.13
Nodes (5): DiocesesRepository, Repository for accessing dioceses and countries data from database., Lookup using the new long-form name_english column., Get all dioceses in a country., Close database connection.

### Community 17 - "Test Suite and Perf Tracking"
Cohesion: 0.16
Nodes (14): parametrize, pytest, statistics, load_performance_history(), Test that country-specific calendar modules exist and can be imported. This…, Test and track the performance of calendar generation., Load performance history from JSON file., Save performance history to JSON file. (+6 more)

### Community 18 - "Benchmark Tool"
Cohesion: 0.21
Nodes (12): argparse, load_performance_history(), main(), plot_performance_trend(), Performance benchmark tool for Ordotools. This script runs a comprehensive…, Load performance history from JSON file., Save performance history to JSON file., Plot the performance trend over time. (+4 more)

### Community 19 - "Easter and Year Marks"
Cohesion: 0.21
Nodes (8): easter(), findsunday(), LiturgicalYearMarks, return the distance betweent the date and the previous Sunday, as timedelta.days, return the date of easter for this year, # TODO: add D_HolyFamily as an option, # TODO: Christ the King is on the last Sunday of October, # TODO: clean up the Ascension days

### Community 20 - "LiturgicalCalendar Core"
Cohesion: 0.24
Nodes (4): LiturgicalCalendar, cal_merger(), IDs are now handled strictly as strings., TranslationsRepository

### Community 21 - "Rank and Precedence"
Cohesion: 0.29
Nodes (7): commemorate(), nobility(), rank(), # NOTE: I can't even remember what this means..., sort_criterion(), sorted_feasts(), transfer()

### Community 22 - "Feasts Repository Resolution"
Cohesion: 0.22
Nodes (6): FeastsRepository, Row, Get a single feast by ID (numeric string or temporal name)., Get feasts for a date, resolving Diocese -> Country -> Roman priority., Convert new schema row to dictionary with parsed JSON., Insert or update a feast using the unified schema.

### Community 23 - "Legacy Build Pipeline Snippet"
Cohesion: 0.33
Nodes (10): LiturgicalCalendar.add_feasts(), LiturgicalCalendar.add_translation(), LiturgicalCalendar.build(), Calendar build pipeline (temporal+sanctoral merge, octaves, BVM Saturday, commemorations, translation, fasting), LiturgicalCalendar.expand_octaves(), LiturgicalCalendar.find_octave(), LiturgicalCalendar (legacy snippet), LiturgicalCalendar.our_ladys_saturday() (+2 more)

### Community 24 - "Shell Runner Script"
Cohesion: 0.47
Nodes (8): env_bin_activate, main(), run_benchmark(), run_calendar(), run_tests(), setup_environment(), ordotools.sh script, show_help()

### Community 25 - "Bathurst Diocese Module"
Cohesion: 0.25
Nodes (5): importlib, Diocese, Proper days of a diocese, which calls a country., # HACK: just to get things started, # HACK: just to get things started

### Community 26 - "Melbourne Diocese Module"
Cohesion: 0.25
Nodes (5): Diocese, Proper days of a diocese, which calls a country., # HACK: just to get things started, # HACK: just to get things started, # NOTE:

### Community 27 - "Rockhampton Diocese Module"
Cohesion: 0.25
Nodes (5): Diocese, Proper days of a diocese, which calls a country., # HACK: just to get things started, # HACK: just to get things started, # NOTE:

### Community 28 - "Sanctoral Year Cache"
Cohesion: 0.32
Nodes (4): datetime, Simple repository to store and load sanctoral dict data by (diocese, year) into…, Idempotently insert a year's worth of feasts if not present. Keys are datetime…, SanctoralRepository

### Community 29 - "py-spy Profiling"
Cohesion: 0.32
Nodes (7): main(), Try different py-spy configurations to work around macOS issues, py-spy macOS compatibility script with multiple fallback approaches, Try alternative profiling methods, try_alternative_profilers(), try_pyspy_variants(), subprocess

### Community 30 - "Lismore Diocese Module"
Cohesion: 0.29
Nodes (4): Diocese, Proper days of a diocese, which calls a country., # HACK: just to get things started, # HACK: just to get things started

### Community 31 - "Maitland Diocese Module"
Cohesion: 0.29
Nodes (4): Diocese, Proper days of a diocese, which calls a country., # HACK: just to get things started, # HACK: just to get things started

### Community 32 - "Roman Sanctoral Module"
Cohesion: 0.29
Nodes (4): # TODO: We need to have a method for events on any day. Greater Litanies, for…, # TODO: get the correct antiphons, The Roman Sanctoral Cycle, which is called at every compilation. |…, Sanctoral

### Community 33 - "Multi-year Profiling"
Cohesion: 0.40
Nodes (3): profile_multiple_years(), Run your calendar generation multiple times for better profiling, time

### Community 34 - "Rennes Diocese Module"
Cohesion: 0.33
Nodes (3): Diocese, # HACK: just to get things started, # HACK: just to get things started

### Community 35 - "Diocese Template"
Cohesion: 0.33
Nodes (3): Diocese, # HACK: just to get things started, # HACK: just to get things started

### Community 36 - "cProfile Runs"
Cohesion: 0.50
Nodes (3): cprofile, # TODO: we need to add the language, pstats

### Community 38 - "Rich Console Runner"
Cohesion: 0.40
Nodes (3): rich_console, rich_table, # TODO: turn the entire run into a class and we can choose the output

### Community 39 - "Performance Trend Chart"
Cohesion: 0.67
Nodes (4): Average Build Time (seconds), Calendar Generation, Calendar Generation Performance Over Time (chart), Build time regression ~5.5ms to ~6.3ms (2025-02-27)

## Ambiguous Edges - Review These
- `LiturgicalCalendar` → `LiturgicalCalendar (legacy snippet)`  [AMBIGUOUS]
  previous_snippets.txt · relation: semantically_similar_to
- `GitHub Pages Deploy Workflow` → `ordo.media test website`  [AMBIGUOUS]
  .github/workflows/static.yml · relation: conceptually_related_to
- `LiturgicalCalendar.build()` → `1950 expected calendar (MM-DD feast names)`  [AMBIGUOUS]
  previous_snippets.txt · relation: conceptually_related_to
- `Hispaniae (country calendar, incomplete stub)` → `Feast YAML schema (id, name_translations, infra_oct_name, date, rank_verbose, rank_numeric, color, office_type, mass_properties, commemorations, nobility)`  [AMBIGUOUS]
  data/countries/hispaniae.yaml · relation: implements
- `D. Rhendonensis (Rennes diocese calendar, 21 feasts, la/fr)` → `Calendar hierarchy (Universal -> country -> diocese)`  [AMBIGUOUS]
  data/dioceses/rhendonensis.yaml · relation: conceptually_related_to
- `S Hilarii ECD (Roman)` → `Commemoration id 27400 (unresolved reference)`  [AMBIGUOUS]
  data/dioceses/roman.yaml · relation: references

## Knowledge Gaps
- **23 isolated node(s):** `Pylint CI Workflow`, `PyPI Publish Workflow`, `output/html static site`, `run.py demo script`, `Ordotools README (reStructuredText)` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 271 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `LiturgicalCalendar` and `LiturgicalCalendar (legacy snippet)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `GitHub Pages Deploy Workflow` and `ordo.media test website`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `LiturgicalCalendar.build()` and `1950 expected calendar (MM-DD feast names)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Hispaniae (country calendar, incomplete stub)` and `Feast YAML schema (id, name_translations, infra_oct_name, date, rank_verbose, rank_numeric, color, office_type, mass_properties, commemorations, nobility)`?**
  _Edge tagged AMBIGUOUS (relation: implements) - confidence is low._
- **What is the exact relationship between `D. Rhendonensis (Rennes diocese calendar, 21 feasts, la/fr)` and `Calendar hierarchy (Universal -> country -> diocese)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `S Hilarii ECD (Roman)` and `Commemoration id 27400 (unresolved reference)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `LiturgicalCalendar` connect `LiturgicalCalendar Core` to `Multi-year Profiling`, `cProfile Runs`, `Date Iteration Tests`, `Liturgical Season Spans`, `Rich Console Runner`, `Fasting and Abstinence`, `Commemoration Handling`, `Test Suite and Perf Tracking`, `Benchmark Tool`, `Feasts Repository Resolution`, `Legacy Build Pipeline Snippet`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._