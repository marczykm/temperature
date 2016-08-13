from flask import Flask
from flask import render_template
import temperature

app = Flask(__name__)

@app.route("/")
def hello():
	temp = str(temperature.read_temp())
	return render_template('index.html', temp=temp)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)