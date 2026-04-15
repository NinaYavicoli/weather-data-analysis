from weather import WeatherData
from database import HistWeather, engine, Base
from sqlalchemy.orm import sessionmaker

# reset database for each run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

#creating weather object to use in methods later
weather = WeatherData(42.9039, -78.6923, 1, 14, 2026)

#weather objects
weather.get_data()

#create session
Session = sessionmaker(bind=engine)
session = Session()

#create database record
record = HistWeather(
    latitude = weather.latitude,
    longitude = weather.longitude,
    month = weather.month,
    day = weather.day,
    year = weather.year,
    avg_temp = weather.avg_temp,
    min_temp = weather.min_temp,
    max_temp = weather.max_temp,
    avg_wind = weather.avg_wind,
    min_wind = weather.min_wind,
    max_wind = weather.max_wind,
    sum_precip = weather.sum_precip,
    min_precip = weather.min_precip,
    max_precip = weather.max_precip,
)

#insert row
session.add(record)
session.commit()

# query table
results = session.query(HistWeather).all()

#show results in formatted table using fixed column widths
for row in results:
    print(f"\nMonth: {row.month:02d} | Day: {row.day:02d} | Year Range: 2022 - 2026")
    print(f"Lat: {row.latitude} | Long: {row.longitude}\n")

    print("Summary of five-year weather data:\n")

    print("*" * 118)
    print(
        f"* {'avg temp':^10} "
        f"* {'min temp':^10} "
        f"* {'max temp':^10} "
        f"* {'avg wind':^10} "
        f"* {'min wind':^10} "
        f"* {'max wind':^10} "
        f"* {'sum precip':^10} "
        f"* {'min precip':^10} "
        f"* {'max precip':^10} *"
    )
    print("*" * 118)

    print(
        f"* {row.avg_temp:^10.2f} "
        f"* {row.min_temp:^10.2f} "
        f"* {row.max_temp:^10.2f} "
        f"* {row.avg_wind:^10.2f} "
        f"* {row.min_wind:^10.2f} "
        f"* {row.max_wind:^10.2f} "
        f"* {row.sum_precip:^10.2f} "
        f"* {row.min_precip:^10.2f} "
        f"* {row.max_precip:^10.2f} *"
    )

    print("*" * 118)
