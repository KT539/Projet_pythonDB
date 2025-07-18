# Project: PythonDB: HarmoniK Festival
# Title: update_Visitor.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 1.0, last modified:  10.06.2025

import tkinter as tk
from tkinter import messagebox
from DB_managment import updateVisitor


def updateVisitor_window(win, selected_visitor_id):

    win.title("Updating visitor account - " + win.username)

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
    label_title = tk.Label(inner_frame, text="Please update the \npersonal information", width=20, height=2, font=("Arial", 20, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(15, 55), sticky="n")

    # firstname entry
    fname_label = tk.Label(inner_frame, text="Updated first name", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    fname_label.grid(row=1, column=0, columnspan=2, padx=10,pady=(55, 5), sticky="nsew")
    fname_entry = tk.Entry(inner_frame, width=60)
    fname_entry.grid(row=2, column=0, columnspan=2, padx=10,pady=(5, 15))

    # lastname entry
    lname_label = tk.Label(inner_frame, text="Updated last name", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    lname_label.grid(row=3, column=0, columnspan=2, padx=10,pady=(10, 5), sticky="nsew")
    lname_entry = tk.Entry(inner_frame, width=60)
    lname_entry.grid(row=4, column=0, columnspan=2, padx=10,pady=(5, 20))

    # birthdate entry
    bdate_label = tk.Label(inner_frame, text="Updated birthdate (YYYY-MM-DD)", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    bdate_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    bdate_entry = tk.Entry(inner_frame, width=60)
    bdate_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 15))

    # email entry
    email_label = tk.Label(inner_frame, text="Updated email", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    email_label.grid(row=7, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    email_entry = tk.Entry(inner_frame, width=60)
    email_entry.grid(row=8, column=0, columnspan=2, padx=10, pady=(5, 15))


    # function to switch to visitors page
    def switch_visitors():
        outer_frame.destroy()
        from Visitors import visitors_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        visitors_window(win)

    # Button to cancel
    btn_cancel = tk.Button(inner_frame, text="Cancel", width=10, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=switch_visitors)
    btn_cancel.grid(row=11, column=1, pady=(120, 10))


    def handle_update():

        new_fname = fname_entry.get()
        new_lname = lname_entry.get()
        new_bdate = bdate_entry.get()
        new_email = email_entry.get()

        updateVisitor(selected_visitor_id, new_fname, new_lname, new_bdate, new_email)
        messagebox.showinfo("Confirmation", "You have updated the visitor account.")
        switch_visitors()

    # Button to update the account
    btn_register = tk.Button(inner_frame, text="Update", width=10, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=handle_update)
    btn_register.grid(row=11, column=0, pady=(120, 10))
