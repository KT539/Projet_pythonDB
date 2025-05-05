import tkinter as tk
from tkinter import *



# Creating the window
win = tk.Tk()
win.title("Login / Register")
win.geometry("400x700")
win.resizable(False, False)

# create an outer frame
outer_frame = tk.Frame(win)
outer_frame.grid(row=0, column=0, sticky="nsew")

# Title
label_title = tk.Label(outer_frame,text="Login", width=10, height=1, font=("Arial", 30), bg="#FFFFFF", fg="#000000")
label_title.grid(row=0, column=0, columnspan=2,padx=80,pady=20, sticky="nsew")

# Email entry
email_label = tk.Label(outer_frame, text="Enter your email", width=15, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
email_label.grid(row=1, column=0, columnspan=2,padx=10,pady=20, sticky="nsew")
email_entry = tk.Entry(outer_frame, width=40)
email_entry.grid(row=2, column=0, columnspan=2,padx=10,pady=20)

# Password entry
password_label = tk.Label(outer_frame, text="Enter your password", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
password_label.grid(row=3, column=0, columnspan=2,padx=10,pady=20)
password_entry = tk.Entry(outer_frame, width=40)
password_entry.grid(row=4, column=0, columnspan=2,padx=10,pady=20)

# Button to log in
btn_login = tk.Button(outer_frame, text="Log in", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_login.grid(row=5, column=0, columnspan=2,padx=10,pady=20)

# Button to register
btn_register = tk.Button(outer_frame, text="Register", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
btn_register.grid(row=6, column=0, columnspan=2,padx=10,pady=20)

win.mainloop()
