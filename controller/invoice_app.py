import tkinter as tk
from datetime import datetime
import calendar as cl

from views.calendar_view.calendar_view import CalendarView
from views.calendar_view.calendar_section import CalendarSection
from views.entries_view.entries_view import EntriesView

from models.entry import Entry


class InvoiceApp(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, root, *args, **kwargs)

        # Today's date
        self.today = datetime.today()

        self.month = self.today.month
        self.year = self.today.year

        self.current_block = None

        self.entries = {}

        # CalendarView displaying todays date
        self.calendar_view = CalendarView(
            self, self, self.today, self.today.month, self.today.year)
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.entries_view = None

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
        self.month = self.month - 1

        if self.month < 1:
            self.month = 12
            self.year = self.year - 1

        # Build updated calendar view
        new_cal_view = CalendarView(
            self, self, self.today, self.month, self.year)

        self.calendar_view.destroy()

        self.calendar_view = new_cal_view
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def next_month(self, event):
        self.month = self.month + 1

        if self.month > 12:
            self.month = 1
            self.year = self.year + 1

        # Build updated calendar section
        new_cal_view = CalendarView(
            self, self, self.today, self.month, self.year)

        self.calendar_view.destroy()

        self.calendar_view = new_cal_view
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def new_entry(self, event):
        self.entries_view.entries_list.entries_lst.insert(
            '', 'end', text="1", values=("2020-11-17", "Labor", 8, 25))

    def delete_entry(self, event):
        item = self.entries_view.entries_list.entries_lst.selection()
        try:
            self.entries_view.entries_list.entries_lst.delete(item)
        except:
            print("Nothin to delete here!!")

    def enter_entries_view(self, event):

        block_id = event.widget.block_id
        self.current_block = block_id

        # Create entries view
        try:
            self.entries_view = EntriesView(self, self, self.entries[block_id])
        except KeyError:
            self.entries_view = EntriesView(self, self, [])

        # Destroy current calendar view
        self.calendar_view.destroy()
        self.calendar_view = None

        # Display entries view
        self.entries_view.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)

    def return_to_calendar(self, event):

        entries = []

        # Save entries from the view
        for child in self.entries_view.entries_list.entries_lst.get_children():
            entries.append(
                self.entries_view.entries_list.entries_lst.item(child)["values"])

        # Store them inside corresponding dict key
        self.entries[self.current_block] = entries

        self.current_block = None
        # Create calendar view
        self.calendar_view = CalendarView(
            self, self, self.today, self.month, self.year)

        # Destroy current entries view
        self.entries_view.destroy()
        self.entries_view = None

        # Display calendar view
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
