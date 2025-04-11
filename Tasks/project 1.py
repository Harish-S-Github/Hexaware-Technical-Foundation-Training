import pyodbc
import datetime

server = 'Hariishs\SQLEXPRESS'
database = 'myproject'
driver = '{SQL Server}'
trust_connection='yes'
 
conn = pyodbc.connect(

    f'DRIVER={driver};'

    f'SERVER={server};'

    f'DATABASE={database};'
    
    f'Trust_connection={trust_connection};'

)

 

cursor = conn.cursor()

 

cursor.execute("use myproject;")

cursor.execute("select name from sys.databases;")

print(cursor.fetchall())

cursor.close()

conn.close()