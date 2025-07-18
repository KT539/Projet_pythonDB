# Project: PythonDB: HarmoniK Festival
# Title: Reservations.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 1.0, last modified:  10.06.2025

import tkinter as tk
from tkinter import messagebox
from DB_managment import reservations_requests, reservationsAdmin_requests, deleteReservation, get_admin_status


'''used both ChatGPT and official doc to learn how to connect to a database
   with Python and understand the basics of the mysql.connector library'''
def reservations_window(win):

    win.title("Reservations - " + win.username)
    admin_status = get_admin_status(win.email)

    selected_reservation = None
    selected_reservation_id = None

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

    if admin_status == 0:
        # create a frame for bottom buttons
        buttons_frame = tk.Frame(outer_frame)
        buttons_frame.grid(row=2, column=0, pady=10)

        def handle_delete():
            nonlocal selected_reservation_id
            if selected_reservation_id is None:
                messagebox.showwarning("Warning", "No reservation selected.")
            else:
                deleteReservation(selected_reservation_id)
                messagebox.showinfo("Confirmation", "Your reservation has been cancelled.")
                outer_frame.destroy()
                reservations_window(win)

        # cancel a reservation button
        btn_cancel = tk.Button(buttons_frame, text="Cancel my reservation", font=("Arial", 12), width=18, fg="#000000", command=lambda: handle_delete())
        btn_cancel.grid(row=0, column=0, columnspan=2, padx=5, pady=(5, 20))

    # function to switch to Home page
    def switch_Homepage():
        outer_frame.destroy()
        from Homepage import homepage_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepage_window(win)

    # return to HomePage button
    btn_return = tk.Button(buttons_frame if admin_status == 0 else outer_frame, text="Return to Home Page", font=("Arial", 12), width=18, fg="#000000", command=switch_Homepage)
    btn_return.grid(row=1 if admin_status == 0 else 2, column=0, columnspan=2, pady=(10, 20))

    # embed an inner frame in the canvas
    inner_frame = tk.Frame(canvas, bg="lightgray", bd=2, relief="groove")
    canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    if admin_status == 0:
        reservations = reservations_requests(win.visitor_id)
    else:
        reservations = reservationsAdmin_requests()

    # put the widgets in the inner frame
    for i, reservation in enumerate(reservations):
        res_id, date_res, first_name, last_name, concert_name, concert_date = reservation
        widgets = tk.Button(inner_frame, text=f"{res_id} | Reservation date : {date_res}\nVisitor : {first_name} {last_name}\nConcert : {concert_name} | Date : {concert_date}", bg="white", bd=1, relief="solid", padx=10, pady=10)
        widgets.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

        if admin_status == 0:
            # Bind the click event, taken from ChatGPT
            widgets.bind("<Button-1>", lambda event, w=widgets, rid=res_id: select_reservation(w, rid))

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

    if admin_status == 0:
        def select_reservation(widget, res_id):
            nonlocal selected_reservation, selected_reservation_id
            # deselect a widget on click
            if widget == selected_reservation:
                widget.config(bg="white")
                selected_reservation = None
                selected_reservation_id = None
            else:
                # deselect the previously selected widget
                if selected_reservation is not None:
                    selected_reservation.config(bg="white")
                # select the new widget
                widget.config(bg="lightgray")
                selected_reservation = widget
                selected_reservation_id = res_id