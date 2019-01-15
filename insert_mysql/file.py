import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO student (rollno, name) VALUES (%s, %s)"
val = (1, "Krati")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
