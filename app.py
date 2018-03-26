from flask import Flask, render_template, jsonify
from database import character, location, character_count, male_count, female_count, missing_gender_count, location_count, episode_count, season_count, most_episodes_in_season, top_viewers_episodes, top_views_episodes, top_imdb_rating, top_imdb_votes, top_50_character, metadata

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/homer')
def homer():
    return render_template('homer.html')


@app.route('/top_50_characters')
def top_50_characters():

    top_50_character_output = top_50_character()
    return (jsonify(top_50_character_output))


@app.route('/character_metadata/<character>')
def character_metadata(character):

    metadataDict = metadata(character)

    return jsonify(metadataDict)


if __name__ == '__main__':
    app.run(debug=True)
