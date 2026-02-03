# Attendance-system
A small project I'll be working on together with my union group. 

Designed and implemented a membership/attendance system using Clean Architecture principles. 
Focused on domain-driven design, business rules enforcement, and layered architecture in Python.


The application is using clean architecture.

attendance_app/
│
├── domain/   
│       ├── member.py                           *entities
│       └── attendance.py
│
├── use_cases/
│   ├── mark_attendance.py                      *Application
│   ├── register_member.py
│   └── pay_membership_fee.py
│
├── interfaces/                                 *repositories
│       ├── member_repository.py
│       └── attendance_repository.py
│
├── infrastructure/                             *data storage  
│       ├── member_repo_mysql.py
│       └── attendance_repo_mysql.py
│
├── web/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── config/
│   └── database.py
│
└── main.py
