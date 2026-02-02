class Attendance: 
    def __init__(self):
        self.records = {}
    
    def mark(self,name,date):
        self.records.setdefault(name, []).append(date)
    
    def unmark(self,name,date): 
        pass 
    
    def is_present(self,name,date):
        pass 