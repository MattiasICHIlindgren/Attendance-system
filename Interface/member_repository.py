from abc import ABC, abstractmethod 
from domain.member import Member

class MemberRepository(ABC): 
    
    @abstractmethod
    def get_by_id(self, member_id: int) -> Member | None:
        pass
    
    @abstractmethod
    def get_all(self) -> list[Member]:
        pass 
    
    @abstractmethod
    def get_active_member_by_id(self, member_id: int) -> Member | None:
        pass
    
    @abstractmethod
    def save_member(self, member: Member) -> None:
        pass 