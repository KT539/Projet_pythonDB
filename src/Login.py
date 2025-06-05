# Project: PythonDB
# Title: Login.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
import hashlib
from tkinter import messagebox


def login_window(win):

    win.title("Login")

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
    label_title = tk.Label(inner_frame, text="HarmoniK Festival \nLogin", width=15, height=2, font=("Arial", 25, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, padx=10, pady=(20, 50), sticky="n")

    # Email entry
    email_label = tk.Label(inner_frame, text="Enter your email", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    email_label.grid(row=1, column=0, padx=10,pady=(40, 5), sticky="nsew")
    email_entry = tk.Entry(inner_frame, width=60)
    email_entry.grid(row=2, column=0, padx=10,pady=(5, 30))

    # Password entry
    password_label = tk.Label(inner_frame, text="Enter your password", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    password_label.grid(row=3, column=0, padx=10,pady=(25, 5), sticky="nsew")
    password_entry = tk.Entry(inner_frame, width=60, show="*")
    password_entry.grid(row=4, column=0, padx=10,pady=(5, 10))

    # function to switch to Home page
    def switch_Homepage_test():
        outer_frame.destroy()
        from Homepage import homepage_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepage_window(win)

    # function to check the login credentials and make the switch
    def check_login():
        email = email_entry.get()
        password = password_entry.get()
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        from DB_managment import login_request, get_visitor_id, get_username
        if login_request(email, password_hash):
            win.visitor_id = get_visitor_id(email)
            win.username = get_username(email)
            win.email = email
            switch_Homepage_test()
        else:
            messagebox.showerror("Error", "Invalid credentials, please try again.")

    # function to switch to updatePassword page
    def switch_updatePassword():
        outer_frame.destroy()
        from update_Password import updatePassword_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        updatePassword_window(win)

    # button to modify password
    btn_update_pswd = tk.Button(inner_frame, text="I forgot my password", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=switch_updatePassword)
    btn_update_pswd.grid(row=5, column=0, padx=10, pady=(5, 40))

    # Button to log in
    btn_login = tk.Button(inner_frame, text="Sign in", width=10, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=check_login)
    btn_login.grid(row=6, column=0, padx=10, pady=(20, 50))

    # registration label
    label_registration = tk.Label(inner_frame, text="Not registered yet ?", width=15, height=1, font=("Arial", 12), fg="#000000")
    label_registration.grid(row=7, column=0, padx=10, pady=(40, 10), sticky="n")

    # function to switch to registration page
    def switch_register():
        outer_frame.destroy()
        from Register import register_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        register_window(win)

    # Button to register
    btn_register = tk.Button(inner_frame, text="Sign up", width=10, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=switch_register)
    btn_register.grid(row=8, column=0, padx=10, pady=(10, 50))