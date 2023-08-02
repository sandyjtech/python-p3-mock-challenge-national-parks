
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
        
        
    
