import unittest
from weather import Weather


class WeatherTests(unittest.TestCase):
    def test_lookup(self):
        w = Weather()
        data = w.lookup(woeid=560743)
        self.assertTrue('Dublin' in data.description())

    def test_search(self):
        w = Weather()
        data = w.lookup_by_location('Dublin')
        self.assertTrue('Dublin' in data.description())

    def test_forecast(self):
        w = Weather()
        location = w.lookup_by_location('Dublin')
        forecasts = location.forecast()
        assert len(forecasts) > 0
        for forecasts in location.forecast():
            print(forecasts.text())
            print(forecasts.date())
            print(forecasts.high())
            print(forecasts.low())
