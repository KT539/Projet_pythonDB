import tkinter as tk
from tkinter import messagebox


def deleteReservation_window(win):

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
    label_title = tk.Label(inner_frame, text="Delete a reservation", width=20, height=1, font=("Arial", 20, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, padx=10, pady=(10, 60), sticky="n")

    # instructions label
    label_instruction = tk.Label(inner_frame, text="Please enter the n° of the \nreservation you wish to delete", width=25, height=2, font=("Arial", 15), fg="#000000")
    label_instruction.grid(row=1, column=0, padx=10, pady=(60, 20), sticky="n")

    # concert name entry
    cname_label = tk.Label(inner_frame, text="Reservation n°", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    cname_label.grid(row=2, column=0, padx=10,pady=(30, 5), sticky="nsew")
    cname_entry = tk.Entry(inner_frame, width=60)
    cname_entry.grid(row=3, column=0, padx=10,pady=(5, 50))


    # Button to confirm the reservation
    btn_confirm = tk.Button(inner_frame, text="Delete my reservation", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    btn_confirm.grid(row=4, column=0, pady=(50, 10))

    # function to switch to registration page
    def switch_concerts():
        outer_frame.destroy()
        from Concerts import concerts_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        concerts_window(win)

    # Button to cancel
    btn_cancel = tk.Button(inner_frame, text="Cancel", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000", command=switch_concerts)
    btn_cancel.grid(row=5, column=0, pady=(10, 130))