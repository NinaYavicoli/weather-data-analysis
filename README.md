## Description

This program retrieves historical weather data for a selected location and date using the Open-Meteo API. It collects data for the most recent five years and calculates summary statistics for temperature, wind speed, and precipitation, including averages, sums, and minimum/maximum values.

The program is organized into three files:

- **weather.py**  
  Contains the WeatherData class, API call logic, and calculations

- **database.py**  
  Defines the database structure and creates the SQLite database

- **main.py**  
  Inserts data into the database, queries the table, and displays the formatted summary output

- **test.py**  
  Runs three tests to verify object initialization, raw data collection across five years, and database insert/query functionality using a different set of date and location data.


---

## Inputs

The program uses predefined inputs in `main.py`:

### Location: Depew, New York  
Latitude: 42.9039  
Longitude: -78.6923  

### Date  
January 14 (for years 2022–2026)

---

## Commands

The following commands (method calls) are used in the program:

- `weather.get_data()`  
  Retrieves weather data from the API for five years and calculates summary statistics  

- `session.add(record)`  
  Inserts the calculated data into the SQLite database  

- `session.commit()`  
  Saves the data to the database  

- `session.query(HistWeather).all()`  
  Retrieves stored data from the database  

---

## Output

The program outputs:

- A formatted display of the selected date and location  
- A summary of five-year weather statistics, including:  
  - Average, minimum, and maximum temperature  
  - Average, minimum, and maximum wind speed  
  - Total, minimum, and maximum precipitation  

The output is displayed in the console after querying the SQLite database.
