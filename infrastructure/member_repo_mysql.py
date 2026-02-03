from Interface.member_repository import MemberRepository 
from domain.member import Member 

class MemberRepositoryMySQL(MemberRepository):
    def __init__(self):
        self._members = {} #Placeholder 
        
        