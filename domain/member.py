from datetime import date

class Member: 
    def __init__(self,member_id: int,name: str,is_member: bool):
        self.member_id = member_id
        self.name = name 
        self.is_member = is_member
    
    def is_membership_active(self) -> bool:
        return self.is_member 