import mysql.connector
from entity import Entity
from departments import Department
from students import Student
from courses import Course


class Database:
    def connect(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Student_Management_System",
        )
        return conn


db = Database().connect()
Entity.db = db


departments = Department()
# departments.add_department("Physics")
# departments.show_departments()
# departments.update_department(11)
# departments.delete_departments(1000)
# departments.search_department(11)


students = Student()
# students.add_student(
#     "Youssif",
#     "Ahmed",
#     "Abdallah",
#     "yoossifahmed66@gmail.com",
#     "01143095568",
#     "Giza",
#     11,
# )

# students.show_students()
# students.update_student(1008)
# students.delete_student(1002)
# students.search_student(1002)


course = Course()
# course.add_course("Abstract Algebra", 100, 11)
# course.show_courses()
# course.update_course(2)
# course.delete_course(2)
course.search_course(3)
