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
        pass

    def visitors(self):
        pass

    def total_visits(self):
        pass

    def best_visitor(self):
        pass

    @classmethod
    def most_visited(cls):
        pass
