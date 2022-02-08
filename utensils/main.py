import datetime as dt, json
from flask import Flask

app = Flask(__name__)

def spork_routes(app):

    @app.route("/")
    def gandalf():
        gandalf_response = {'Gandalf': 'You shall not pass without the sacred utensil!'}
        return json.dumps(gandalf_response)

    @app.route("/datetime")
    def date_time():
        current_time = dt.datetime.now()
        datetime_response = {'message': 'Automate All the things!', 'timestamp': f'{current_time}'}
        return json.dumps(datetime_response)

if __name__ == "__main__":
    spork_routes(app)
    app.run(host='0.0.0.0')