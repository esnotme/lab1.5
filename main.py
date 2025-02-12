from flask import Flask, request, jsonify # type: ignore
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)

@app.route('/stats')
def get_stats():
  
    chicken_count = 0
    fish_count = 0
    vegetable_count = 0
    comp_sp = 0
    comp_m =0
    IT_sp =0
    IT_m =0
    for student in data:
      if student['pref'] == 'Chicken':
        chicken_count += 1
      elif student['pref'] == 'Fish':
        fish_count += 1
      elif student['pref'] == 'Vegetable':
        vegetable_count += 1
      if student['programme'] == 'Computer Science (Special)':
        comp_sp +=1 
      elif student['programme'] == 'Computer Science (Major)': 
        comp_m +=1
      elif student['programme'] == 'Information Technology (Special)': 
        IT_sp +=1 
      elif student['programme'] == 'Information Technology (Major)':
        IT_m +=1

    return jsonify({
      'Chicken': chicken_count,
      'Fish': fish_count,
      'Vegetable': vegetable_count,
      'Computer Science(Special)': comp_sp,
      'Computer Science(Major)': comp_m,
      'Information Technology(Special)': IT_sp,
      'Information Technology(Major)': IT_m
    })   


@app.route('/add/<int:a>/<int:b>')
def add(a,b):
  return str(a + b)

@app.route('/subtract/<int:a>/<int:b>')
def subract(a,b):
  return str(a - b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a,b):
  return str(a * b)

@app.route('/divide/<int:a>/<int:b>')
def divide(a,b):
  return str(a/b)





app.run(host='0.0.0.0', port=8080, debug=True)
