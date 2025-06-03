# Project: PythonDB
# Title: addConcert.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
from tkinter import messagebox
from DB_managment import newConcert

def addConcert_window(win):

    win.title("Adding a new concert - " + win.username)

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
    label_title = tk.Label(inner_frame, text="Please enter the \nconcert's details", width=20, height=2, font=("Arial", 20, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 30), sticky="n")

    # concert name entry
    cname_label = tk.Label(inner_frame, text="Enter the concert's name", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    cname_label.grid(row=1, column=0, columnspan=2, padx=10,pady=(30, 5), sticky="nsew")
    cname_entry = tk.Entry(inner_frame, width=60)
    cname_entry.grid(row=2, column=0, columnspan=2, padx=10,pady=(5, 10))

    # concert date entry
    cdate_label = tk.Label(inner_frame, text="Enter the concert's date (YYYY-MM-DD HH:MM:SS)", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    cdate_label.grid(row=3, column=0, columnspan=2, padx=10,pady=(10, 5), sticky="nsew")
    cdate_entry = tk.Entry(inner_frame, width=60)
    cdate_entry.grid(row=4, column=0, columnspan=2, padx=10,pady=(5, 10))

    # concert price entry
    price_label = tk.Label(inner_frame, text="Enter the concert's price", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    price_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    price_entry = tk.Entry(inner_frame, width=60)
    price_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 10))

    # scene nb entry
    scene_label = tk.Label(inner_frame, text="Enter the concert's scene number", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    scene_label.grid(row=7, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    scene_entry = tk.Entry(inner_frame, width=60)
    scene_entry.grid(row=8, column=0, columnspan=2, padx=10, pady=(5, 10))

    # max capacity entry
    mcap_label = tk.Label(inner_frame, text="Enter the concert's maximum capacity", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    mcap_label.grid(row=9, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    mcap_entry = tk.Entry(inner_frame, width=60)
    mcap_entry.grid(row=10, column=0, columnspan=2, padx=10, pady=(5, 10))

    # band_id entry
    bndid_label = tk.Label(inner_frame, text="Enter performing band's ID number", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    bndid_label.grid(row=11, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    bndid_entry = tk.Entry(inner_frame, width=60)
    bndid_entry.grid(row=12, column=0, columnspan=2, padx=10, pady=(5, 10))

    # function to switch to Concerts_admin page
    def switch_Concerts():
        outer_frame.destroy()
        from Concerts import concerts_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        concerts_window(win)

    #function to handle adding a new concert
    def handle_newConcert():
        concert_name = cname_entry.get().strip()
        concert_date = cdate_entry.get().strip()
        concert_price = price_entry.get().strip()
        scene_number = scene_entry.get().strip()
        max_capacity = mcap_entry.get().strip()
        band_id = bndid_entry.get().strip()

        newConcert(concert_name, concert_date, concert_price, scene_number, max_capacity, band_id)
        messagebox.showinfo("Confirmation", "You have added a new concert.")
        switch_Concerts()

    # Button to add the concert
    btn_cadd = tk.Button(inner_frame, text="Add new concert", width=15, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=handle_newConcert)
    btn_cadd.grid(row=13, column=0, pady=(45, 5))

    # Button to cancel
    btn_cancel = tk.Button(inner_frame, text="Cancel", width=15, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=switch_Concerts)
    btn_cancel.grid(row=13, column=1, pady=(45, 5))