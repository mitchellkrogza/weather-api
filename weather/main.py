from .weather import Weather
import sys
import argparse

def main():
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        "location",
        help="The location to lookup."
    )
    PARSER.add_argument(
        "-unit",
        default="c",
        choices=["c","f"],
        help="Units C or F."
    )
    PARSER.add_argument(
        "-f",
        "--forecast",
        default=False,
        action="store_true",
        help="Pass this argument to get a weather forecast."
    )
    PARSER.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        help="Start Day."
    )
    PARSER.add_argument(
        "-e",
        "--end",
        type=int,
        default=3,
        help="End Day."
    )
    ARGS = PARSER.parse_args()
    weather = Weather(ARGS.unit)
    loc = weather.lookup_by_location(ARGS.location)
    condition = loc.condition
    print("%s, %s" % (loc.location.city, loc.location.country))
    print("%s" % (condition.date))
    print("----------------------------------------------")
    print("Now:{:^19} {} | {} Deg C".format(condition.text, condition.code, condition.temp))
    print("----------------------------------------------")
    print("")
    print("----------------------------------------------")
    print("--------------- 7 DAY OUTLOOK ----------------")
    print("----------------------------------------------")
    print("CHILL: %s, DIR: %s, SPEED: %s" % (loc.wind.chill, loc.wind.direction, loc.wind.speed))
    print("%s" % (loc.astronomy))
    print("%s" % (loc.atmosphere))

    if ARGS.forecast:
        loc = weather.lookup_by_location(ARGS.location)
        condition = loc.condition
        start = 0 if not ARGS.start else ARGS.start # If the start argument isn't set, set the start as the first element in the forecast array.
        end =  len(loc.forecast) if not ARGS.end else ARGS.end # if the end argument isn't set, set the end as the last element in the forecast array.
        for forecast in loc.forecast[start:end]:
            print("{}: {:^18} {} | High: {} | Low: {}".format(forecast.day, forecast.text, forecast.code, forecast.high, forecast.low))
            start += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

