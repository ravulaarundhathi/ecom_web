import psycopg2

conn = psycopg2.connect(
    host="tramway.proxy.rlwy.net",
    port= 14655,
    user="postgres",
    password="xvaMsbGBNmxOGeaHOeWvxalJctsgURmG",
    database="railway"
)

if conn:
    print("Connection Successful!")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE  IF NOT EXISTS students(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")
conn.commit()


# cursor.execute("INSERT INTO students(id, name, age) VALUES (3,'aru',20), (4,'somya',21), (5,'amulya',20)")
# conn.commit()

cursor.execute("SELECT *FROM students")
rows = cursor.fetchall()
print(rows)

cursor.execute("UPDATE students SET age=24 WHERE id= 5")
conn.commit()
print("Records updated Successfully!")

cursor.execute("UPDATE students set age=24 WHERE ID= 5")

cursor.execute("DELETE FROM students WHERE id=4")
conn.commit()
print("Record Deleted Successfully")

cursor.execute("SELECT *FROM students")
rows = cursor.fetchall()
print(rows)


cursor.execute("SELECT name from students")
rows = cursor.fetchall()
print(rows)


cursor.execute("SELECT *FROM students")
rows = cursor.fetchone()
print(rows)

cursor.execute("SELECT *FROM students WHERE age<25")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT *FROM students ORDER BY age DESC")
rows = cursor.fetchall()
print(rows)


cursor.execute("SELECT *FROM students LIMIT 1")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT *FROM students")
rows = cursor.fetchone()
print(rows)
