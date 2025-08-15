from entity import Entity


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
        print("Here are all the departments: ")
        for row in cursor:
            print(f"Department no.: {row['Dno']} \nName: {row['Name']}")
            print("-----------------------------")
        cursor.close()

    def update_department(self, dno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments where Dno = %s", (dno,))
        course = cursor.fetchone()
        if not course:
            print(f"Can't find a departments with id {dno}")
            return
        print("Updating on department", dno)
        newName = input("Enter the new name: ")
        cursor.execute(
            "Update departments SET Name = %s where Dno = %s ", (newName, dno)
        )
        self.db.commit()
        cursor.close()
        print("Department Updated Successfuly")

    def delete_departments(self, dno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments where Dno = %s", (dno,))
        course = cursor.fetchone()
        if not course:
            print(f"Can't find a departments with id {dno}")
            return
        cursor.execute("DELETE FROM departments WHERE Dno = %s", (dno,))
        self.db.commit()
        print("Department deleted successfully")
        cursor.close()

    def search_department(self, dno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments where Dno = %s", (dno,))
        row = cursor.fetchone()
        if not row:
            print(f"Can't find a department with id {dno}")
        print(f"Name: {row['Name']} ")
        print(f"Created at: {row['Created_at']} ")
        print(f"Updated at: {row['Updated_at']} ")
        cursor.close()
