from argparse import ArgumentParser
from .weather import Weather
import sys


def main():
    pa = ArgumentParser()
    pa.add_argument('location', help='The location to lookup.')
    pa.add_argument('--unit', default='c', nargs='?', choices=['c', 'f'])
    pa.add_argument('--f', '--forecast', nargs='?', help='Pass this argument to get a weather forecast', action="store_true")
    pa.add_argument('--s', '--start', default='1', nargs='?', help='Start Day')
    pa.add_argument('--e', '--end', default='3', nargs='?', help='End Day')
    args = pa.parse_args()
    weather = Weather(args.unit)
    loc = weather.lookup_by_location(args.location)
    condition = loc.condition
    print("Weather report for %s, %s" % (loc.location.city, loc.location.country))
    print("Condition: %s " % condition.text)
    print("Temperature: %s" % condition.temp)
if args.forecast:
   start = 0 if not args.start else args.start # If the start argument isn't set, set the start as the first element in the forecast array.
   end =  len(location.forecast) if not args.end else args.end # if the end argument isn't set, set the end as the last element in the forecast array.
   for forecast in location.forecast[start:end]:
       print("Day%s: %s" % (start, forecast.text))
       start += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

		
