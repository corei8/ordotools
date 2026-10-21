#!/usr/bin/env bash
#
# ordotools - CLI wrapper for Ordotools operations
#

# Colors for formatting output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Set script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Ensure virtualenv is activated if it exists
if [ -d "$SCRIPT_DIR/env" ]; then
    source "$SCRIPT_DIR/env/bin/activate"
fi

# Help function
show_help() {
    echo -e "${BOLD}Ordotools CLI${NC}"
    echo
    echo -e "A command-line interface for the Ordotools liturgical calendar generator"
    echo
    echo -e "${BOLD}Usage:${NC}"
    echo -e "  ./ordotools.sh [command] [options]"
    echo
    echo -e "${BOLD}Commands:${NC}"
    echo -e "  ${GREEN}run${NC}          Generate a calendar (default command)"
    echo -e "  ${GREEN}sweep${NC}        Build every year in a range and report failures"
    echo -e "  ${GREEN}test${NC}         Run tests"
    echo -e "  ${GREEN}benchmark${NC}    Run performance benchmarks"
    echo -e "  ${GREEN}setup${NC}        Setup development environment"
    echo -e "  ${GREEN}help${NC}         Display this help message"
    echo
    echo -e "${BOLD}Options for 'run':${NC}"
    echo -e "  ${YELLOW}-y, --year${NC} YEAR       Year to generate (default: current year)"
    echo -e "  ${YELLOW}-d, --diocese${NC} DIOCESE  Diocese to use (default: roman)"
    echo -e "  ${YELLOW}-l, --lang${NC} LANG        Language (default: la)"
    echo -e "  ${YELLOW}--dump${NC}                 Dump calendar to stdout in readable format"
    echo
    echo -e "${BOLD}Options for 'sweep':${NC}"
    echo -e "  ${YELLOW}-d, --dioceses${NC} DIOCESES Comma-separated list of dioceses (default: roman)"
    echo -e "  ${YELLOW}-l, --lang${NC} LANG        Language (default: la)"
    echo -e "  ${YELLOW}--from${NC} YEAR            First year (default: 1900)"
    echo -e "  ${YELLOW}--to${NC} YEAR              Last year (default: 3500)"
    echo
    echo -e "${BOLD}Options for 'test':${NC}"
    echo -e "  ${YELLOW}-p, --performance${NC}      Run performance tests"
    echo -e "  ${YELLOW}-b, --basic${NC}            Run basic tests"
    echo -e "  ${YELLOW}-a, --all${NC}              Run all tests"
    echo -e "  ${YELLOW}-v, --verbose${NC}          Verbose output"
    echo
    echo -e "${BOLD}Options for 'benchmark':${NC}"
    echo -e "  ${YELLOW}-y, --years${NC} YEARS      Comma-separated list of years (default: 2025,2026,2027)"
    echo -e "  ${YELLOW}-r, --runs${NC} RUNS        Number of runs per test (default: 5)"
    echo -e "  ${YELLOW}-d, --dioceses${NC} DIOCESES Comma-separated list of dioceses (default: roman)"
    echo
    echo -e "${BOLD}Examples:${NC}"
    echo -e "  ./ordotools.sh run -y 2025 -d roman --dump"
    echo -e "  ./ordotools.sh sweep -d roman,melbournensis"
    echo -e "  ./ordotools.sh test -p"
    echo -e "  ./ordotools.sh benchmark -y 2025,2026 -r 3"
    echo
}

# Generate and display a calendar
run_calendar() {
    year=$(date +%Y)
    diocese="roman"
    lang="la"
    dump=false

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        key="$1"
        case $key in
            -y|--year)
                year="$2"
                shift
                shift
                ;;
            -d|--diocese)
                diocese="$2"
                shift
                shift
                ;;
            -l|--lang)
                lang="$2"
                shift
                shift
                ;;
            --dump)
                dump=true
                shift
                ;;
            *)
                echo -e "${RED}Unknown option: $1${NC}"
                show_help
                exit 1
                ;;
        esac
    done

    echo -e "${BLUE}Generating liturgical calendar for year $year, diocese $diocese, language $lang${NC}"
    
    # Create a temporary Python script for running with proper output
    if [ "$dump" = true ]; then
        python3 - << END
from ordotools import LiturgicalCalendar

calendar = LiturgicalCalendar($year, "$diocese", "$lang").build()

print(f"\n{'Date':<12} {'Rank':<15} {'Color':<10} {'Name'}")
print("-" * 80)

for feast in calendar:
    print(f"{feast.date.strftime('%Y-%m-%d'):<12} {feast.rank_verbose:<15} {feast.color:<10} {feast.name}")
END
    else
        # Run without detailed output - just build calendar
        python3 - << END
from ordotools import LiturgicalCalendar

calendar = LiturgicalCalendar($year, "$diocese", "$lang").build()
print(f"Successfully generated {len(calendar)} feast days")
END
    fi
}

# Build calendars for every year in a range, reporting any failures
run_sweep() {
    dioceses="roman"
    lang="la"
    start=1900
    end=3500

    while [[ $# -gt 0 ]]; do
        case $1 in
            -d|--dioceses) dioceses="$2"; shift 2 ;;
            -l|--lang) lang="$2"; shift 2 ;;
            --from) start="$2"; shift 2 ;;
            --to) end="$2"; shift 2 ;;
            *)
                echo -e "${RED}Unknown option: $1${NC}"
                show_help
                exit 1
                ;;
        esac
    done

    echo -e "${BLUE}Building $start-$end for diocese=$dioceses, language $lang${NC}"
    python3 - "$dioceses" "$lang" "$start" "$end" << 'END'
import signal, sys, time, traceback
from ordotools import LiturgicalCalendar
from ordotools.tools.rank import transferred_feasts

dioceses, lang, start, end = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

# a single build takes well under a second; anything past this is a hang
TIMEOUT = 10
def on_alarm(*_):
    raise TimeoutError(f"no result after {TIMEOUT}s (probably an infinite loop)")
signal.signal(signal.SIGALRM, on_alarm)

failures = []
t0 = time.time()
# for diocese in dioceses:
for year in range(start, end + 1):
	transferred_feasts.clear()  # module-level state; a timed-out build leaves leftovers
	signal.alarm(TIMEOUT)
	try:
		LiturgicalCalendar(year, dioceses, lang).build()
	except Exception as e:
		failures.append((dioceses, year, e))
		print(f"FAIL {dioceses} {year}: {type(e).__name__}: {e}", flush=True)
		if len(failures) == 1:
			traceback.print_exc()
	signal.alarm(0)
	if year % 100 == 0:
		print(f"  {dioceses}: {year}", flush=True)

total = len(dioceses) * (end - start + 1)
print(f"\n{total - len(failures)}/{total} calendars built in {time.time() - t0:.1f}s")
sys.exit(1 if failures else 0)
END
}

# Run tests
run_tests() {
    test_type=""
    verbose=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        key="$1"
        case $key in
            -p|--performance)
                test_type="test_performance"
                shift
                ;;
            -b|--basic)
                test_type="test_basic"
                shift
                ;;
            -a|--all)
                test_type=""
                shift
                ;;
            -v|--verbose)
                verbose="-v"
                shift
                ;;
            *)
                echo -e "${RED}Unknown option: $1${NC}"
                show_help
                exit 1
                ;;
        esac
    done

    echo -e "${BLUE}Running tests...${NC}"
    
    if [ -n "$test_type" ]; then
        pytest tests/test_.py::$test_type $verbose
    else
        pytest $verbose
    fi
}

# Run performance benchmarks
run_benchmark() {
    years="2025,2026,2027"
    runs=5
    dioceses="roman"

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        key="$1"
        case $key in
            -y|--years)
                years="$2"
                shift
                shift
                ;;
            -r|--runs)
                runs="$2"
                shift
                shift
                ;;
            -d|--dioceses)
                dioceses="$2"
                shift
                shift
                ;;
            *)
                echo -e "${RED}Unknown option: $1${NC}"
                show_help
                exit 1
                ;;
        esac
    done

    echo -e "${BLUE}Running benchmark with years=$years, runs=$runs, dioceses=$dioceses${NC}"
    "$SCRIPT_DIR/benchmark.py" --years "$years" --runs "$runs" --dioceses "$dioceses"
}

# Setup development environment
setup_environment() {
    echo -e "${BLUE}Setting up development environment...${NC}"
    
    if [ ! -d "$SCRIPT_DIR/env" ]; then
        echo -e "${YELLOW}Creating virtual environment...${NC}"
        python3 -m venv env
        source "$SCRIPT_DIR/env/bin/activate"
        echo -e "${GREEN}Virtual environment created and activated${NC}"
    else
        source "$SCRIPT_DIR/env/bin/activate"
        echo -e "${GREEN}Virtual environment activated${NC}"
    fi
    
    echo -e "${YELLOW}Installing dependencies...${NC}"
    pip install -r requirements.txt
    
    echo -e "${YELLOW}Installing package in development mode...${NC}"
    pip install -e .
    
    echo -e "${GREEN}Setup complete!${NC}"
}

# Main function that parses arguments and calls appropriate functions
main() {
    # Handle no arguments
    if [ $# -eq 0 ]; then
        run_calendar
        exit 0
    fi

    # Handle arguments
    command="$1"
    shift

    case $command in
        run)
            run_calendar "$@"
            ;;
        sweep)
            run_sweep "$@"
            ;;
        test)
            run_tests "$@"
            ;;
        benchmark)
            run_benchmark "$@"
            ;;
        setup)
            setup_environment
            ;;
        help)
            show_help
            ;;
        *)
            echo -e "${RED}Unknown command: $command${NC}"
            show_help
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"
