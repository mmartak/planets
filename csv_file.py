import sqlite3
import csv

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE t (name,age);")

with open('data.csv', 'r') as fin:
  dr = csv.DictReader(fin)
  to_db = [(i['name'], i['age']) for i in dr]

cursor.executemany("INSERT INTO t (name,age) VALUES (?, ?);", to_db)
connection.commit()

cursor = connection.cursor()
cursor.execute("SELECT * FROM t;")
results = cursor.fetchall()
for r in results:
 print(r)
cursor.close()
connection.close()