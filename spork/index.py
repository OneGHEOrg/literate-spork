import datetime, json
from flask import Flask

app = Flask(__name__)

@app.route("/datetime")
def hello_world():
  current_time = datetime.datetime.now()
  simple_response = {'message': 'Automate All the things!', 'timestamp': f'{current_time}'}
  return json.dumps(simple_response)