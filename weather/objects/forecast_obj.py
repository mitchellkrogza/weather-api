class Forecast(object):
    def __init__(self, forecast_data):
        self._forecast_data = forecast_data

    @property
    def text(self):
        return self._forecast_data['text']

    @property
    def date(self):
        return self._forecast_data['date']

    @property
    def high(self):
        return self._forecast_data['high']

    @property
    def low(self):
        return self._forecast_data['low']