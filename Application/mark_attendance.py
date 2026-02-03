from datetime import date 
from domain.attendance import Attendance
from Interface.member_repository import MemberRepository 
from Interface.attendance_repository import AttendanceRepository 


class MarkAttendance: 
    def __init__(
        self, 
        member_repo: MemberRepository, 
        attendance_repo: AttendanceRepository
    ):
        self.member_repo = member_repo 
        self.attendance_repo = attendance_repo 
        
    def check_member(self, member_id: int):
        member = self.member_repo.get_active_member_by_id(member_id)
        
        if not member:
            raise PermissionError("Access denied: not an active member")
        
        attendance = Attendance(member_id, date.today()) 
        self.attendance_repo.save(attendance)
        
        return attendance