import pyodbc

server = 'Hariishs\\SQLEXPRESS'
database = 'school'
driver = '{SQL Server}'

conn= pyodbc.connect(
    f'Driver={driver};'
    f'Database={database};'
    f'Server={server};'
    'Truested_Connection = yes;'
)

cursor=conn.cursor()

def create_student(roll_no,name,std,age):
    cursor.execute(
        "INSERT INTO stud (roll_no,name,std,age) VALUES (?, ?, ?, ?)",
        (roll_no,name,std,age)
    )
    conn.commit()
    print("Student added!!!")


def read_student():
    cursor.execute("SELECT * FROM stud")
    for row in cursor.fetchall():
        print(row)

def update_student(roll_no, new_age):
    cursor.execute(
        "UPDATE stud SET age=? WHERE roll_no=?",
        (new_age, roll_no)
    )
    conn.commit()
    print("Student Updated")

def delete_student(roll_no):
    cursor.execute(
        "DELETE FROM stud WHERE roll_no=?",
        (roll_no,)  # Note the comma here
    )
    conn.commit()
    print("Student Deleted!!")

create_student(1, "anu", 4, 8)
create_student(2, "ram", 2, 6)
create_student(3, "guna", 3, 7)
create_student(4, "chandru", 6, 10)
create_student(5, "vibin", 5, 9)
create_student(6, "zoya", 5, 9)