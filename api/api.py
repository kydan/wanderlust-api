import json
import os
from flask import Flask
from flask import render_template
from flask import jsonify

from lib import wandb

app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_root():
  api_paths = ['/phones','/networks','/countries','/reports']
  return render_template('root.html', paths=api_paths)
    
@app.route('/phones/',methods=['GET'])
@app.route('/phones/<id>',methods=['GET'])
def get_phones(id=None):
  data = wandb.phones(id)
  return jsonify(data)
  
@app.route('/networks/',methods=['GET'])
@app.route('/networks/<id>',methods=['GET'])
def get_networks(id=None):
  data = wandb.networks(id)
  return jsonify(data)

@app.route('/countries/',methods=['GET'])
@app.route('/countries/<id>',methods=['GET'])
def get_countries(id=None):
  data = wandb.countries(id)
  return jsonify(data)
  
@app.route('/reports/',methods=['GET'])
def get_reports():
  data = wandb.reports()
  return jsonify(data)
  
if __name__ == "__main__":
  port = 8080 
  host = '0.0.0.0'
  app.run(debug=True,port=port,host=host)

