import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

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


def metaData():
    return metaDataList


def metaData():
    return metaDataList


def metaData():
    return metaDataList
