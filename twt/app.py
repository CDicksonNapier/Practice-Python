import requests
import os

from flask import Flask, render_template

API_KEY=os.environ["API_KEY"]
BASE_URL ="https://api.openweathermap.org/data/2.5/"
CITY="Edinburgh"
LAT= 55.9533
LON= 3.1883

app = Flask(__name__, static_url_path="", static_folder="web/static", template_folder="web/templates")
@app.route('/')

def index():
    return render_template('index.html', message="HELLO")

@app.route('/current')
def current():
  try:
    r = requests.get(f"{BASE_URL}/weather?q={CITY}&units=metric&appid={API_KEY}")
    r.raise_for_status()
    data = r.json()

    current_weather ={
        "description": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["icon"],
        "name": data["name"],
        "temperature": data["main"]["temp"],
        "wind": data["wind"]["speed"]
    }

    return render_template('index.html', weather=current_weather)
  except requests.exceptions.HTTPError as err:
    return f"Error: {err}"


@app.route('/forecast')
def forecast():
    r = requests.get(f"{BASE_URL}/onecall?lat={LAT}&lon={LON}&units=metric&appid={API_KEY}").json()
    return render_template('index.html', forecast=r['daily'])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html', message=error ), 404