from Interface.member_repository import MemberRepository 
from domain.member import Member 

class MemberRepositoryMySQL(MemberRepository):
    def __init__(self):
        self._members = {} #Placeholder 
        
    def get_by_id(self, member_id):
        return self._members.get(member_id)
        
        