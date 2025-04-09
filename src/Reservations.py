import tkinter as tk
from tkinter import *

# creating the window
win = tk.Tk()
win.title("Reservations")
win.geometry("400x700")

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
for i in range(5):
    block = tk.Label(blocks_frame, text=f"Reservation {i+1}", bg="white", bd=1, relief="solid", padx=10, pady=10)
    block.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

# stretch the blocks horizontally inside the frame
blocks_frame.grid_columnconfigure(0, weight=1)

win.mainloop()