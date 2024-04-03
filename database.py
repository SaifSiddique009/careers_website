import pymysql
import os

db_conn_pass = os.environ['DB_CONN_PASS']
db_conn_host = os.environ['DB_CONN_HOST']
db_conn_user = os.environ['DB_CONN_USER']

def get_db_connection():
  connection = pymysql.connect(
      charset="utf8mb4",
      connect_timeout=10,
      cursorclass=pymysql.cursors.DictCursor,
      db="defaultdb",
      host=db_conn_host,
      password=db_conn_pass,
      port=28283,
      user=db_conn_user,
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
