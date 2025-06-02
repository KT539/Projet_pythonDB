# Project: PythonDB
# Title: Bands.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
from DB_managment import bands_requests, get_admin_status, deleteBand
from tkinter import messagebox


def bands_window(win):

    win.title("Bands - " + win.username)
    admin_status = get_admin_status(win.email)

    selected_band = None
    selected_band_id = None

    # create an outer frame
    outer_frame = tk.Frame(win)
    outer_frame.grid(row=0, column=0, sticky="nsew")

    # title label
    label_title = tk.Label(outer_frame, text="Bands", width=10, height=1, font=("Arial", 25, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="n")

    # embed the canvas and scrollbar in the outer frame
    canvas = tk.Canvas(outer_frame, width=360, height=535)
    scrollbar = tk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky="ns")
    canvas.grid(row=1, column=0, sticky="nsew", padx=5, pady=10)

    # make the outer frame resizable
    outer_frame.grid_rowconfigure(1, weight=1)
    outer_frame.grid_columnconfigure(0, weight=1)

    if admin_status == 1 :
        # create a frame for bottom buttons
        buttons_frame = tk.Frame(outer_frame)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

        def switch_addBand():
            outer_frame.destroy()
            from addBand import addBand_window
            addBand_window(win)

        def handle_delete():
            nonlocal selected_band_id
            if selected_band_id is None:
                messagebox.showwarning("Warning", "No band selected.")
            else:
                deleteBand(selected_band_id)
                messagebox.showinfo("Confirmation", "You have deleted a band.")
                outer_frame.destroy()
                bands_window(win)

        # add a new band button
        btn_add = tk.Button(buttons_frame, text="Add a band", font=("Arial", 12), fg="#000000", command=switch_addBand)
        btn_add.grid(row=0, column=0, padx=5, pady=(5, 15))

        # delete a band button
        btn_del = tk.Button(buttons_frame, text="Delete a band", font=("Arial", 12), fg="#000000", command=handle_delete)
        btn_del.grid(row=0, column=1, padx=5, pady=(5, 15))

        # function to switch to update_Band page
        def switch_updateBand():
            if selected_band_id is None:
                messagebox.showwarning("Warning", "No band selected.")
            else:
                outer_frame.destroy()
                from update_Band import updateBand_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
                updateBand_window(win, selected_band_id)

        # update a band button
        btn_updt = tk.Button(buttons_frame, text="Update a band", font=("Arial", 12), fg="#000000", command=switch_updateBand)
        btn_updt.grid(row=1, column=0, columnspan=2, padx=5, pady=(5, 15))

        def select_band(widget, bnd_id):
            nonlocal selected_band, selected_band_id  # changed global to nonlocal on ChatGPT's suggestion
            # deselect a widget on click
            if widget == selected_band:
                widget.config(bg="white")
                selected_band = None
                selected_band_id = None
            else:
                # Deselect the previously selected widget
                if selected_band is not None:
                    selected_band.config(bg="white")

                # Select the new widget
                widget.config(bg="lightgray")
                selected_band = widget
                selected_band_id = bnd_id

    # embed an inner frame in the canvas
    inner_frame = tk.Frame(canvas, bg="lightgray", bd=2, relief="groove")
    canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    bands = bands_requests()

    # put the widgets in the inner frame
    for i, band in enumerate(bands):  # loop structure from ChatGPT
        band_id, band_name, band_genre, band_desc, band_origin = band
        widgets = tk.Label(inner_frame, text=f"{band_id} | Band Name : {band_name} | Origin : {band_origin}\nGenre : {band_genre}\nDescription : {band_desc} ", bg="white", bd=1, relief="solid", padx=10, pady=10)
        widgets.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

        if admin_status == 1:
            # Bind the click event, taken from ChatGPT
            widgets.bind("<Button-1>", lambda event, w=widgets, bid=band_id: select_band(w, bid))

    # stretch the blocks horizontally inside the frame
    inner_frame.grid_columnconfigure(0, weight=1)

    # update the scrollregion
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", update_scrollregion)

    # adjust widgets dynamic width
    def resize_inner_frame(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize_inner_frame)

    # function to switch to Home page
    def switch_Homepage():
        outer_frame.destroy()
        from Homepage_test import homepage_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepage_window(win)

    # return to HomePage button
    btn_return = tk.Button(outer_frame if admin_status == 0 else buttons_frame, text="Return to Home Page", font=("Arial", 12), fg="#000000", command=switch_Homepage)
    btn_return.grid(row=2, column=0, columnspan=2, pady=20 if admin_status == 0 else 10)