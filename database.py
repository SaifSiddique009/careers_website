import pymysql

def get_db_connection():
  connection = pymysql.connect(
      charset="utf8mb4",
      connect_timeout=10,
      cursorclass=pymysql.cursors.DictCursor,
      db="defaultdb",
      host="mysql-career-website.a.aivencloud.com",
      password="AVNS_Uhm7MbwzYt-f9zfK7k7",
      port=28283,
      user="avnadmin",
      read_timeout=10,
      write_timeout=10,
  )
  return connection

def load_jobs_from_db():
  connection = get_db_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM jobs")
  jobs = cursor.fetchall()
  return jobs
