import os
import tkinter as tk

from controller.invoice_app import InvoiceApp

if __name__ == "__main__":
    # Required to connect to X-Sever
    os.environ["DISPLAY"] = ":0.0"

    root = tk.Tk()
    root.minsize(1000, 500)

    invoice_app = InvoiceApp(root)
    invoice_app.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    root.mainloop()
