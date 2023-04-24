
from .game_UI import UI
from .save_time_popup import SaveTimePopup


class UIControl:

    def start(self):
        self._show_game()

    def _show_game(self):
        ui = UI(self._show_save_time_popup)
        ui.show_screen()

    def _show_save_time_popup(self, time, date):
        SaveTimePopup(time, date, self._show_game)
