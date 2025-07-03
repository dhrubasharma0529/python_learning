import mysql.connector
connection = mysql.connector.connect(
    host= "localhost",
    user = "root",
    database = "Student"
)
if(connection):
    print("the database is connected successfully.")
else:
    print("The connection is not successful.")
mydb = connection.cursor()
mydb.execute('Select id from student')
data = mydb.fetchall()
#insert
mydb.execute("insert into `student` (`name`) values('Dhruba')")
connection.commit()
# update
mydb.execute("Update `student` Set `name` = 'suda' WHERE id = 1")
connection.commit()
# delete 
mydb.execute("Delete from `student` where id = 1.")
connection.commit()

