import pyodbc

server = 'Hariishs\\SQLEXPRESS'
database = 'employee'
driver = '{SQL Server}'

conn = pyodbc.connect(
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

def create_employee(emp_id, name, age, department):
    cursor.execute(
        "INSERT INTO employee_table (emp_id, name, age, department) VALUES (?, ?, ?, ?)",
        (emp_id, name, age, department)
    )
    conn.commit()
    print("Employee Added!!!")

def read_employees():
    cursor.execute("SELECT * FROM employee_table")
    for row in cursor.fetchall():
        print(row)

def update_employee(emp_id, new_age):
    cursor.execute(
        "UPDATE employee_table SET age=? WHERE emp_id=?",
        (new_age, emp_id)
    )
    conn.commit()
    print("Employee Updated")

def delete_employee(emp_id):
    cursor.execute(
        "DELETE FROM employee_table WHERE emp_id=?",
        (emp_id,)  # Note the comma here
    )
    conn.commit()
    print("Employee Deleted!!")

# Test calls
create_employee(1, "aana", 40, "QA")
create_employee(2, "bhavi", 20, "QA")
create_employee(3, "caana", 30, "QA")
create_employee(4, "daana", 60, "QA")
create_employee(5, "Eaana", 24, "QA")
read_employees()
update_employee(1, 10)
read_employees()
delete_employee(1)
