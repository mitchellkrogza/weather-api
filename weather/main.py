from argparse import ArgumentParser
from .weather import Weather
import sys


def main():
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        "-unit",
        default="c",
        choices=["c","f"],
        help="Units C or F."
    )
    PARSER.add_argument(
        "-f",
        "--forecast",
        action="store_true",
        help="Pass this argument to get a weather forecast."
    )
    PARSER.add_argument(
        "-s",
        "--start",
        default="1",
        action="store_true",
        help="Start Day."
    )
    PARSER.add_argument(
        "-e",
        "--end",
        default="3",
        action="store_true",
        help="End Day."
    )
    PARSER.add_argument(
        "location",
        help="The location to lookup."
    )
    ARGS = PARSER.parse_args()
    weather = Weather(ARGS.unit)
    loc = weather.lookup_by_location(ARGS.location)
    condition = loc.condition
    print("Weather report for %s, %s" % (loc.location.city, loc.location.country))
    print("Condition: %s " % condition.text)
    print("Temperature: %s" % condition.temp)

    if ARGS.forecast()
        start = 0 if not ARGS.start else ARGS.start # If the start argument isn't set, set the start as the first element in the forecast array.
        end =  len(location.forecast) if not ARGS.end else ARGS.end # if the end argument isn't set, set the end as the last element in the forecast array.
    for forecast in location.forecast[start:end]:
        print("Day%s: %s" % (start, forecast.text))
        start += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
