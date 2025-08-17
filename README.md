# Student-Management-System
This is a simple command-line student management system built with Python and MySQL. It allows administrators to manage students, departments, and courses in an educational institution. The application is still under development and currently supports basic CRUD (Create, Read, Update, Delete) operations.

## Features
- **Departments Management**: Add, view, update, delete, and search departments.
- **Students Management**: Add, view, update, delete, and search students, including validation for names, emails, and phone numbers.
- **Courses Management**: Add, view, update, delete, and search courses, with associations to departments.
- **Database auto-creation**: If the database doesn't exist, it will be created automatically along with the required tables from schema.sql.
- Error handling for common database issues like duplicate entries or invalid foreign keys.
- Timestamps for creation and updates on records.

### Future enhancements may include:
- Instructor management.
- Enrollment and teaching assignments.
- Grade management.
- More advanced queries and reporting.

## Prerequisites
- Python 3.6+ (tested with Python 3.12.3, but compatible with earlier versions).
- MySQL Server (e.g., via XAMPP, MAMP, or standalone installation).
- Required Python library: `mysql-connector-python` (install via `pip install mysql-connector-python`).

**Note**: Ensure your MySQL server is running before launching the application. The default connection uses:
- Host: `localhost`
- User: `root`
- Password: `""` (empty; update in `database.py` if needed).

## Installation
1. Clone the repository:
``` bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```
2. Install the required Python library:
``` bash
pip install mysql-connector-python
```
4. Start your MySQL server.
5. Run the application:`python main.py`
The database (`Student_Management_System`) and tables will be created automatically if they don't exist.

## Usage
Upon running `main.py`, you'll see a CLI menu:
```
Welcome to student manager
There are the categories we have
1: Students
2: Departments
3: Courses
0: Exit
```
- Select a category (e.g., "1" for Students).
- Sub-menus allow operations like adding, updating, etc.
- Input validation is handled for most fields (e.g., emails must match a valid pattern, phones must be 11 digits).

Example: Adding a student
- Choose "1: Students" > "2: Add a student".
- Enter details as prompted (e.g., name, email, phone, address, department number).
- Handles errors like duplicate emails/phones or non-existent departments.

## Database Setup
- The schema is defined in `schema.sql` and imported automatically.
- Tables include:
  - `departments`: Department details (auto-increment from 10).
  - `students`: Student info with foreign key to departments (auto-increment from 1000).
  - `courses`: Course details with foreign key to departments (auto-increment from 1).
  - `enrollments`: Student-course enrollments.
  - `instructors`: Instructor details (auto-increment from 100, under development).
  - `teaching`: Instructor-course assignments (under development).
- Foreign keys use `RESTRICT` on delete to prevent orphaned records.
  
## Folder Structure
```
student-management-system/
├── Entities/             # Entity classes for database operations
│   ├── init.py       # (Optional, for package)
│   ├── entity.py         # Base class for sharing DB connection
│   ├── departments.py    # Department CRUD operations
│   ├── students.py       # Student CRUD operations
│   └── courses.py        # Course CRUD operations
├── database.py           # Database connection and creation logic
├── schema.sql            # SQL schema for tables
├── validation.py         # Input validation and error handling functions
├── main.py               # Entry point with CLI menu
├── README.md             # This file
```
# Contributing
This project is open for contributions! Feel free to:
- Fork the repo.
- Create a feature branch.
- Submit a pull request.

Issues and suggestions are welcome via GitHub Issues.
