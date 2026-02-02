from abc import ABC, abstractmethod 
from datetime import date

class AttendanceRepository(ABC):
    @abstractmethod
    def mark(self,member_id,attendance_date: date):
        pass 
    
    @abstractmethod
    def get_dates_for_member(self,member_id):
        pass 
