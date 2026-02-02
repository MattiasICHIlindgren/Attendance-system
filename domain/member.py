from datetime import date

class Member: 
    def __init__(self,id,name,membership_expires_at):
        self.id = id
        self.name = name 
        self.membership_expires_at = membership_expires_at
    
    def is_membership_active(self):
        return self.membership_expires_at >= date.today()