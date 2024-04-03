import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-career-website.a.aivencloud.com",
  password="AVNS_Uhm7MbwzYt-f9zfK7k7",
  read_timeout=timeout,
  port=28283,
  user="avnadmin",
  write_timeout=timeout,
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM jobs")
jobs = cursor.fetchall()