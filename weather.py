import requests
# class creation (c1)
class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
#initialized with location and date information
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
#WeatherData initially set equal to nothing
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None

        self.avg_wind = None
        self.min_wind = None
        self.max_wind = None

        self.sum_precip = None
        self.min_precip = None
        self.max_precip = None


#make single API call and store data into lists
    def get_data(self):
            temps_list = []
            winds_list = []
            precip_list = []

            for i in range(5):
                    c_year = self.year - i
                    date = f"{c_year:02d}-{self.month:02d}-{self.day:02d}"

                    url = (
                            "https://archive-api.open-meteo.com/v1/archive"
                            f"?latitude={self.latitude}&longitude={self.longitude}"
                            f"&start_date={date}&end_date={date}"
                            "&daily=temperature_2m_mean,wind_speed_10m_max,precipitation_sum"
                            "&temperature_unit=fahrenheit"
                            "&wind_speed_unit=mph"
                            "&precipitation_unit=inch"
                    )

                    response = requests.get(url)
                    data = response.json()

                    temps_list.append(data["daily"]["temperature_2m_mean"][0])
                    winds_list.append(data["daily"]["wind_speed_10m_max"][0])
                    precip_list.append(data["daily"]["precipitation_sum"][0])

    # methods to make calculations
            self.avg_temp = sum(temps_list) / len(temps_list)
            self.min_temp = min(temps_list)
            self.max_temp = max(temps_list)

            self.avg_wind = sum(winds_list) / len(winds_list)
            self.min_wind = min(winds_list)
            self.max_wind = max(winds_list)

            self.sum_precip = sum(precip_list)
            self.min_precip = min(precip_list)
            self.max_precip = max(precip_list)

            return temps_list, winds_list, precip_list
