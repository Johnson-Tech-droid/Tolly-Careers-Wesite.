from flask import Flask , render_template ,jsonify 

app = Flask(__name__)

JOBS = [
  {
    'id' : 2,
    'title' : 'Computer Scientist',
    'location':'Kisumu, Kenya',
    'salary' : '200k',
  },
  {
    'id' : 3,
    'title' : 'Accountant',
    'location' : 'Nairobi, Kenya',
    'salary' : '80k',
  },
  {
  'id' : 4,
  'title' : 'Software Engineer',
  'location' : 'Eldoret, Kenya',
   'salary' : '350k',
  },
  
]

@app.route("/")
def hello_world ():
  return render_template('home.html',
                         jobs = JOBS ,
                         company_name = 'Tolly')

@app.route("/JOBS")
def list_JOBS():
  return jsonify("JOBS")


if __name__ == "__main__":
  app.run("0.0.0.0",debug=True)