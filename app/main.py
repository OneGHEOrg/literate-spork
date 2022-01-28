import datetime as dt, json,pytest
from flask import Flask
app = Flask(__name__)

@app.route("/datetime")
def datetime():
    current_time = dt.datetime.now()
    datetime_response = {'message': 'Automate All the things!', 'timestamp': f'{current_time}'}
    return json.dumps(datetime_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')