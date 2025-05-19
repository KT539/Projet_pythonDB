# Project: PythonDB
# Title: HomePage.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
from PIL import Image, ImageTk
from Reservations import reservations_window
from Concerts import concerts_window
from Bands import bands_window
from Login import login_window

def homepage_window(win):

    win.title("Home - " + win.username)

    image_path = ".//background_img.png"
    img = Image.open(image_path)
    img = img.resize((300, 200))
    tk_img = ImageTk.PhotoImage(img)

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
    label_title = tk.Label(inner_frame, text="Home", width=10, height=1, font=("Arial", 25, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, padx=10, pady=(20, 40), sticky="n")

    # homePage image
    hp_image = tk.Label(inner_frame, image=tk_img)
    hp_image.image = tk_img
    hp_image.grid(row=1, column=0, pady=(10, 60))


    # function to switch to reservations page
    def switch_reservations():
        outer_frame.destroy()
        reservations_window(win)

    # button to see all reservations
    btn_reservations = tk.Button(inner_frame, text="Reservations", font=("Arial", 15), width=20, command=switch_reservations)
    btn_reservations.grid(row=2, column=0, pady=10)

    # function to switch to concerts page
    def switch_concerts():
        outer_frame.destroy()
        concerts_window(win)

    # button to see all concerts
    btn_concerts = tk.Button(inner_frame, text="Concerts", font=("Arial", 15), width=20, command=switch_concerts)
    btn_concerts.grid(row=3, column=0, pady=10)

    # function to switch to bands page
    def switch_bands():
        outer_frame.destroy()
        bands_window(win)

    # button to see all bands
    btn_bands = tk.Button(inner_frame, text="Bands", font=("Arial", 15), width=20, command=switch_bands)
    btn_bands.grid(row=4, column=0, pady=10)

    # function to switch to login page
    def switch_login():
        outer_frame.destroy()
        login_window(win)

    # logout button
    btn_logout = tk.Button(inner_frame, text="Log out", font=("Arial", 15), width=20, command=switch_login)
    btn_logout.grid(row=5, column=0, pady=(65, 30))