from tkinter import *    # Standard binding to Tk (tk-inter(face))
from tkinter import ttk  # Binding to newer "themed widgets"

from GUI_functions import check_entry


def make_window():

    def button_function():
        text_entry = username.get()
        answer = check_entry(text_entry)

    root = Tk()  # Defines the top (root) window.

    username = StringVar()
    name = ttk.Entry(root, textvariable=username)
    name.grid(column=0, row=0)

    button = ttk.Button(root, text='Run', command=button_function)
    button.grid(column=0, row=1)

    root.mainloop()


if __name__ == '__main__':
    make_window()

