
class Statistic:
    '''Class that represents users typing test statistics.
        Attributes:
            name: String, identifier of player
            time: Float, time of completion in seconds
            difficulty: Integer, difficulty of sudoku
            date: String, date of completion
    '''

    def __init__(self, name=None, time=0, difficulty=0, date=None):
        self.name = name
        self.time = time
        self.difficulty = difficulty
        self.date = date

    def get_time_formatted(self):
        # Returns time in format M:SS
        minutes = self.time // 60
        seconds = self.time % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        seconds = str(seconds)[:5]
        return f"{int(minutes)}:{seconds}"
