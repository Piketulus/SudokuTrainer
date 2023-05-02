
import pygame
from .game_UI import UI
from .save_time_popup import SaveTimePopup
from .statistics_view import StatisticsView


class UIControl:
    """
    Class that handles the main control of the different UI screens to allow for switching between them.
    """

    def start(self):
        """
         Start the UI by showing the game screen.
        """
        self._show_game()

    def _show_game(self):
        ui = UI(self._show_save_time_popup, self._show_statistics_view)
        ui.show_screen()

    def _show_save_time_popup(self, time, diffiulty, date):
        pygame.quit()
        SaveTimePopup(time, diffiulty, date, self._show_game)

    def _show_statistics_view(self):
        pygame.quit()
        StatisticsView(self._show_game)
