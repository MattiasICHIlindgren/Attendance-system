from Interface.member_repository import MemberRepository

class MembershipFee: 
    def __init__(self, member_repo: MemberRepository):
        self.member_repo = member_repo
        
        
    def fetch_member(self, member_id: int):
        member = self.member_repo.get_by_id(member_id)
        
        if not member:
            return ValueError("Member not found")
        
        member.is_member = True
        self.member_repo.save_member(member) 
        
            