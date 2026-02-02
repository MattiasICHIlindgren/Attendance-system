from abc import ABC, abstractmethod 

class MemberRepository(ABC): 
    @abstractmethod
    def get_by_id(self,member_id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass 
    
    @abstractmethod
    def get_active_member_by_id(self,member_id):
        pass