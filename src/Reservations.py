import tkinter as tk
from tkinter import *
import mysql.connector

'''used both ChatGPT and official doc to learn how to connect to a database
   with Python and understand the basics of the mysql.connector library'''
def reservations_window():

    # connect to the database
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="festival_PythonDB"
    )

    cursor = connexion.cursor()
    cursor.execute('''
        SELECT reservations.id, reservations.date_reservation, visitors.first_name, visitors.last_name, concerts.name AS concert_title, concerts.date
        FROM reservations
        INNER JOIN visitors ON reservations.visitor_id = visitors.id
        INNER JOIN concerts ON reservations.concert_id = concerts.id'''
    )
    reservations = cursor.fetchall()
    print(reservations)

    # creating the window
    win = tk.Tk()
    win.title("Reservations")
    win.geometry("400x700")
    win.resizable(False, False)

    # title
    label_title = Label(text="Reservations", width=10, height=1, font=("Arial", 25, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, padx=10, pady=20, sticky="n")

    # frame
    blocks_frame = tk.Frame(win, bg="lightgray", bd=2, relief="groove")
    blocks_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # stretch frame horizontally and vertically to fill the window
    win.grid_rowconfigure(1, weight=1)
    win.grid_columnconfigure(0, weight=1)

    # example blocks
    for i, reservation in enumerate(reservations):
        res_id, date_res, first_name, last_name, concert_name, concert_date = reservation
        block = tk.Label(blocks_frame, text=f"{res_id} | Reservation date : {date_res}\nVisitor : {first_name} {last_name}\nConcert : {concert_name} | Date : {concert_date}", bg="white", bd=1, relief="solid", padx=10, pady=10)
        block.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

    # stretch the blocks horizontally inside the frame
    blocks_frame.grid_columnconfigure(0, weight=1)

    btn_return = tk.Button(win, text="Return to Home Page", font=("Arial", 12), fg="#000000")
    btn_return.grid(row=2, column=0, pady=20)

    win.mainloop()
    cursor.close()
    connexion.close()