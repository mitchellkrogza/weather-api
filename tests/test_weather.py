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
        self.assertTrue(len(forecasts) > 0)
        first = forecasts[0]
        self.assertTrue(hasattr(first, 'text'))
        self.assertTrue(hasattr(first, 'high'))
        self.assertTrue(hasattr(first, 'low'))
        self.assertTrue(hasattr(first, 'date'))
