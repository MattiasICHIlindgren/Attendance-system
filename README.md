# Attendance-system
A small project I'll be working on together with my union group. 
This application will feature a toggle like attendance system to keep track of memberships for the members in our union group

The goal of this application is to mark attendances of the members and keep track of their membership : if the membership fee has been paid etc 
The data will be storedin a simple mySQL database. 


The application is using clean architecture.

attendance_app/
│
├── domain/
│   ├── entities/
│   │   ├── member.py
│   │   └── attendance.py               *Entity
│   │
│   └── value_objects/
│       └── membership_status.py
│
├── use_cases/
│   ├── mark_attendance.py
│   ├── register_member.py              *Business logic 
│   └── pay_membership_fee.py
│
├── interfaces/
│   └── repositories/
│       ├── member_repository.py        
│       └── attendance_repository.py
│
├── infrastructure/
│   └── mysql/                          
│       ├── member_repo_mysql.py        *Data Storage 
│       └── attendance_repo_mysql.py
│
├── web/
│   ├── app.py                          *Flask app
│   └── templates/
│       └── index.html
│
└── config/
│    └── database.py
│
└── main.py 