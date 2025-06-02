# Project: PythonDB
# Title: main.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
from Login_test import login_window


def main():
    # creating the main window
    win = tk.Tk()
    win.title("Main Page")
    win.geometry("400x700")
    win.resizable(False, False)

    login_window(win)
    win.mainloop()

main()