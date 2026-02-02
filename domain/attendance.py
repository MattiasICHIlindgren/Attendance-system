class Attendance: 
    def __init__(self):
        self.records = {}
    
    def mark(self,name,date):
        self.records.setdefault(name, []).append(date)
    
    def unmark(self,name,date): 
        if name in self.records and date in self.records[name]: 
            self.records[name].remove(date)
    
    def is_present(self,name,date):
        pass 