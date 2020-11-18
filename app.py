from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/parks/')
def parks():
	with open('parks.json', 'r') as f:
		parks = json.load(f)

	return render_template("parks.html", parks = parks)

if __name__ == "__main__":
	app.run()