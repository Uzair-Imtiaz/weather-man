from WeatherReadings import WeatherReadings
import csv


class FileParser:
    '''A class that parses the files and populates the readings data structure with correct data types.'''

    def __init__(self, filename: str) -> None:
        '''Initialise the filename attribute'''
        self.filename = filename

    def parse_file(self) -> list:
        '''Open the file using csv.DictReader which reads the data into a dictionary. Iterate over the data and append
        it to a list. Return that list.
        '''
        readings_list = []
        with open(self.filename, 'r', encoding="utf-8") as records_file:
            reader = csv.reader(records_file)
            next(reader)
            for row in reader:
                readings_list.append(row)
            return readings_list

    def populate(self, readings_list) -> list:
        '''Assign data read from the file to the object of weatherReadings class. Return the list.'''

        weather_readings = []
        for reading in readings_list:
            w_reading = WeatherReadings(reading)
            weather_readings.append(w_reading)
        return weather_readings


