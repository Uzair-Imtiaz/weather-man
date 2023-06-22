

class _Temperature:
    ''' A private class to hold readings of temperature type.'''

    def __init__(self, max_, mean, min_) -> None:
        ''' Assign min, mean, max values after casting them to int.'''

        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _DewPoint:
    '''A private class to hold readings of dew point type.'''

    def __init__(self, std, mean, min_) -> None:
        '''Assign min, mean, max values after casting them to int.'''

        self.std = int(std) if std.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min_ = int(min_) if min_.isdigit() else 0


class _Humidity:
    '''A private class to hold readings of humidity type.'''

    def __init__(self, max_, mean, min_) -> None:
        '''Assign min, mean, max values after casting them to int.'''

        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _SeaLevelPressure:
    '''A private class to hold readings of sea level pressure type.'''

    def __init__(self, max_, mean, min_) -> None:
        '''Assign min, mean, max values after casting them to int.'''
        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _Visibility:
    '''A private class to hold readings of visibility type.'''

    def __init__(self, max_, mean, min_) -> None:
        '''Assign min, mean, max values after casting them to int.'''
        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0
        self.min = int(min_) if min_.isdigit() else 0


class _WindSpeed:
    ''' A private class to hold readings of wind speed type. '''

    def __init__(self, max_, mean) -> None:
        ''' Assign min, mean, max values after casting them to int.'''

        self.max = int(max_) if max_.isdigit() else 0
        self.mean = int(mean) if mean.isdigit() else 0


class WeatherReadings:
    ''' A class that holds the weather reading values.'''

    def __init__(self, data) -> None:
        self.date = data[0]
        self.temperature = _Temperature(data[1], data[2], data[3])
        self.dew_point = _DewPoint(data[4], data[5], data[6])
        self.humidity = _Humidity(data[7], data[8], data[9])
        self.sea_level_pressure = _SeaLevelPressure(data[10], data[11], data[12])
        self.visibility = _Visibility(data[13], data[14], data[15])
        self.wind_speed = _WindSpeed(data[16], data[17])
        self.max_gust_speed = data[18]
        self.precipitation = data[19]
        self.cloud_cover = data[20]
        self.events = data[21]
        self.wind_dir_degrees = data[22]
