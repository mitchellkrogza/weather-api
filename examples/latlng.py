from weather import Weather, Unit

w = Weather(Unit.CELSIUS)
lookup = w.lookup_by_latlng(53.3494, -6.2601)
condition = lookup.condition
print(condition.text)
