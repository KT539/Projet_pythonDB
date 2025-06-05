# Project: PythonDB
# Title: update_Password.py
# Author: Kilian Testard + Ahmet Karabulut
# Version: 0.2, last modified:  19.05.2025

import tkinter as tk
from tkinter import messagebox
import hashlib
from DB_managment import updatePassword, get_visitor_id


def updatePassword_window(win):

    win.title("Forgotten password")

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
    label_title = tk.Label(inner_frame, text="Choose your new\npassword", width=20, height=2, font=("Arial", 20, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 75), sticky="n")

    # email entry
    email_label = tk.Label(inner_frame, text="Please enter your email", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    email_label.grid(row=1, column=0, columnspan=2, padx=10, pady=(30, 5), sticky="nsew")
    email_entry = tk.Entry(inner_frame, width=60)
    email_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 70))

    # password entry
    pswd_label = tk.Label(inner_frame, text="Please enter your new password", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    pswd_label.grid(row=3, column=0, columnspan=2, padx=10,pady=(20, 5), sticky="nsew")
    pswd_entry = tk.Entry(inner_frame, width=60, show="*")
    pswd_entry.grid(row=4, column=0, columnspan=2, padx=10,pady=(5, 15))

    # password confirmation
    pswdConf_label = tk.Label(inner_frame, text="Please confirm your new password", width=20, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
    pswdConf_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(15, 5), sticky="nsew")
    pswdConf_entry = tk.Entry(inner_frame, width=60, show="*")
    pswdConf_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 30))


    # function to switch to login page
    def switch_Login():
        outer_frame.destroy()
        from Login import login_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        login_window(win)

    def handle_update():
        email = email_entry.get().strip()
        visitor_id = get_visitor_id(email)
        new_pswd = pswd_entry.get().strip()
        new_pswd_hash = hashlib.sha256(new_pswd.encode('utf-8')).hexdigest()
        new_pswd_conf = pswdConf_entry.get().strip()

        # Check if the fields are filled in
        if not email or not new_pswd or not new_pswd_conf:
            messagebox.showerror("Error", "Please answer all entry fields.")
            return
        # Check if the account is valid
        elif visitor_id is None:
            messagebox.showerror("Error", "No account found with that email.")
        elif pswd_entry.get() == pswdConf_entry.get():
            updatePassword(new_pswd_hash, visitor_id)
            messagebox.showinfo("Confirmation", "You have set a new password.")
            outer_frame.destroy()
            switch_Login()
        else :
            messagebox.showerror("Error", "The passwords do not match.")
            return

    # Button to update the account
    btn_register = tk.Button(inner_frame, text="Update", width=10, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=handle_update)
    btn_register.grid(row=11, column=0, pady=(100, 20))

    # Button to cancel
    btn_cancel = tk.Button(inner_frame, text="Cancel", width=10, height=1, font=("Arial", 12), bg="#FFFFFF", fg="#000000", command=switch_Login)
    btn_cancel.grid(row=11, column=1, pady=(100, 20))