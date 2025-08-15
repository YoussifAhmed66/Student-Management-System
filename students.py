from entity import Entity


class Student(Entity):
    def add_student(self, fname, maname, lname, email, phone, address, dno):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO students(FName, Mname, Lname, Email, Phone, Address, Dno) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (fname, maname, lname, email, phone, address, dno),
        )
        self.db.commit()
        cursor.close()
        print(f"Student {fname} {lname} was added successfuly")

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
        cursor.close()

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
                new = input("Enter the new department Id of the student: ")
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
        cursor.close()

    def delete_student(self, id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students where Sid = %s", (id,))
        student = cursor.fetchone()
        if not student:
            print(f"Can't find a student with id {id}")
            return
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
        cursor.close()
