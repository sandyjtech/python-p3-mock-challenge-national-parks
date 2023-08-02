from classes.trip import Trip


class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

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
        #if start is passed today?
        return len(self.trips())

    def best_visitor(self):
        all_visitors = [trip.visitor for trip in self.trips()]
        visitor_counts = {}  

        
        for visitor in all_visitors:
            visitor_counts[visitor] = visitor_counts.get(visitor, 0) + 1

        best_visitor = None
        max_visits = 0

        for visitor, count in visitor_counts.items():
            if count > max_visits:
                best_visitor = visitor
                max_visits = count

        return best_visitor
                  
    @classmethod
    def most_visited(cls):
        return max(cls.all, key=lambda national_park: national_park.total_visits())


    def __repr__(self):
        return f"<Park: {self.name}>" 