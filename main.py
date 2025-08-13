import mysql.connector


class Database:
    def connect(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Student_Management_System",
        )
        return conn


class Entity:
    db = None


# Removed the constructor to work with the parent one and changed every self.conn to self.db
class Department(Entity):
    # def __init__(self, db):
    #     self.conn = db.connect()

    def add_department(self, name):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO departments(Name) VALUES (%s)", (name,))
        self.db.commit()
        cursor.close()
        print(f"{name} department was added successfuly")

    def show_departments(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT Dno, Name FROM departments")
        for row in cursor:
            print(f"Department no.: {row['Dno']} \nName: {row['Name']}")
            print("-----------------------------")
        cursor.close()

    def update_department(self, dno):
        cursor = self.db.cursor()
        print("Updating on department", dno)
        newName = input("Enter the new name: ")
        cursor.execute(
            "Update departments SET Name = %s where Dno = %s ", (newName, dno)
        )
        self.db.commit()
        cursor.close()
        print("Department Updated Successfuly")

    def delete_departments(self, dno):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM departments WHERE Dno = %s", (dno,))
        self.db.commit()
        print("Department deleted successfully")
        cursor.close()

    def search_department(self, dno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments where Dno = %s", (dno,))
        row = cursor.fetchone()
        print(f"Name: {row['Name']} ")
        print(f"Created at: {row['Created_at']} ")
        print(f"Updated at: {row['Updated_at']} ")


class Student(Entity):
    def add_student(self, fname, maname, lname, email, phone, address, dno):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO students(FName, Mname, Lname, Email, Phone, Address, Dno) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (fname, maname, lname, email, phone, address, dno),
        )
        self.db.commit()
        cursor.close()
        print(f"{fname} {lname} department was added successfuly")

    def show_students(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(
            "SELECT s.*, d.Name AS DName FROM students AS s LEFT JOIN departments AS d ON s.Dno = d.Dno"
        )
        print("Here are all the students:")
        for row in cursor:
            print(f"Id: {row['Sid']}")
            print(f"Name: {row['Fname']} {row['Mname']} {row['Lname']}")
            print(f"Email: {row['Email']}")
            print(f"Phone: {row['Phone']}")
            print(f"Address: {row['Address']}")
            print(f"Department: {row['DName']}")
            print("-----------------------------")
        cursor.close

    def update_student(self, id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students where Sid = %s", (id,))
        student = cursor.fetchone()
        if not student:
            print(f"Can't find a student with id {id}")
            return
        print(
            f"Updating on the student {student['Fname']} {student['Mname']} {student['Lname']}"
        )
        # cursor.close()
        while True:
            print("please choose what to edit")
            print("1: Name")
            print("2: Email")
            print("3: Phone")
            print("4: Address")
            print("5: Department")
            print("0: Done")
            choice = input(
                "Enter the value corresponding to the field you want to change: "
            )
            if choice == "1":
                new = input("Please enter the full name of the student: ")
                new = new.split(" ")
                cursor.execute(
                    "UPDATE students SET Fname = %s, Mname = %s, Lname = %s where Sid = %s",
                    (new[0], new[1], new[2], id),
                )
                self.db.commit()
            elif choice == "2":
                new = input("Enter the new email: ")
                cursor.execute(
                    "UPDATE students SET Email = %s where Sid = %s ", (new, id)
                )
                self.db.commit()
            elif choice == "3":
                new = input("Enter the new phone: ")
                cursor.execute(
                    "UPDATE students SET Phone = %s where Sid = %s ", (new, id)
                )
                self.db.commit()
            elif choice == "4":
                new = input("Enter the new address: ")
                cursor.execute(
                    "UPDATE students SET Address = %s where Sid = %s ", (new, id)
                )
                self.db.commit()
            elif choice == "5":
                new = input("Enter the new department of the student: ")
                cursor.execute(
                    "UPDATE students SET Dno = %s where Sid = %s ", (new, id)
                )
                self.db.commit()
            elif choice == "0":
                break
            else:
                print("Please enter a valid input \n")
            print("Updated Successfuly")
            print("-----------------------------")

    def delete_student(self, id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students where Sid = %s", (id,))
        student = cursor.fetchone()
        if not student:
            print(f"Can't find a student with id {id}")
            return
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM students WHERE Sid = %s", (id,))
        self.db.commit()
        print(f"Student {student['Fname']} deleted successfully")
        cursor.close()

    def search_student(self, id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students where Sid = %s", (id,))
        row = cursor.fetchone()
        if not row:
            print(f"Can't find a student with id {id}")
            return
        print(f"Name: {row['Fname']} {row['Mname']} {row['Lname']}")
        print(f"Email: {row['Email']} ")
        print(f"Phone: {row['Phone']} ")
        print(f"Address: {row['Address']} ")
        print(f"Department: {row['Dno']} ")
        print(f"Created at: {row['Created_at']} ")
        print(f"Updated at: {row['Updated_at']} ")


db = Database().connect()
Entity.db = db
departments = Department()
# departments.add_department("Physics")
# departments.show_departments()
# departments.update_department(11)
# departments.delete_departments(10)
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
# students.delete_student(1009)
students.search_student(1002)
