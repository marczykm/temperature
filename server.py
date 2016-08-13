from flask import Flask
from flask import render_template
from flask import jsonify

import time
import temperature

app = Flask(__name__)

@app.route("/")
def index():
	temp = str(temperature.read_temp())
	return render_template('index.html', temp=temp)

@app.route("/api/temperature")
def temperature_json():
	temp = temperature.read_temp()
	return jsonify(timestamp=int(time.time()),temperature=temp)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
