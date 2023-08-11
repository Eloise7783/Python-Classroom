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
#StudentTable=cur.execute("""alter TABLE Student
#add PRIMARY KEY(StudentID)""")
#StudentTable="""CREATE TABLE Student (
#StudentID int PRIMARY KEY,
#FirstName nvarchar(40) NOT NULL,
#Surname nvarchar(30) NULL,
#Course nvarchar(30) NULL,
#City nvarchar(15) NULL)"""

#insertQuery = [cur.execute("Insert into student(StudentID, FirstName, Surname, Course, City) values (1, 'Eloise', 'Wood', 'DevOps', 'Exeter')"),cur.execute("Insert into student(StudentID, FirstName, Surname, Course, City) values (2, 'Veronica', 'Sawyer', 'Law', 'Westerburg')"),cur.execute("Insert into student(StudentID, FirstName, Surname, Course, City) values (3, 'Doug', 'Dimmadome', 'Ownership', 'Dimmsdale')")]
#updateQuery = [cur.execute("update student set FirstName = 'Heather' where FirstName = 'Doug'"),cur.execute("update student set Surname = 'MacNamara' where Surname = 'Dimmadome'"),cur.execute("update student set Course = 'Sociology' where Course = 'Ownership'"),cur.execute("update student set City = 'Westerburg' where City = 'Dimmsdale'")]
#insertQuery = cur.execute("Insert into student(StudentID, FirstName, Surname, Course, City) values (4, 'Jason', 'Dean', 'Slush-Puppies', 'Ohio')")
               # We close the connection
conn.commit()
selectquery = cur.execute("SELECT * FROM student").fetchall()
conn.close()
# We display the result we saved
for selrow in selectquery:
    print(selrow)