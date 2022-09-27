from flask import Flask,render_template

app = Flask(__name__)
JOBS=[
  {'id':1,
    'Title':'Data Analyst',
     'Location':'Bengaluru',
      'salary':'Rs. 20,00,000' 
  },
  {
  'id':2,
    'Title':'Data Scientist',
     'Location':'Bengaluru',
      'salary':'Rs. 20,00,000' 
  },
  {
  'id':3,
    'Title':'Data Analyst',
     'Location':'Chennai',
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS,company_name='Jovian')
  
  @app.route("/api/jobs")
  def list_jobs():
    return jsonify(JOBS)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)