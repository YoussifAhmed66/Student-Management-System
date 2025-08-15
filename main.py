import mysql.connector
from mysql.connector import errorcode  # shortcut for error handeling module

# importing entity classes
from entity import Entity
from departments import Department
from students import Student
from courses import Course


# This is the database cennection class which connects to the database if exists and if not it creates a new one and import it's structure from schema.sql
# Then it return a connection object
class Database:
    def connect(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Student_Management_System",
            )
            return conn
        # if the connection to the database failed because of unkown database it creates a new database but if it was for any other reason like username, password, etc... it raises the error
        except mysql.connector.Error as error:
            if (
                error.errno == errorcode.ER_BAD_DB_ERROR
            ):  # constant value with integer error number for unkown database: 1049
                print("Creating Database")
                self.create_database()
                self.import_schema()
                return self.connect()  # connect aain after the database was created
            else:
                raise  # more error handeling will be added soon

    # A Method to create a new database
    def create_database(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="")
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE Student_Management_System")
        print("Database Student_Management_System created successfuly")
        cursor.close()
        conn.close()

    # A method to import the tables structure to the new database created
    def import_schema(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Student_Management_System",
        )
        cursor = conn.cursor()
        # it reads schema.sql file then execute each statement individually by splitting them at ';' and looping through them
        with open("schema.sql", "r") as file:
            schema = file.read()

        for statement in schema.split(";"):
            cursor.execute(statement.strip())
        conn.commit()
        cursor.close()


# Main

# creating the database connection abject and passing it to the parent entity class
db = Database().connect()
Entity.db = db

# Just testing the methods of the classes

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
