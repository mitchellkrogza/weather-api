from argparse import ArgumentParser
from .weather import Weather
import sys


def main():
    pa = ArgumentParser()
    pa.add_argument('location', help='The location to lookup.')
    pa.add_argument('--unit', default='c', nargs='?', choices=['c', 'f'])
    pa.add_argument("--f"', "--forecast", nargs="?", "Pass this argument to get a weather forecast")
    pa.add_argument("--s"', "--start", nargs="?", "The forecast start")
    pa.add_argument("--e"', "--end", nargs="?", "The forecast end")
    args = pa.parse_args()
    weather = Weather(args.unit)
    loc = weather.lookup_by_location(args.location)
    condition = loc.condition
    print("Weather report for %s, %s" % (loc.location.city, loc.location.country))
    print("Condition: %s " % condition.text)
    print("Temperature: %s" % condition.temp)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

		
if args.forecast:
   start = 0 if not args.start else args.start # If the start argument isn't set, set the start as the first element in the forecast array.
   end =  len(location.forecast) if not args.end else args.end # if the end argument isn't set, set the end as the last element in the forecast array.
   for forecast in location.forecast[start:end]:
       print("Day%s: %s" % (start, forecast.text))
       start += 1