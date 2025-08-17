import re
import mysql.connector
from mysql.connector import errorcode


def validate_integer(msg):
    while True:
        n = input(msg).strip()
        if not n.isdigit():
            print("Please enter an integer value")
            continue
        return n


def validate_name(msg):
    while True:
        name = input(msg).strip()
        if not name.isalpha():
            print("Name should be only text A-Z,a-z ")
            continue
        return name


def validate_email(msg):
    while True:
        email = input(msg).strip()
        pattern = r"^(?!.*\.\.)(?!.*-\.)[\w\.-]+@[\w\.-]+\.\w+$"
        # the pattern consists of (?!.*\.\.) which prevents two dots after each other and (?!.*-\.) which prevents -. in the email and the rest is for normal email patterns
        # since this is a mailfor students so it may contain multiple dots at the domain name like: example@university.edu.eg
        if not bool(re.fullmatch(pattern, email)):
            print("Please enter a valid email")
            continue
        return email


def validate_phone(msg):
    while True:
        phone = input(msg).strip()
        if len(phone) != 11 or not phone.isdigit():
            print("Please enter a valid phone number")
            continue
        return phone


def handle_db_error(
    error,
):
    if error.errno == errorcode.ER_DUP_ENTRY:  # constant equivelent to error code 1062
        if "Email" in error.msg:
            print("proccess failed")
            print("This email already exists")
        if "Phone" in error.msg:
            print("proccess failed")
            print("This phone number already exists")
        if "Name" in error.msg:
            print("proccess failed")
            print("this name already exists")

    if (
        error.errno
        == errorcode.ER_NO_REFERENCED_ROW_2  # constant equivelent to error code 1452
    ):
        print(f"The department doesn't exist")


# def check_id(db, id, table):
#     cursor = db.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM %s where Sid = %s", (table, id))
#     student = cursor.fetchone()
#     if not student:
#         return False
#     return True
