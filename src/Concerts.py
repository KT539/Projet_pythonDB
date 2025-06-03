# Project: PythonDB
# Title: Concerts.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
from tkinter import messagebox
from DB_managment import concerts_requests, newReservation, get_admin_status, deleteConcert

'''used both ChatGPT and official doc to learn how to connect to a database
   with Python and understand the basics of the mysql.connector library'''
def concerts_window(win):

    win.title("Concerts - " + win.username)
    admin_status = get_admin_status(win.email)

    selected_concert = None
    selected_concert_id = None

    # create an outer frame
    outer_frame = tk.Frame(win)
    outer_frame.grid(row=0, column=0, sticky="nsew")

    # title label
    label_title = tk.Label(outer_frame, text="Concerts", width=10, height=1, font=("Arial", 25, "bold"), fg="#000000")
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

    # create a frame for bottom buttons
    buttons_frame = tk.Frame(outer_frame)
    buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

    if admin_status == 1:
        def switch_addConcert():
            outer_frame.destroy()
            from add_Concert import addConcert_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
            addConcert_window(win)

        def handle_delete():
            nonlocal selected_concert_id
            if selected_concert_id is None:
                messagebox.showwarning("Warning", "No concert selected.")
            else:
                deleteConcert(selected_concert_id)
                messagebox.showinfo("Confirmation", "You have deleted a concert.")
                outer_frame.destroy()
                concerts_window(win)

        # add a new concert button
        btn_add = tk.Button(buttons_frame, text="Add a concert", font=("Arial", 12), fg="#000000", command=switch_addConcert)
        btn_add.grid(row=0, column=0, padx=5, pady=(5, 15))

        # delete a concert button
        btn_del = tk.Button(buttons_frame, text="Delete a concert", font=("Arial", 12), fg="#000000", command=handle_delete)
        btn_del.grid(row=0, column=1, padx=5, pady=(5, 15))

        # function to switch to updateConcert
        def switch_update_concert():
            if selected_concert_id is None:
                messagebox.showwarning("Warning", "No concert selected.")
            else:
                outer_frame.destroy()
                from Update_Concert import updateConcert_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
                updateConcert_window(win, selected_concert_id)

        # update a concert button
        btn_update = tk.Button(buttons_frame, text="Update a concert", font=("Arial", 12), fg="#000000", command=switch_update_concert)
        btn_update.grid(row=1, column=0, columnspan=2, padx=5, pady=(5, 15))

    else:
        def handle_newReservation():
            nonlocal selected_concert_id
            if selected_concert_id is None:
                messagebox.showwarning("Warning", "No concert selected.")

            else:
                from DB_managment import newReservation
                success = newReservation(selected_concert_id, win.visitor_id)
                if success:
                    messagebox.showinfo("Confirmation", "You have made a new reservation.")
                    outer_frame.destroy()
                    concerts_window(win)
                else:
                    messagebox.showwarning("Warning", "You have already reserved this concert.")

        # make a reservation button
        btn_res = tk.Button(buttons_frame, text="Make a reservation", font=("Arial", 12), fg="#000000", command=lambda: handle_newReservation())
        btn_res.grid(row=0, column=0, columnspan=2, padx=5, pady=(5, 15))

    # function to switch to Home page
    def switch_Homepage():
        outer_frame.destroy()
        from Homepage import homepage_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepage_window(win)

    # return to HomePage button
    btn_return = tk.Button(buttons_frame, text="Return to Home Page", font=("Arial", 12), fg="#000000", command=switch_Homepage)
    btn_return.grid(row=2 if admin_status == 1 else 1, column=0, columnspan=2, pady=10)

    # embed an inner frame in the canvas
    inner_frame = tk.Frame(canvas, bg="lightgray", bd=2, relief="groove")
    canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    concerts = concerts_requests()

    # put the widgets in the inner frame
    for i, concert in enumerate(concerts):  # loop structure from ChatGPT
        cnrt_id, cnrt_name, cnrt_date, cnrt_scene = concert
        widgets = tk.Button(inner_frame, text=f"{cnrt_id} | Concert name : {cnrt_name}\nConcert date : {cnrt_date}\nLocation : scene n° {cnrt_scene}", bg="white", bd=1, relief="solid", padx=10, pady=10)
        widgets.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

        # Bind the click event, taken from ChatGPT
        widgets.bind("<Button-1>", lambda event, w=widgets, cid=cnrt_id: select_concert(w, cid))

    # stretch the widgets horizontally inside the frame
    inner_frame.grid_columnconfigure(0, weight=1)

    # update the scrollregion
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", update_scrollregion)

    # adjust widgets dynamic width
    def resize_inner_frame(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize_inner_frame)

    def select_concert(widget, cnrt_id):
        nonlocal selected_concert, selected_concert_id  # changed global to nonlocal on ChatGPT's suggestion
        # deselect a widget on click
        if widget == selected_concert:
            widget.config(bg="white")
            selected_concert = None
            selected_concert_id = None
        else:
            # Deselect the previously selected widget
            if selected_concert is not None:
                selected_concert.config(bg="white")

            # Select the new widget
            widget.config(bg="lightgray")
            selected_concert = widget
            selected_concert_id = cnrt_id