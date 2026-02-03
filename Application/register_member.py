from domain.member import Member 
from Interface.member_repository import MemberRepository 

class RegisterMember:
    def __init__(self, member_repo: MemberRepository):
        self.member_repo = member_repo 
        
    def execute(self ,member_id: int, name: str ):
        member = Member(member_id, name , is_member= True)
        self.member_repo.save_member(member)
        return member     
        
        
        
    
    