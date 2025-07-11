# Project: PythonDB: HarmoniK Festival
# Title: add_Band.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 1.0, last modified:  10.06.2025

import tkinter as tk
from tkinter import messagebox
from DB_managment import newBand


def addBand_window(win):

    win.title("Adding a new band - " + win.username)

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
    label_title = tk.Label(inner_frame, text="Please enter the \nband's information", width=20, height=2, font=("Arial", 20, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 65), sticky="n")

    # band name entry
    bname_label = tk.Label(inner_frame, text="Enter the band's name", width=12, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    bname_label.grid(row=1, column=0, columnspan=2, padx=10,pady=(65, 5), sticky="nsew")
    bname_entry = tk.Entry(inner_frame, width=60)
    bname_entry.grid(row=2, column=0, columnspan=2, padx=10,pady=(5, 10))

    # band genre entry
    bgenre_label = tk.Label(inner_frame, text="Enter the band's genre", width=12, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    bgenre_label.grid(row=3, column=0, columnspan=2, padx=10,pady=(10, 5), sticky="nsew")
    bgenre_entry = tk.Entry(inner_frame, width=60)
    bgenre_entry.grid(row=4, column=0, columnspan=2, padx=10,pady=(5, 10))

    # band origin entry
    borigin_label = tk.Label(inner_frame, text="Enter the band's origin", width=12, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    borigin_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    borigin_entry = tk.Entry(inner_frame, width=60)
    borigin_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 10))

    # scene nb entry
    bdesc_label = tk.Label(inner_frame, text="Enter the band's description", width=12, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    bdesc_label.grid(row=7, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    bdesc_entry = tk.Entry(inner_frame, width=60)
    bdesc_entry.grid(row=8, column=0, columnspan=2, padx=10, pady=(5, 70))


    # function to switch to Bands window
    def switch_Bands():
        outer_frame.destroy()
        from Bands import bands_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        bands_window(win)

    # function to handle adding a new band
    def handle_newBand():
        band_name = bname_entry.get().strip()
        band_genre = bgenre_entry.get().strip()
        band_origin = borigin_entry.get().strip()
        band_description = bdesc_entry.get().strip()

        newBand(band_name, band_genre, band_origin, band_description)
        messagebox.showinfo("Confirmation", "You have added a new band.")
        switch_Bands()


    # Button to add the band
    btn_cadd = tk.Button(inner_frame, text="Add new band", width=15, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=handle_newBand)
    btn_cadd.grid(row=13, column=0, pady=(60, 10))

    # Button to cancel
    btn_cancel = tk.Button(inner_frame, text="Cancel", width=15, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=switch_Bands)
    btn_cancel.grid(row=13, column=1, pady=(60, 10))