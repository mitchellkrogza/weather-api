class Location(object):
    def __init__(self, location_data):
        self._location_data = location_data

    def city(self):
        return self._location_data['city']

    def country(self):
        return self._location_data['country']
        
    def region(self):
        return self._location_data['region']
    
        
