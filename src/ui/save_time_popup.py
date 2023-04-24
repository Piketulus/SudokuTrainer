
from tkinter import Tk, ttk

class SaveTimePopup:

    def __init__(self, time, date):
        self.time = time
        self.date = date
        self.name = None

        self._root = Tk()
        self._root.title("Save Time")
        self._root.geometry("300x200")

        self._frame = ttk.Frame(master=self._root)

    def _add_widgets(self):
        # Add a field to enter a name and two buttons to save or cancel
        pass

    def _save(self):
        pass

    def _cancel(self):
        pass

