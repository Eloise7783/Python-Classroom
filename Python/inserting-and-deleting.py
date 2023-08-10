from ast import Try, excepthandler
import pyodbc  # We need the module to connect the db

# We set up an object to describe how to connect to the DB
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
# We open the connection to the database (like opening a file)
# This creates an intermediate DB object
conn = pyodbc.connect(connectionString)
# We use our new object to create another object called a cursor
# They cursor can send SQL commands to the DB
cur = conn.cursor()
try:
    #insert a company
    qaInsert = cur.execute("insert into company(company_no, company_name, tel, county, post_code) values (4500, 'QA', '01234 567890', 'London', 'w1 1aa')")
except: 
    print("Could not insert, have you already committed this?")
try:
    ammendment = cur.execute("update company set county = 'West London' where county = 'London'")
except: 
    print("Could not update, have you already committed this?")
try:
    deletion = cur.execute("delete from salesperson where first_name = 'Inge'")
except:
    print("Could not delete, have you already committed this?")
conn.commit()

updated = cur.execute("SELECT * FROM company").fetchall()
insertion = cur.execute("SELECT * FROM company where company_name = 'QA'").fetchall()
deleted = cur.execute("SELECT * FROM salesperson").fetchall()

# We close the connection
conn.close()

print('--- Update ---')
for row in updated:
    print(row)
print("\n")
print('--- Insert ---')
for row in insertion:
    print(row)
print("\n")
print("--- Delete ---")
for row in deleted:
    print(row)

        