from flask import Flask
from flask import render_template
import json
import csv

app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Hola mundo!</h1>'


@app.route('/home')
@app.route('/home/<string:opcion>')
def home(opcion='Temperatures'):
  file = open('static/data/components/menu.json', 'r')
  content = file.read()
  #print(content)
  data = json.loads(json.dumps(eval(content)))
  opciones = data["data"]["opciones"]
  #print(opciones)
  set=''
  for opc in opciones:
    if opc['label'] == opcion:
      set = opc['dataset']
  
  dataset=[]      
  file = open("static/data/datasets/{}".format(set), newline='')
  reader = csv.reader(file)
  for row in reader:
    dataset.append(float(row[0]))
  file.close()
  
  return render_template('home.html', opciones=data["data"]["opciones"], opcion=opcion, dataset=dataset )

@app.route('/calculate')
def calculate():
  return render_template('results.html')

app.run(host='0.0.0.0', port=8080)