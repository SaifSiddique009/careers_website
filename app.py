from flask import Flask, render_template, jsonify
from database import jobs 

app = Flask(__name__)

# Jobs list
# JOBS = [
#   {
#     'id': 1, 
#     'title': 'Data Analyst',
#     'location': 'Dhaka, Bangladesh',
#     'salary': 'Rs. 10,0000'
#   },
#   {
#     'id': 2, 
#     'title': 'Data Engineer',
#     'location': 'Rajshahi, Bangladesh',
#     'salary': 'Rs. 20,0000'
#   },
#   {
#     'id': 3, 
#     'title': 'Front Engineer',
#     'location': 'Remote'
#   },
#   {
#     'id': 4, 
#     'title': 'BackEnd Engineer',
#     'location': 'Bugura, Bangladesh',
#     'salary': '$ 1,000'
#   }
# ]

def load_jobs_from_db():
  return jobs

@app.route('/')
def hello_world():
  return render_template('home.html',
                        jobs=jobs, 
                        company_name='Artistic')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
