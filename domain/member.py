from datetime import date

class Member: 
    def __init__(self,id,name,is_member):
        self.id = id
        self.name = name 
        self.is_member = is_member
    
    def is_membership_active(self) -> bool:
        return self.is_member 