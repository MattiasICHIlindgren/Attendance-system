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