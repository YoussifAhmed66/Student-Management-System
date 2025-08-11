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


class Department:
    def __init__(self, db):
        self.conn = db.connect()

    def add_department(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO departments(Name) VALUES (%s)", (name,))
        self.conn.commit()
        cursor.close()
        print(f"{name} department was added successfuly")

    def show_departments(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT Dno, Name FROM departments")
        for row in cursor:
            print(f"Department no.: {row['Dno']} \nName: {row['Name']}")
            print("-----------------------------")
        cursor.close()

    def update_department(self, dno):
        cursor = self.conn.cursor()
        print("Updating on department", dno)
        newName = input("Enter the new name: ")
        cursor.execute(
            "Update departments SET Name = %s where Dno = %s ", (newName, dno)
        )
        self.conn.commit()
        cursor.close()

    def delete_departments(self, dno):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM departments WHERE Dno = %s", (dno,))
        self.conn.commit()
        print("Department deleted successfully")
        cursor.close()

    def search_department(self, dno):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departments where Dno = %s", (dno,))
        row = cursor.fetchone()
        print(f"Name: {row['Name']} ")
        print(f"Created at: {row['Created_at']} ")
        print(f"Updated at: {row['Updated_at']} ")


db = Database()
departments = Department(db)
# departments.add_department("Physics")
# departments.show_departments()
departments.update_department(11)
# departments.delete_departments(10)
# departments.search_department(11)
