# testing will use a different set of location and date data than main program

def testing():
    from weather import WeatherData
    from database import HistWeather, engine, Base
    from sqlalchemy.orm import sessionmaker

# Test 1: validates that the weather object is successfully created and values are assigned correctly
    weather = WeatherData(39.0510, -94.5884, 10, 17, 2000)
    weather.get_data()

    print("Test 1: Object Creation Validation")
    print(f"Location Latitude: {weather.latitude}")
    print(f"Location Longitude: {weather.longitude}")
    print(f"Date: {weather.month}/{weather.day}/{weather.year}")

    assert weather.latitude == 39.0510
    assert weather.longitude == -94.5884
    assert weather.month == 10
    assert weather.day == 17
    assert weather.year == 2000

    print("Test 1: passed :)\n")

# Test 2: validates that a complete list of raw data is being collected and sorted from API
    print("Test 2: Data Collection Validation")
    temps, winds, precip = weather.get_data()
    years = [weather.year - i for i in range(5)]

    print(f"Years checked: {years}")
    print(f"Raw Temp Data: {temps}")
    print(f"Raw Wind Data: {winds}")
    print(f"Raw Precip Data: {precip}")

    assert len(temps) == 5
    assert len(winds) == 5
    assert len(precip) == 5

    print("Test 2: passed :))\n")

# Test 3: tests that the database is storing data
    print("Test 3: Database Creation and Query Validation")

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

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

    results = session.query(HistWeather).all()
    # This should equal one
    print(f"Number of records: {len(results)}")
    assert len(results) == 1

    print("Test 3: passed :)))\n")
    print("All tests passed successfully")

if __name__ == "__main__":
    testing()
