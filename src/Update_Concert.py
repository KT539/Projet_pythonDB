# Project: PythonDB
# Title: update_Visitor.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
from tkinter import messagebox
from DB_managment import updateConcert


def updateConcert_window(win, selected_concert_id):

    win.title("Updating concert  - " + win.username)

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
    label_title = tk.Label(inner_frame, text="Please update the \nconcert information", width=20, height=2, font=("Arial", 20, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 25), sticky="n")

    # name entry
    name_label = tk.Label(inner_frame, text="Updated name", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    name_label.grid(row=1, column=0, columnspan=2, padx=10,pady=(25, 5), sticky="nsew")
    name_entry = tk.Entry(inner_frame, width=60)
    name_entry.grid(row=2, column=0, columnspan=2, padx=10,pady=(5, 15))

    # date entry
    date_label = tk.Label(inner_frame, text="Updated date (YYYY-MM-DD)", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    date_label.grid(row=3, column=0, columnspan=2, padx=10,pady=(10, 5), sticky="nsew")
    date_entry = tk.Entry(inner_frame, width=60)
    date_entry.grid(row=4, column=0, columnspan=2, padx=10,pady=(5, 20))

    # price entry
    price_label = tk.Label(inner_frame, text="Updated price)", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    price_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    price_entry = tk.Entry(inner_frame, width=60)
    price_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 15))

    # scene number entry
    snmbr_label = tk.Label(inner_frame, text="Updated scene number", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    snmbr_label.grid(row=7, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    snmbr_entry = tk.Entry(inner_frame, width=60)
    snmbr_entry.grid(row=8, column=0, columnspan=2, padx=10, pady=(5, 15))

    # max_capacity entry
    capacity_label = tk.Label(inner_frame, text="Updated maximum capacity", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    capacity_label.grid(row=9, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    capacity_entry = tk.Entry(inner_frame, width=60)
    capacity_entry.grid(row=10, column=0, columnspan=2, padx=10, pady=(5, 15))

    # band_id entry
    band_label = tk.Label(inner_frame, text="Updated band id", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    band_label.grid(row=11, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    band_entry = tk.Entry(inner_frame, width=60)
    band_entry.grid(row=12, column=0, columnspan=2, padx=10, pady=(5, 15))

    # function to switch to Concerts_admin page
    def switch_concertsAdmin():
        outer_frame.destroy()
        from Concerts_admin import concertsAdmin_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        concertsAdmin_window(win)

    def handle_update():
        new_name = name_entry.get()
        new_date = date_entry.get()
        new_price = price_entry.get()
        new_snmbr = snmbr_entry.get()
        new_capacity = capacity_entry.get()
        new_band = band_entry.get()

        # Check if any field is empty
        if not all([new_name, new_date, new_price, new_snmbr, new_capacity, new_band]):
            messagebox.showwarning("Missing Information", "Please fill in all fields!")
            return

        # (Optional) Check if numeric fields are valid
        try:
            float(new_price)
            int(new_snmbr)
            int(new_capacity)
            int(new_band)
        except ValueError:
            messagebox.showerror("Invalid Input",
                                 "Price must be a number. Scene number, capacity, and band ID must be integers.")
            return

        updateConcert(selected_concert_id, new_name, new_date, new_price, new_snmbr, new_capacity, new_band)
        messagebox.showinfo("Confirmation", "You have updated the concert.")
        switch_concertsAdmin()

    # Button to update the account
    btn_register = tk.Button(inner_frame, text="Update", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000", command=handle_update)
    btn_register.grid(row=13, column=0, pady=(20, 20))

    # Button to cancel
    btn_cancel = tk.Button(inner_frame, text="Cancel", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000", command=switch_concertsAdmin)
    btn_cancel.grid(row=13, column=1, pady=(20, 20))