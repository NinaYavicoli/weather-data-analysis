# This file defines the database structure using SQLAlchemy and creates the SQLite database

from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# C4: Creates the table and defines columns and datatypes
class HistWeather(Base):
    __tablename__ = 'hist_weather'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)

    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)

    avg_wind = Column(Float)
    min_wind = Column(Float)
    max_wind = Column(Float)

    sum_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)

# Create SQLite database file
engine = create_engine('sqlite:///weather.db')
