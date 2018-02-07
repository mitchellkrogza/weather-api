from argparse import ArgumentParser
from .weather import Weather

def main():
    pa = ArgumentParser()
    pa.add_argument('location', help='The location to lookup.')
    args = pa.parse_args()
    weather = Weather()
    location = weather.lookup_by_location(args.location)
    condition = location.condition()
    print(condition.text())
        


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)