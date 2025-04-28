import tkinter as tk

def homepage_window():
    # creating the window
    win = tk.Tk()
    win.title("Home Page")
    win.geometry("400x700")
    win.resizable(False, False)

    # configuring the grid
    win.grid_rowconfigure(0, weight=1)
    win.grid_rowconfigure(1, weight=1)
    win.grid_rowconfigure(2, weight=1)
    win.grid_rowconfigure(3, weight=1)
    win.grid_rowconfigure(4, weight=1)
    win.grid_rowconfigure(5, weight=1)
    win.grid_rowconfigure(6, weight=1)

    win.grid_columnconfigure(0, weight=1)

    # Title
    label_title = tk.Label(win, text="Festival_Title", font=("Arial", 25, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, pady=(15, 0))

    # homePage image
    hp_image = tk.Label(win, text="Image", font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    hp_image.grid(row=1, column=0, pady=(10, 20))

    # button to see all concerts
    btn_concerts = tk.Button(win, text="Concerts", font=("Arial", 15), fg="#000000")
    btn_concerts.grid(row=2, column=0, pady=(5, 10))

    # button to see all bands
    btn_bands = tk.Button(win, text="Bands", font=("Arial", 15), fg="#000000")
    btn_bands.grid(row=3, column=0, pady=(5, 10))

    # button to see all reservations
    btn_myRes = tk.Button(win, text="Reservations", font=("Arial", 15), fg="#000000")
    btn_myRes.grid(row=4, column=0, pady=(5, 10))

    # login button
    btn_login = tk.Button(win, text="Log in / Register", font=("Arial", 15), fg="#000000")
    btn_login.grid(row=5, column=0, pady=(10, 10))

    win.mainloop()

homepage_window()