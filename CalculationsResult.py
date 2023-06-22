

class CalculationsResult:
    '''A class that will hold the calculations results.'''

    def __init__(self):
        '''Initialise the variables to be used to store the calculation results.'''

        self.average_mean_humidity = None
        self.lowest_average_temperature = None
        self.highest_average_temperature = None
        self.humidity = None
        self.lowest_temperature_day = None
        self.lowest_temperature = None
        self.highest_temperature_day = None
        self.highest_temperature = None
        self.most_humid_day = None

    def set_extremes(self, highest, day_of_highest, lowest, day_of_lowest, humidity, most_humid_day) -> None:
        '''Sets the values of the highest and lowest temperatures and maximum humidity.'''

        self.highest_temperature = highest
        self.highest_temperature_day = day_of_highest
        self.lowest_temperature = lowest
        self.lowest_temperature_day = day_of_lowest
        self.humidity = humidity
        self.most_humid_day = most_humid_day

    def set_average(self, highest_avg_temperature, lowest_avg_temperature, avg_mean_humidity) -> None:
        '''Sets the values of the highest and lowest temperatures and maximum humidity.'''

        self.highest_average_temperature = highest_avg_temperature
        self.lowest_average_temperature = lowest_avg_temperature
        self.average_mean_humidity = avg_mean_humidity
