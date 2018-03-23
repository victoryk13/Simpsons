import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy import func

engine = create_engine("sqlite:///data/simpsons_db.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
inspector = inspect(engine)

Simpsons_characters = Base.classes.simpsons_characters
Simpsons_episodes = Base.classes.simpsons_episodes
Simpsons_locations = Base.classes.simpsons_locations
Simpsons_script_lines = Base.classes.simpsons_script_lines

session = Session(engine)


def character():
    queryExpression = session.query(Simpsons_characters)
    characterList = [each.normalized_name for each in queryExpression]
    return characterList

def location():
    queryExpression = session.query(Simpsons_locations)
    locationList = [each.normalized_name for each in queryExpression]
    return locationList
  
def character_count():
    characterCount = session.query(Simpsons_characters).count()
    return characterCount

def male_count():
    maleCount = session.query(Simpsons_characters).filter_by(gender = 'm').count()
    return maleCount

def female_count():
    femaleCount = session.query(Simpsons_characters).filter_by(gender = 'f').count()
    return femaleCount

def missing_gender_count():
    missingGenderCount = session.query(Simpsons_characters).filter_by(gender = None).count()
    return missingGenderCount

def location_count():
    locationCount = session.query(Simpsons_locations).count()
    return locationCount

def episode_count():
    episodeCount = session.query(Simpsons_episodes).count()
    return episodeCount

def season_count():
    seasonCount = session.query(func.max(Simpsons_episodes.season)).first()[0]
    return seasonCount

def most_episodes_in_season():
    mostEpisodesInSeason = session.query(func.max(Simpsons_episodes.number_in_season)).first()[0]
    return mostEpisodesInSeason

def top_viewers_episodes():
    topViewersEpisodes = session.query(Simpsons_episodes.title, Simpsons_episodes.us_viewers_in_millions).order_by(Simpsons_episodes.us_viewers_in_millions.desc()).limit(10).all()
    return topViewersEpisodes

def top_views_episodes():
    topViewsEpisodes = session.query(Simpsons_episodes.title, Simpsons_episodes.views).order_by(Simpsons_episodes.views.desc()).limit(10).all()
    return topViewsEpisodes

def top_imdb_rating():
    topImdbRating = session.query(Simpsons_episodes.title, Simpsons_episodes.imdb_rating).order_by(Simpsons_episodes.imdb_rating.desc()).limit(10).all()
    return topImdbRating

def top_imdb_votes():
    topImdbVotes = session.query(Simpsons_episodes.title, Simpsons_episodes.imdb_votes).order_by(Simpsons_episodes.imdb_votes.desc()).limit(10).all()
    return topImdbVotes