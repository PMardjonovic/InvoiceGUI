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
        # Changes background color of calendar block to
        # notify users they are pointing to calendar block

        event.widget["bg"] = "#D7DBDD"
        event.widget.date_lbl["bg"] = "#D7DBDD"
        event.widget.time_lbl["bg"] = "#D7DBDD"

    def hover_out(self, event):
        # Reverts background color of calendar block to
        # notify users they are no longer pointing to calendar block

        event.widget["bg"] = "white"
        event.widget.date_lbl["bg"] = "white"
        event.widget.time_lbl["bg"] = "white"

    def prev_month(self, event):
        month = self.calendar_view.month - 1
        year = self.calendar_view.year

        if month < 1:
            month = 12
            year = year - 1

        # Update calendar header
        self.calendar_view.main_header.header_lbl["text"] = f"{cl.month_name[month]}, {year}"

        # Build new calendar section
        new_cal_section = CalendarSection(
            self.calendar_view, self, month, year)

        # Destroy old calendar section
        self.calendar_view.calendar_section.destroy()

        # Pack in new calendar section
        self.calendar_view.calendar_section = new_cal_section
        self.calendar_view.calendar_section.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)

        # Update month and year for CalendarView
        self.calendar_view.month = month
        self.calendar_view.year = year

    def next_month(self, event):
        month = self.calendar_view.month + 1
        year = self.calendar_view.year

        if month > 12:
            month = 1
            year = year + 1

        # Update calendar header
        self.calendar_view.main_header.header_lbl["text"] = f"{cl.month_name[month]}, {year}"

        # Build new calendar section
        new_cal_section = CalendarSection(
            self.calendar_view, self, month, year)

        # Destroy old calendar section
        self.calendar_view.calendar_section.destroy()

        # Pack in new calendar section
        self.calendar_view.calendar_section = new_cal_section
        self.calendar_view.calendar_section.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)

        # Update month and year for CalendarView
        self.calendar_view.month = month
        self.calendar_view.year = year

    def enter_entries_view(self, event):
        pass
