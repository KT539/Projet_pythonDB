import tkinter as tk
from Reservations import reservations_window
from Concerts import concerts_window
from Bands import bands_window

def homepage_window(win):

    # configure the main window
    win.grid_rowconfigure(0, weight=1)
    win.grid_columnconfigure(0, weight=1)

    # create an outer frame
    outer_frame = tk.Frame(win)
    outer_frame.grid(row=0, column=0, sticky="nsew")

    # create an inner frame
    inner_frame = tk.Frame(outer_frame)
    inner_frame.grid(row=0, column=0)

    # Title
    label_title = tk.Label(inner_frame, text="Home", font=("Arial", 25, "bold"))
    label_title.grid(row=0, column=0, pady=(30, 10))

    # homePage image
    hp_image = tk.Label(inner_frame, text="Background image", bg="#CCCCCC", width=30, height=10)
    hp_image.grid(row=1, column=0, pady=10)


    # function to switch to reservations page
    def switch_reservations():
        outer_frame.destroy()
        reservations_window(win)

    # button to see all reservations
    btn_reservations = tk.Button(inner_frame, text="Reservations", font=("Arial", 15), width=20, command=switch_reservations)
    btn_reservations.grid(row=2, column=0, pady=5)

    # function to switch to concerts page
    def switch_concerts():
        outer_frame.destroy()
        concerts_window(win)

    # button to see all concerts
    btn_concerts = tk.Button(inner_frame, text="Concerts", font=("Arial", 15), width=20, command=switch_concerts)
    btn_concerts.grid(row=3, column=0, pady=5)

    # function to switch to bands page
    def switch_bands():
        outer_frame.destroy()
        bands_window(win)

    # button to see all bands
    btn_bands = tk.Button(inner_frame, text="Bands", font=("Arial", 15), width=20, command=switch_bands)
    btn_bands.grid(row=4, column=0, pady=5)