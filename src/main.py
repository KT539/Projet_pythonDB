import tkinter as tk
from HomePage import homepage_window
from Login import login_window


def main():
    # creating the main window
    win = tk.Tk()
    win.title("Main Page")
    win.geometry("400x700")
    win.resizable(False, False)

    # login_window(win)
    homepage_window(win)
    win.mainloop()

main()