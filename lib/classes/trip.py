
class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
        
    @property
    def start_date(self):
        return self._start_date
    
    @property 
    def end_date(self):
        return self._end_date
    
    @property
    def visitor(self):
        return self._visitor
    
    @property
    def national_park(self):
        return self._national_park
    
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str):
            self._start_date = value
        else:
            raise Exception
        
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str):
            self._end_date = value
        else:
            raise Exception
        
    @visitor.setter
    def visitor(self, value):
        from classes.visitor import Visitor
        if isinstance(value, Visitor):
            self._visitor = value
        else:
            raise Exception
        
    @national_park.setter
    def national_park(self, value):
        from classes.national_park import NationalPark
        if isinstance(value, NationalPark):
            self._national_park = value
        else:
            raise Exception
        
    def __repr__(self):
        return f"<Trip: {self.start_date}, {self.end_date}>" 
