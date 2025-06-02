# Project: PythonDB
# Title: update_Band.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
from tkinter import messagebox
from DB_managment import updateBand


def updateBand_window(win, selected_band_id):

    win.title("Updating the band's info - " + win.username)

    # configure the main window
    win.grid_rowconfigure(0, weight=1)
    win.grid_columnconfigure(0, weight=1)

    # create an outer frame
    outer_frame = tk.Frame(win)
    outer_frame.grid(row=0, column=0, sticky="nsew")

    # configure the outer frame to center the inner frame
    # used ChatGPT to understand line weight, then wrote my own code
    outer_frame.grid_rowconfigure(0, weight=2)
    outer_frame.grid_rowconfigure(1, weight=0)
    outer_frame.grid_rowconfigure(2, weight=2)
    outer_frame.grid_columnconfigure(0, weight=1)

    # create an inner frame
    inner_frame = tk.Frame(outer_frame)
    inner_frame.grid(row=1, column=0)

    # title label
    label_title = tk.Label(inner_frame, text="Please update the \nband's info", width=20, height=2, font=("Arial", 20, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 25), sticky="n")

    # name entry
    name_label = tk.Label(inner_frame, text="Updated band name", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    name_label.grid(row=1, column=0, columnspan=2, padx=10,pady=(25, 5), sticky="nsew")
    name_entry = tk.Entry(inner_frame, width=60)
    name_entry.grid(row=2, column=0, columnspan=2, padx=10,pady=(5, 15))

    # genre entry
    genre_label = tk.Label(inner_frame, text="Updated musical genre", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    genre_label.grid(row=3, column=0, columnspan=2, padx=10,pady=(10, 5), sticky="nsew")
    genre_entry = tk.Entry(inner_frame, width=60)
    genre_entry.grid(row=4, column=0, columnspan=2, padx=10,pady=(5, 20))

    # origin entry
    origin_label = tk.Label(inner_frame, text="Updated origin", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    origin_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    origin_entry = tk.Entry(inner_frame, width=60)
    origin_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 15))

    # description entry
    desc_label = tk.Label(inner_frame, text="Updated description", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    desc_label.grid(row=7, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    desc_entry = tk.Entry(inner_frame, width=60)
    desc_entry.grid(row=8, column=0, columnspan=2, padx=10, pady=(5, 15))


    # function to switch to Bands_admin page
    def switch_bandsAdmin():
        outer_frame.destroy()
        from Bands_admin import bandsAdmin_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        bandsAdmin_window(win)

    # function to execute the update
    def handle_update():
        new_name = name_entry.get()
        new_genre = genre_entry.get()
        new_origin = origin_entry.get()
        new_desc = desc_entry.get()

        updateBand(selected_band_id, new_name, new_genre, new_origin, new_desc)
        messagebox.showinfo("Confirmation", "You have updated the band's info.")
        switch_bandsAdmin()

    # Button to update the band's info
    btn_register = tk.Button(inner_frame, text="Update", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000", command=handle_update)
    btn_register.grid(row=11, column=0, pady=(20, 20))


    # Button to cancel
    btn_cancel = tk.Button(inner_frame, text="Cancel", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000", command=switch_bandsAdmin)
    btn_cancel.grid(row=11, column=1, pady=(20, 20))