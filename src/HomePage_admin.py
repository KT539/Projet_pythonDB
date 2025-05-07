import tkinter as tk
from PIL import Image, ImageTk
from Reservations_admin import reservationsAdmin_window
from Concerts_admin import concertsAdmin_window
from Bands_admin import bandsAdmin_window
from Visitors_admin import visitorsAdmin_window

def homepageAdmin_window(win):

    image_path = ".//background_img_admin.png"
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
    hp_image.grid(row=1, column=0, pady=(10, 75))

    # function to switch to visitors page
    def switch_visitors_admin():
        outer_frame.destroy()
        visitorsAdmin_window(win)

    # button to see all visitors
    btn_visitors = tk.Button(inner_frame, text="Visitors", font=("Arial", 15), width=20, command=switch_visitors_admin)
    btn_visitors.grid(row=2, column=0, pady=10)

    # function to switch to reservations page
    def switch_reservations_admin():
        outer_frame.destroy()
        reservationsAdmin_window(win)

    # button to see all reservations
    btn_reservations = tk.Button(inner_frame, text="Reservations", font=("Arial", 15), width=20, command=switch_reservations_admin)
    btn_reservations.grid(row=3, column=0, pady=10)

    # function to switch to concerts page
    def switch_concerts_admin():
        outer_frame.destroy()
        concertsAdmin_window(win)

    # button to see all concerts
    btn_concerts = tk.Button(inner_frame, text="Concerts", font=("Arial", 15), width=20, command=switch_concerts_admin)
    btn_concerts.grid(row=4, column=0, pady=10)

    # function to switch to bands page
    def switch_bands_admin():
        outer_frame.destroy()
        bandsAdmin_window(win)

    # button to see all bands
    btn_bands = tk.Button(inner_frame, text="Bands", font=("Arial", 15), width=20, command=switch_bands_admin)
    btn_bands.grid(row=5, column=0, pady=(10, 125))