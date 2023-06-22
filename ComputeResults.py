from CalculationsResult import CalculationsResult


class ComputeResults:
    '''A class that will compute the results for the reports and store those in the calculationResults type object.'''

    def __init__(self) -> None:
        pass

    def assign_to_results_class(self, weather_readings) -> CalculationsResult:
        '''Go through the weather_readings list and calculates the required values. Then assign them to the
        CalculationsResult class.
        '''

        # Using the lambda function to pass an extra parameter for the max function. That extra parameter is the value
        # at the index of that specific reading.
        max_temp_entry = max(weather_readings, key=lambda x: x.temperature.max)
        max_temp = max_temp_entry.temperature.max
        max_temp_date = max_temp_entry.date
        min_temp_entry = min(weather_readings, key=lambda x: x.temperature.min)
        min_temp = min_temp_entry.temperature.min
        min_temp_date = min_temp_entry.date
        max_humidity_entry = max(weather_readings, key=lambda x: x.humidity.max)
        max_humidity = max_humidity_entry.humidity.max
        max_humidity_date = max_humidity_entry.date
        sum_highest_temp = 0
        sum_lowest_temp = 0
        sum_mean_humidity = 0
        for reading in weather_readings:
            sum_highest_temp += reading.temperature.max
            sum_lowest_temp += reading.temperature.min
            sum_mean_humidity += reading.humidity.mean
        avg_highest_temp = sum_highest_temp // len(weather_readings)
        avg_lowest_temp = sum_lowest_temp // len(weather_readings)
        avg_mean_humidity = sum_mean_humidity // len(weather_readings)
        calculations = CalculationsResult()
        calculations.set_extremes(max_temp, max_temp_date, min_temp, min_temp_date, max_humidity, max_humidity_date)
        calculations.set_average(avg_highest_temp, avg_lowest_temp, avg_mean_humidity)
        return calculations


