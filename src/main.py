# Project: PythonDB: HarmoniK Festival
# Title: main.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 1.0, last modified:  10.06.2025

import tkinter as tk
from Login import login_window


def main():
    # creating the main window
    win = tk.Tk()
    win.title("Main Page")
    win.geometry("400x700")
    win.resizable(False, False)

    login_window(win)
    win.mainloop()

main()