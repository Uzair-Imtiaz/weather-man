import glob
from FileParser import FileParser
from ComputeResults import ComputeResults
from datetime import datetime


class ReportGenerator:
    '''A class that will generate reports.'''

    def __init__(self) -> None:
        pass

    def report_e(self, files):
        '''Generate a report: for a given year display the highest temperature and day, lowest temperature and day,
    most humid day and humidity.
        '''

        fp = FileParser(files[0])
        readings_list = fp.parse_file()
        weather_readings = fp.populate(readings_list)
        compute = ComputeResults()
        selected_results = compute.assign_to_results_class(weather_readings)
        # Loop through the files of a specified month.
        for file in files[1:]:
            fp = FileParser(file)
            readings_list = fp.parse_file()
            weather_readings = fp.populate(readings_list)
            compute = ComputeResults()
            results = compute.assign_to_results_class(weather_readings)
            if results.highest_temperature > selected_results.highest_temperature:
                selected_results.highest_temperature = results.highest_temperature
                selected_results.highest_temperature_day = results.highest_temperature_day
            if results.lowest_temperature < selected_results.lowest_temperature:
                selected_results.lowest_temperature = results.lowest_temperature
                selected_results.lowest_temperature_day = results.lowest_temperature_day
            if results.humidity > selected_results.humidity:
                selected_results.humidity = results.humidity
                selected_results.most_humid_day = results.most_humid_day
        formatted_date = datetime.strptime(selected_results.highest_temperature_day,
                                           "%Y-%m-%d").strftime("%B %d")
        print('Highest: {}C on {}'.format(selected_results.highest_temperature,
                                          formatted_date))
        formatted_date = datetime.strptime(selected_results.lowest_temperature_day,
                                           "%Y-%m-%d").strftime("%B %d")
        print('Lowest: {}C on {}'.format(selected_results.lowest_temperature,
                                         formatted_date))
        formatted_date = datetime.strptime(selected_results.most_humid_day,
                                           "%Y-%m-%d").strftime("%B %d")
        print('Humidity: {}% on {}'.format(selected_results.humidity,
                                           formatted_date))

    def report_a(self, file):
        '''Generate a report for a given month display the average highest temperature, average lowest temperature,
    average mean humidity.
        '''
        fp = FileParser(file)
        readings_list = fp.parse_file()
        weather_readings = fp.populate(readings_list)
        compute = ComputeResults()
        results = compute.assign_to_results_class(weather_readings)
        print('Highest Average: {}C'.format(results.highest_average_temperature))
        print('Lowest Average: {}C'.format(results.lowest_average_temperature))
        print('Average Mean Humidity: {}%'.format(results.average_mean_humidity))

    def report_c(self, file):
        '''Generate a report for a given month draw two horizontal bar charts on the console for the highest and lowest
    temperature on each day. Highest in red and lowest in blue.
        '''

        fp = FileParser(file)
        readings_list = fp.parse_file()
        weather_readings = fp.populate(readings_list)
        for index, reading in enumerate(weather_readings):
            print(str(index + 1) + "\033[34m+\033[0m" * reading.temperature.min, end='')
            print("\033[31m+\033[0m" * reading.temperature.max, '{}C - {}C'.format(reading.temperature.min,
                                                                                   reading.temperature.max))

    # noinspection DuplicatedCode
    def generate_report(self, *args):
        '''Send calls to all the appropriate classes and their methods to generate results object and then use that
        object to generate the report.
        '''

        months = [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
        ]
        path_to_files_dir = args[0]
        ranges = []
        for i in range(1, len(args)):
            ranges.append(args[i])

        # Using glob.glob function to get a list of all the filenames having the given month or year as wildcard.
        if ranges[2] is not None:
            pattern = f"{path_to_files_dir}/*{ranges[2]}*"
            files = glob.glob(pattern)
            self.report_e(files)
        if ranges[0] is not None:
            # Get the last word of the range which represents the month. Use that number to get the month's name.
            if len(ranges[0]) > 6:
                month = months[int(ranges[0][-2:]) - 1]
            else:
                month = months[int(ranges[0][-1]) - 1]
            print(month + ' ' + ranges[0][:4])
            pattern = f"{path_to_files_dir}/*{month}*"
            file = glob.glob(pattern)
            self.report_a(file[0])
        if ranges[1] is not None:
            if len(ranges[1]) > 6:
                month = months[int(ranges[1][-2:]) - 1]
            else:
                month = months[int(ranges[1][-1]) - 1]
            print(month + ' ' + ranges[1][:4])
            pattern = f"{path_to_files_dir}/*{month}*"
            file = glob.glob(pattern)
            self.report_c(file[0])
