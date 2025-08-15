from entity import Entity


class Course(Entity):
    def add_course(self, name, capacity, dno):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO courses(Name, Capacity, Dno) VALUES (%s, %s, %s)",
            (name, capacity, dno),
        )
        self.db.commit()
        cursor.close()
        print(f"{name} course was added successfuly")

    def show_courses(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(
            "SELECT c.*, d.Name AS DName FROM courses AS c LEFT JOIN departments AS d ON c.Dno = d.Dno"
        )
        print("Here are all the courses:")
        for row in cursor:
            print(f"Id: {row['Cno']}")
            print(f"Name: {row['Name']}")
            print(f"Capacity: {row['Capacity']}")
            print(f"Department: {row['DName']}")
            print("-----------------------------")
        cursor.close()

    def update_course(self, cno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses where Cno = %s", (cno,))
        course = cursor.fetchone()
        if not course:
            print(f"Can't find a course with number {cno}")
            return
        print(f"Updating on the course {course['Name']}")
        while True:
            print("please choose what to edit")
            print("1: Name")
            print("2: Capacity")
            print("3: Department")
            print("0: Done")
            choice = input(
                "Enter the value corresponding to the field you want to change: "
            )
            if choice == "1":
                new = input("Please enter the name of the course: ")
                cursor.execute(
                    "UPDATE courses SET Name = %s where Cno = %s",
                    (new, cno),
                )
                self.db.commit()
            elif choice == "2":
                new = input("Enter the new capacity: ")
                cursor.execute(
                    "UPDATE courses SET capacity = %s where Cno = %s ", (new, cno)
                )
                self.db.commit()
            elif choice == "3":
                new = input("Enter the new department Id for the course: ")
                cursor.execute(
                    "UPDATE courses SET Dno = %s where Cno = %s ", (new, cno)
                )
                self.db.commit()
            elif choice == "0":
                break
            else:
                print("Please enter a valid input \n")
            print("Updated Successfuly")
            print("-----------------------------")
        cursor.close()

    def delete_course(self, cno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses where Cno = %s", (cno,))
        course = cursor.fetchone()
        if not course:
            print(f"Can't find a course with number {cno}")
            return
        cursor.execute("DELETE FROM courses WHERE Cno = %s", (cno,))
        self.db.commit()
        print(f"course {course['Name']} deleted successfully")
        cursor.close()

    def search_course(self, cno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses where Cno = %s", (cno,))
        row = cursor.fetchone()
        if not row:
            print(f"Can't find a course with number {cno}")
            return
        print(f"Course name: {row['Name']}")
        print(f"Department: {row['Dno']} ")
        print(f"Created at: {row['Created_at']} ")
        print(f"Updated at: {row['Updated_at']} ")
        cursor.close()
