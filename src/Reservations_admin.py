# Project: PythonDB
# Title: Reservations.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.1, last modified:  01.05.2025

import tkinter as tk

from DB_managment import reservationsAdmin_requests


'''used both ChatGPT and official doc to learn how to connect to a database
   with Python and understand the basics of the mysql.connector library'''
def reservationsAdmin_window(win):

    # create an outer frame
    outer_frame = tk.Frame(win)
    outer_frame.grid(row=0, column=0, sticky="nsew")

    # title label
    label_title = tk.Label(outer_frame, text="Reservations", width=10, height=1, font=("Arial", 25, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="n")

    # embed the canvas and scrollbar in the outer frame
    canvas = tk.Canvas(outer_frame, width=360, height=535)
    scrollbar = tk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky="ns")
    canvas.grid(row=1, column=0, sticky="nsew", padx=5, pady=10)

    # make the outer frame expandable
    outer_frame.grid_rowconfigure(1, weight=1)
    outer_frame.grid_columnconfigure(0, weight=1)

    # function to switch to Home page
    def switch_HomePage_admin():
        outer_frame.destroy()
        from HomePage_admin import homepageAdmin_window # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepageAdmin_window(win)

    # return to HomePage button
    btn_return = tk.Button(outer_frame, text="Return to Home Page", font=("Arial", 12), fg="#000000", command=switch_HomePage_admin)
    btn_return.grid(row=2, column=0, columnspan=2, pady=10)

    # embed an inner frame in the canvas
    inner_frame = tk.Frame(canvas, bg="lightgray", bd=2, relief="groove")
    canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    reservations = reservationsAdmin_requests()

    # put the widgets in the inner frame
    for i, reservation in enumerate(reservations): # loop structure from ChatGPT
        res_id, date_res, first_name, last_name, concert_name, concert_date = reservation
        widgets = tk.Button(inner_frame, text=f"{res_id} | Reservation date : {date_res}\nVisitor : {first_name} {last_name}\nConcert : {concert_name} | Date : {concert_date}", bg="white", bd=1, relief="solid", padx=10, pady=10)
        widgets.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

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