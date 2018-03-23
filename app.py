from flask import Flask, render_template, jsonify
from database import character, location, character_count, male_count, female_count, missing_gender_count, location_count, episode_count, season_count, most_episodes_in_season, top_viewers_episodes, top_views_episodes, top_imdb_rating, top_imdb_votes

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


@app.route('/number_of_characters')
def number_of_characters():

    characters_count = character_count()
    return (jsonify(characters_count))


@app.route('/number_of_male_characters')
def number_of_male_characters():

    males_count = male_count()
    return (jsonify(males_count))


@app.route('/number_of_female_characters')
def number_of_female_characters():

    females_count = female_count()
    return (jsonify(females_count))


@app.route('/number_of_gender_unknown_characters')
def number_of_gender_unknown_characters():

    missing_genders_count = missing_gender_count()
    return (jsonify(missing_genders_count))


@app.route('/number_of_locations')
def number_of_locations():

    locations_count = location_count()
    return (jsonify(locations_count))


@app.route('/number_of_episodes')
def number_of_episodes():

    episodes_count = episode_count()
    return (jsonify(episodes_count))


@app.route('/number_of_seasons')
def number_of_seasons():

    seasons_count = season_count()
    return (jsonify(seasons_count))


@app.route('/most_episodes_in_a_season')
def most_episodes_in_a_season():

    most_episodes_in_a_season = most_episodes_in_season()
    return (jsonify(most_episodes_in_a_season))


@app.route('/top_ten_episodes_with_most_viewers')
def top_ten_episodes_with_most_viewers():

    top_viewer_episodes = top_viewers_episodes()
    return (jsonify(top_viewer_episodes))


@app.route('/top_ten_episodes_with_most_views')
def top_ten_episodes_with_most_views():

    top_view_episodes = top_views_episodes()
    return (jsonify(top_view_episodes))


@app.route('/top_ten_episodes_with_highest_imdb_rating')
def top_ten_episodes_with_highest_imdb_rating():

    top_imdb_ratings = top_imdb_rating()
    return (jsonify(top_imdb_ratings))


@app.route('/top_ten_episodes_with_most_imdb_votes')
def top_ten_episodes_with_most_imdb_votes():

    top_imdb_vote = top_imdb_votes()
    return (jsonify(top_imdb_vote))


if __name__ == '__main__':
    app.run(debug=True)