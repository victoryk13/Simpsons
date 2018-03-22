from flask import Flask, render_template, jsonify
from database import character, location

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/characters')
def characters():

    character_output = character()
    return (jsonify(character_output))


@app.route('/locations')
def locations():

    location_output = location()
    return (jsonify(location_output))


if __name__ == '__main__':
    app.run(debug=True)
