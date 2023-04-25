
from tkinter import VERTICAL, Tk, ttk
from services.statistic_service import statistic_service


class StatisticsView:

    def __init__(self, show_game):
        self._show_game = show_game

        self._root = Tk()
        self._root.title("Saved Times")
        self._root.geometry("+589+194")
        self._style = ttk.Style()
        self._style.configure("TFrame", background="#FFCCCC")

        self._frame = ttk.Frame(master=self._root)

        self._stats_table = None

        self._get_stats_table()
        self._add_widgets()
        self._frame.pack()

        self._root.mainloop()

    def _add_widgets(self):
        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._back_to_game)
        back_button.grid(row=2, column=0, padx=5, pady=5)

    def _back_to_game(self):
        self._root.destroy()
        self._show_game()

    def _get_stats_table(self):
        if self._stats_table:
            self._delete_table()

        stats = statistic_service.get_all()

        if stats:
            columns = ("Name", "Time", "Difficulty", "Date")
            self._stats_table = ttk.Treeview(
                master=self._frame, columns=columns, show="headings", selectmode="none")
            self._style.configure("Treeview.Heading", background="#FFCCCC")
            for column in columns:
                self._stats_table.heading(column, text=column)
            for stat in stats:
                self._stats_table.insert("", "end", values=(
                    stat.name, stat.get_time_formatted(), stat.difficulty, stat.date))
            self._stats_table.grid(row=1, columnspan=1, padx=5, pady=5)
            self._insert_table_scrollbar(self._stats_table)

        else:
            note = ttk.Label(
                master=self._frame, text="You do not currently have any recorded times", background="#FFCCCC")
            note.grid(row=1, padx=5, pady=5)

    def _delete_table(self):
        for element in self._stats_table.get_children():
            self._stats_table.delete(element)

    def _insert_table_scrollbar(self, table):
        scrollbar = ttk.Scrollbar(
            self._frame, orient=VERTICAL, command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky='NS')
