
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
        self._name_filter_entry = None
        self._maxtime_filter_entry = None
        self._difficulty_filter_dropdown = None

        self._get_stats_table()
        self._add_widgets()
        self._frame.pack()

        self._root.mainloop()

    def _add_widgets(self):
        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._back_to_game)
        back_button.grid(row=3, column=0, padx=5, pady=5)
        filter_label = ttk.Label(
            master=self._frame, text="Filter:", background="#FFCCCC")
        filter_label.grid(row=0, column=0, padx=5, pady=5)
        name_filter_label = ttk.Label(master=self._frame, text="Name:", background="#FFCCCC")
        name_filter_label.grid(row=0, column=1, padx=5, pady=5)
        self._name_filter_entry = ttk.Entry(master=self._frame)
        self._name_filter_entry.grid(row=1, column=1, padx=5, pady=5)
        maxtime_filter_label = ttk.Label(master=self._frame, text="Max time (secs):", background="#FFCCCC")
        maxtime_filter_label.grid(row=0, column=2, padx=5, pady=5)
        self._maxtime_filter_entry = ttk.Entry(master=self._frame)
        self._maxtime_filter_entry.grid(row=1, column=2, padx=5, pady=5)
        difficulty_filter_label = ttk.Label(master=self._frame, text="Difficulty:", background="#FFCCCC")
        difficulty_filter_label.grid(row=0, column=3, padx=5, pady=5)
        self._difficulty_filter_dropdown = ttk.Combobox(master=self._frame, values=["All", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"], state="readonly")
        self._difficulty_filter_dropdown.grid(row=1, column=3, padx=5, pady=5)
        self._difficulty_filter_dropdown.current(0)
        search_button = ttk.Button(master=self._frame, text="Search", command=self._get_stats_table_by_filter)
        search_button.grid(row=1, column=4, padx=5, pady=5)
        reset_button = ttk.Button(master=self._frame, text="Reset", command=self._reset)
        reset_button.grid(row=0, column=4, padx=5, pady=5)

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
            self._stats_table.grid(row=2, columnspan=5, padx=5, pady=5)
            self._insert_table_scrollbar(self._stats_table)

        else:
            note = ttk.Label(
                master=self._frame, text="You do not currently have any recorded times", background="#FFCCCC")
            note.grid(row=2, column=2, padx=5, pady=5)

    def _get_stats_table_by_filter(self):
        name = self._name_filter_entry.get()
        maxtime = self._maxtime_filter_entry.get()
        difficulty = self._difficulty_filter_dropdown.get()

        if not maxtime:
            maxtime = 99999999

        try:
            maxtime = int(maxtime)
        except ValueError:
            self._maxtime_filter_entry.delete(0, "end")
            self._maxtime_filter_entry.insert(0, "Please enter an integer")
            return
        
        if self._stats_table:
            self._delete_table()

        stats = statistic_service.get_all_by_filter(name, maxtime, difficulty)

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
            self._stats_table.grid(row=2, columnspan=5, padx=5, pady=5)
            self._insert_table_scrollbar(self._stats_table)

        else:
            note = ttk.Label(
                master=self._frame, text="No records match your filters")
            note.grid(row=2, column=2, padx=5, pady=5)

    def _delete_table(self):
        for element in self._stats_table.get_children():
            self._stats_table.delete(element)

    def _insert_table_scrollbar(self, table):
        scrollbar = ttk.Scrollbar(
            self._frame, orient=VERTICAL, command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=5, sticky='NS')

    def _reset(self):
        self._name_filter_entry.delete(0, "end")
        self._maxtime_filter_entry.delete(0, "end")
        self._difficulty_filter_dropdown.set("All")
        self._get_stats_table()
