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
Simpsons_top_50_characters = Base.classes.simpsons_top_50_characters
Simpsons_top_50_metadata = Base.classes.simpsons_top_50_metadata

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

def top_50_character():
    queryExpression = session.query(Simpsons_top_50_characters)
    top50CharacterList = [each.character_name for each in queryExpression]
    return top50CharacterList

def metadata(character):
    queryExpression = session.query(Simpsons_top_50_metadata.character_name, Simpsons_top_50_metadata.word_count, Simpsons_top_50_metadata.sentence_count, Simpsons_top_50_metadata.syllable_count, Simpsons_top_50_metadata.Flesch_readability, Simpsons_top_50_metadata.Flesch_Kincaid_grade, Simpsons_top_50_metadata.gender, Simpsons_top_50_metadata.status, Simpsons_top_50_metadata.hair, Simpsons_top_50_metadata.occupation, Simpsons_top_50_metadata.first_appearance, Simpsons_top_50_metadata.img_url).filter(Simpsons_top_50_metadata.character_name == character).all()
    metadataDict = [{"Character Name": each[0],
             "Word Count": each[1],
             "Sentence Count": each[3],
             "Syllable Count": each[2],
             "Flesch Readability": each[4],
             "Flesch-Kincaid Grade": each[5],
             "Gender": each[6],
             "Status": each[7],
             "Hair": each[8],
             "Occupation": each[9],
             "First Appearance": each[10],
             "Image URL": each[11]
            } for each in queryExpression]
    return metadataDict