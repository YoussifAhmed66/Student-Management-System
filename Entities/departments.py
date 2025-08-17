from entity import Entity
import validation


# Removed the constructor to work with the parent attribute and changed every self.conn to self.db
class Department(Entity):
    # def __init__(self, db):
    #     self.conn = db.connect()

    def add_department(self, name):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO departments(Name) VALUES (%s)", (name,))
        self.db.commit()
        cursor.close()
        print(f"\n{name} department was added successfuly\n")

    def show_departments(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT Dno, Name FROM departments")
        print("\nHere are all the departments: ")
        for row in cursor:
            print("-----------------------------")
            print(f"Department no.: {row['Dno']} \nName: {row['Name']}")
        cursor.close()

    def update_department(self, dno):
        # Search first on the id, if not found return and the same goes for delete and search
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments where Dno = %s", (dno,))
        row = cursor.fetchone()
        if not row:
            print(f"Can't find a departments with id {dno}")
            return

        print(f"Updating on {row['Name']} department: {dno}")
        newName = validation.validate_name("Enter the new name: ")
        cursor.execute(
            "Update departments SET Name = %s where Dno = %s ", (newName, dno)
        )
        self.db.commit()
        cursor.close()
        print("Department Updated Successfuly")

    def delete_department(self, dno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments where Dno = %s", (dno,))
        row = cursor.fetchone()
        if not row:
            print(f"Can't find a departments with id {dno}")
            return

        cursor.execute("DELETE FROM departments WHERE Dno = %s", (dno,))
        self.db.commit()
        print(f"Department {row['Name']} deleted successfully")
        cursor.close()

    def search_department(self, dno):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments where Dno = %s", (dno,))
        row = cursor.fetchone()
        if not row:
            print(f"Can't find a department with id {dno}")
            return
        print("")
        print(f"Name: {row['Name']} ")
        print(f"Created at: {row['Created_at']} ")
        print(f"Updated at: {row['Updated_at']} ")
        cursor.close()
