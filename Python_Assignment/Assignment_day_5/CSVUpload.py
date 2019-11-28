import pymysql
import csv


db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor(pymysql.cursors.DictCursor)

reader = csv.reader(open('Employee.csv', 'r'), delimiter=',')
for data in reader:
    sql = "INSERT INTO Employee (FNAME, LNAME, LOCATION) VALUES (%s, %s, %s)"
    val = [data[0], data[1], data[2]]
    cursor.execute(sql, val)



# data = cursor.execute("""CREATE TABLE
#                       Employee(
#                       FNAME CHAR(20) NOT NULL,
#                          LNAME CHAR(20),
#                          LOCATION CHAR(20))""")

db.commit()
db.close()
