# Project: PythonDB: HarmoniK Festival
# Title: Visitors_admin.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 1.0, last modified:  10.06.2025

import tkinter as tk
from tkinter import messagebox
from DB_managment import visitors_requests, deleteVisitor
from src.DB_managment import deleteVisReservation

'''used both ChatGPT and official doc to learn how to connect to a database
   with Python and understand the basics of the mysql.connector library'''
def visitors_window(win):

    win.title("Visitors - " + win.username)

    selected_visitor = None
    selected_visitor_id = None

    # create an outer frame
    outer_frame = tk.Frame(win)
    outer_frame.grid(row=0, column=0, sticky="nsew")

    # title label
    label_title = tk.Label(outer_frame, text="Visitors", width=10, height=1, font=("Arial", 25, "bold"), fg="#000000")
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

    # create a frame for bottom buttons
    buttons_frame = tk.Frame(outer_frame)
    buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

    def handle_delete():
        nonlocal selected_visitor_id
        if selected_visitor_id is None:
            messagebox.showwarning("Warning", "No visitor selected.")
        else:
            deleteVisReservation(selected_visitor_id)
            deleteVisitor(selected_visitor_id)
            messagebox.showinfo("Confirmation", "You have deleted a visitor account.")
            outer_frame.destroy()
            visitors_window(win)

    def switch_updateVisitor():
        nonlocal selected_visitor_id

        if selected_visitor_id is None:
            messagebox.showwarning("Warning", "No visitor selected.")
        else:
            outer_frame.destroy()
            from update_Visitor import updateVisitor_window # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
            updateVisitor_window(win, selected_visitor_id)

    # update a visitor  button
    btn_update = tk.Button(buttons_frame, text="Update a visitor", font=("Arial", 12), width=13, fg="#000000", command=switch_updateVisitor)
    btn_update.grid(row=0, column=0, padx=5, pady=(5, 15))

    # delete a visitor button
    btn_del = tk.Button(buttons_frame, text="Delete a visitor", font=("Arial", 12), width=13, fg="#000000", command=handle_delete)
    btn_del.grid(row=0, column=1, padx=5, pady=(5, 15))

    # function to switch to Home page
    def switch_Homepage():
        outer_frame.destroy()
        from Homepage import homepage_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepage_window(win)

    # return to HomePage button
    btn_return = tk.Button(buttons_frame, text="Return to Home Page", font=("Arial", 12), fg="#000000", command=switch_Homepage)
    btn_return.grid(row=1, column=0, columnspan=2, pady=10)


    # embed an inner frame in the canvas
    inner_frame = tk.Frame(canvas, bg="lightgray", bd=2, relief="groove")
    canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    visitors = visitors_requests()

    # put the widgets in the inner frame
    for i, visitor in enumerate(visitors): # loop structure from ChatGPT
        vis_id, vis_first_name, vis_last_name, vis_birthdate, vis_email = visitor
        widgets = tk.Button(inner_frame, text=f"{vis_id} | Name : {vis_first_name} {vis_last_name}\nBirthdate : {vis_birthdate}\nEmail : {vis_email}", bg="white", bd=1, relief="solid", padx=10, pady=10)
        widgets.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

        # Bind the click event, taken from ChatGPT
        widgets.bind("<Button-1>", lambda event, w=widgets, vid=vis_id: select_visitor(w, vid))

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

    def select_visitor(widget, vis_id):
        nonlocal selected_visitor, selected_visitor_id # changed global to nonlocal on ChatGPT's suggestion
        # deselect a widget on click
        if widget == selected_visitor:
            widget.config(bg="white")
            selected_visitor = None
            selected_visitor_id = None
        else:
            # Deselect the previously selected widget
            if selected_visitor is not None:
                selected_visitor.config(bg="white")

            # Select the new widget
            widget.config(bg="lightgray")
            selected_visitor = widget
            selected_visitor_id = vis_id