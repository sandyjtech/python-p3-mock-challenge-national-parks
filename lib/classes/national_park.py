from classes.trip import Trip


class NationalPark:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, 'name'):
             self._name = value
        else:
            raise Exception
    
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return [*set([trip.visitor for trip in self.trips()])]

    def total_visits(self):
        pass

    def best_visitor(self):
        pass

    @classmethod
    def most_visited(cls):
        pass

    def __repr__(self):
        return f"<Park: {self.name}>" 