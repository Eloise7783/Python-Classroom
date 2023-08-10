import pyodbc  # We need the module to connecto the db

# We set up an object to describe how to connect to the DB
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
# We open the connection to the database (like opening a file)
# This creates an intermediate DB object
conn = pyodbc.connect(connectionString)
# We use our new object to create another object called a cursor
# They cursor can send SQL commands to the DB
cur = conn.cursor()
# We send a command to the DB and save the result
result = cur.execute('SELECT * FROM company').fetchall()
whereResult = cur.execute("select * from company where county = 'Devon'").fetchall()
cont = cur.execute('SELECT * FROM contact').fetchall()
whereResult1 = cur.execute("select contact_name from contact where contact_name like 'q%'").fetchall()
department = cur.execute('select * from dept').fetchall()
whereResult2 = cur.execute("select manager from dept where sales_target between '15' and '45'").fetchall()
salespeople = cur.execute('select * from salesperson').fetchall()
whereResult3 = cur.execute("select first_name,last_name from salesperson where county in('London','Hampshire')").fetchall()
sales = cur.execute('select * from sale').fetchall()
whereResult4 = cur.execute("select * from sale where order_value > 15").fetchall()
# We close the connection
conn.close()
# We display the result we saved
print('--- Company Table ---')
print('                     ')
for row in result:
    print(row)
print('                     ')
print('--- Companies in Devon ---')
print('                     ')
for row in whereResult:
    print(row)
print('                     ')
print('--- Contact Table ---')
print('                     ')
for row in cont:
    print(row)
print('                     ')
print('--- Contact Name beqins with Q ---')
print('                     ')
for row in whereResult1:
    print(row)
print('                     ')
print('--- Dept Table ---')
print('                     ')
for row in department:
    print(row)
print('                     ')
print('--- Dept Manager with Sales Target Between 15 and 45 ---')
print('                     ')
for row in whereResult2:
    print(row)
print('                     ')
print('--- Salesperson Table ---')
print('                     ')
for row in salespeople:
    print(row)
print('                     ')
print('--- Salespeople in London or Hampshire ---')
print('                     ')
for row in whereResult3:
    print(row)
print('                     ')
print('--- Sales Table ---')
print('                     ')
for row in sales:
    print(row)
print('                     ')
print('--- Sales Where order value > 15 ---')
print('                     ')
for row in whereResult4:
    print(row)