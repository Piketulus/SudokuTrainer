
class Statistic:
    '''Class that represents users typing test statistics.
        Attributes:
            name: String, identifier of player
            time: Float, time of completion in seconds
            date: String, date of completion
    '''

    def __init__(self, name = None, time = 0, date = None):
        self.name = name
        self.time = time
        self.date = date

    def get_time_formatted(self):
        #Returns time in format MM:SS
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes}:{seconds:02d}"
        
