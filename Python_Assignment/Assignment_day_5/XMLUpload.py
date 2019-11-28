import pymysql
import xml.dom.minidom

root = xml.dom.minidom.parse("users.xml")
users = root.documentElement

db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor(pymysql.cursors.DictCursor)

# data = cursor.execute("""CREATE TABLE
#                       XMLUser(
#                       FNAME CHAR(20) NOT NULL,
#                          LNAME CHAR(20))""")


for user in users.getElementsByTagName('user'):
    fname = user.getElementsByTagName('fname')[0]
    f = fname.childNodes[0].data
    lname = user.getElementsByTagName('lname')[0]
    l = lname.childNodes[0].data
    sql = "INSERT INTO XMLUser (FNAME, LNAME) VALUES (%s, %s)"
    val = [f, l]
    cursor.execute(sql, val)


db.commit()
db.close()


# for user in users.getElementsByTagName('user'):
#     fname = user.getElementsByTagName('fname')[0]
#     f = fname.childNodes[0].data
#     lname = user.getElementsByTagName('lname')[0]
#     l = lname.childNodes[0].data
#     sql = "INSERT INTO User (FNAME, LNAME) VALUES (%s, %s)"
#     val = [f, l]
#     cursor.execute(sql, val)