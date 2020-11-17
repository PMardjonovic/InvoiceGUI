import tkinter as tk
from datetime import datetime
import calendar as cl

from views.calendar_view.calendar_view import CalendarView
from views.calendar_view.calendar_section import CalendarSection


class InvoiceApp(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, root, *args, **kwargs)

        # Today's date
        self.today = datetime.today()

        self.calendar_view = CalendarView(
            self, self, self.today, self.today.month, self.today.year)

        # CalendarView displaying todays date
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def hover_in(self, event):
        pass

    def hover_out(self, event):
        pass

    def prev_month(self, event):
        pass

    def next_month(self, event):
        pass

    def enter_entries_view(self, event):
        pass
