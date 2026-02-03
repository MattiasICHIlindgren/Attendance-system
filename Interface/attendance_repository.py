from abc import ABC, abstractmethod 
from domain.attendance import Attendance

class AttendanceRepository(ABC):
    @abstractmethod
    def save(self,attendace: Attendance) -> None:
        pass 
    
    @abstractmethod
    def get_by_member_id(self,member_id: int) -> list[Attendance]:
        pass 
