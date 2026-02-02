# Attendance-system
A small project I'll be working on together with my union group. 

Designed and implemented a membership and attendance system using Clean Architecture principles. 
Focused on domain-driven design, business rules enforcement, and layered architecture in Python.


The application is using clean architecture.

attendance_app/
│
├── domain/
│   ├── entities/
│   │   ├── member.py
│   │   └── attendance.py
│   └── value_objects/
│       └── membership_status.py
│
├── use_cases/
│   ├── mark_attendance.py
│   ├── register_member.py
│   └── pay_membership_fee.py
│
├── interfaces/
│   └── repositories/
│       ├── member_repository.py
│       └── attendance_repository.py
│
├── infrastructure/
│   └── mysql/
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
