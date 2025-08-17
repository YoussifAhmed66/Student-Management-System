import mysql.connector
from mysql.connector import errorcode  # shortcut for error handeling module

# importing entity classes
from database import Database
from Entities.entity import Entity
from Entities.departments import Department
from Entities.students import Student
from Entities.courses import Course
import validation


# Main

# creating the database connection abject and passing it to the parent entity class
db = Database().connect()
Entity.db = db

# A simple CLI to navigate through methods
# When the user choose a category an instance of the coresponding class is created to manage it
print("Welcome to student manager")
print("==========================================")
while True:
    print("There are the categories we have")
    print("1: Students")
    print("2: departments")
    print("3: Courses")
    print("0: Exit")
    choice = input("Enter the number of the category you want to manage: ")
    print("==========================================\n")
    if choice == "1":
        # creating an instance from Student class and show the options for it
        students = Student()
        while True:
            print("Please choose what you want")
            print("1: Show all students")
            print("2: Add a student")
            print("3: Update a student")
            print("4: Delete a student")
            print("5: Search for a student")
            print("0: Back")
            sub_choice = input("Enter what you want to do: ")
            if sub_choice == "1":
                students.show_students()

            elif sub_choice == "2":
                # inserting the student data using the validation functions from the validation module
                print("\nInserting new student")
                fname = validation.validate_name("Enter the first name: ")
                mname = validation.validate_name("Enter the middle name: ")
                lname = validation.validate_name("Enter the last name: ")
                email = validation.validate_email("Enter the email of the student: ")
                phone = validation.validate_phone(
                    "Enter the phone number of the student: "
                )
                address = input("Enter the address of the student: ")
                dno = input("Enter the department number of the student: ")

                # Adding the data in student table while checking if the eamail or phone are duplicated in the students table and if the department no doesn't exist to avoid errors
                try:
                    students.add_student(
                        fname, mname, lname, email, phone, address, dno
                    )
                except mysql.connector.Error as error:
                    validation.handle_db_error(error)

            elif sub_choice == "3":
                id = validation.validate_integer(
                    "Enter the id of the student you wnat to update: "
                )
                try:
                    students.update_student(id)
                except mysql.connector.Error as error:
                    validation.handle_db_error(error)

            elif sub_choice == "4":
                id = validation.validate_integer(
                    "Enter the id of the student you wnat to delete: "
                )
                students.delete_student(id)

            elif sub_choice == "5":
                id = validation.validate_integer(
                    "Enter the id of the student you wnat to search for: "
                )
                students.search_student(id)

            elif sub_choice == "0":
                break
            else:
                print("Please enter a valid input")
            print("-----------------------------------\n")

    elif choice == "2":
        # creating an instance from department class and show the options for it
        departments = Department()
        while True:
            print("Please choose what you want")
            print("1: Show all departments")
            print("2: Add a department")
            print("3: Update a department")
            print("4: Delete a department")
            print("5: Search for a department")
            print("0: Back")
            sub_choice = input("Enter what you want to do: ")
            if sub_choice == "1":
                departments.show_departments()

            elif sub_choice == "2":
                print("\nInserting new department")
                name = validation.validate_name("Enter the name of the department: ")
                try:
                    departments.add_department(name)
                except mysql.connector.Error as error:
                    validation.handle_db_error(error)

            elif sub_choice == "3":
                id = validation.validate_integer(
                    "Enter the number of the department to update: "
                )
                try:
                    departments.update_department(id)
                except mysql.connector.Error as error:
                    validation.handle_db_error(error)

            elif sub_choice == "4":
                id = validation.validate_integer(
                    "Enter the department number you want to delete: "
                )
                departments.delete_department(id)

            elif sub_choice == "5":
                id = validation.validate_integer(
                    "Enter the department number you want to search for: "
                )
                departments.search_department(id)

            elif sub_choice == "0":
                break
            else:
                print("Please enter a valid input")
            print("-----------------------------------\n")

    elif choice == "3":
        courses = Course()
        while True:
            print("Please choose what you want")
            print("1: Show all courses")
            print("2: Add a course")
            print("3: Update a course")
            print("4: Delete a course")
            print("5: Search for a course")
            print("0: Back")
            sub_choice = input("Enter what you want to do: ")
            if sub_choice == "1":
                courses.show_courses()

            elif sub_choice == "2":
                print("\nInserting new course")
                # the course name doesn't apply normal validation because some names may contain numbers or special characters
                name = input("Enter the name of the course: ")
                capacity = validation.validate_integer(
                    "Enter the capacity of the course: "
                )
                dno = input(
                    "Enter the number of the department which is responsible for this course: "
                )

                try:
                    courses.add_course(name, capacity, dno)
                except mysql.connector.Error as error:
                    validation.handle_db_error(error)

            elif sub_choice == "3":
                id = validation.validate_integer(
                    "Enter the number of the course you want to update: "
                )
                try:
                    courses.update_course(id)
                except mysql.connector.Error as error:
                    validation.handle_db_error(error)

            elif sub_choice == "4":
                id = validation.validate_integer(
                    "enter the number of the course you want to delete: "
                )
                courses.delete_course(id)

            elif sub_choice == "5":
                id = validation.validate_integer(
                    "enter the number of the course you want to search for: "
                )
                courses.search_course(id)

            elif sub_choice == "0":
                break
            else:
                print("Please enter a valid input")
            print("-----------------------------------\n")

    elif choice == "0":
        print("Thank you, good bye")
        break
    else:
        print("Please enter a valid input")

    print("==========================================\n")
