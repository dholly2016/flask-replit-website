from flask import Flask, render_template, jsonify
app = Flask(__name__)


JOBS = [
  {
    'id': 1 ,
    'title' : 'Data Analyst',
    'location':'New York, New York',
    'salary':'$80,000'
  },
  {
    'id': 2 ,
    'title' : 'Financial Analyst',
    'location':'Remote',
    'salary':'$80,000'
  },
  {
    'id': 3 ,
    'title' : 'Senior Financial Analyst',
    'location':'Bridgeport, CT',
    'salary':'$80,000'
  },
  {
    'id': 4 ,
    'title' : 'Research Analyst',
    'location': 'Norwalk, CT',
    'salary':'$80,000'
  },
  {
    'id': 5 ,
    'title' : 'Forecast Analyst',
    'location':'Hamden, New York',
    'salary':'$80,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS, 
                        Company = 'Dwight')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)