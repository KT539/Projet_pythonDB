import tkinter as tk
from tkinter import messagebox


def register_window(win):

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
    label_title = tk.Label(inner_frame, text="Please enter your \npersonal information", width=20, height=2, font=("Arial", 20, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 25), sticky="n")

    # firstname entry
    fname_label = tk.Label(inner_frame, text="Enter your first name *", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    fname_label.grid(row=1, column=0, columnspan=2, padx=10,pady=(25, 5), sticky="nsew")
    fname_entry = tk.Entry(inner_frame, width=60)
    fname_entry.grid(row=2, column=0, columnspan=2, padx=10,pady=(5, 15))

    # lastname entry
    lname_label = tk.Label(inner_frame, text="Enter your last name *", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    lname_label.grid(row=3, column=0, columnspan=2, padx=10,pady=(10, 5), sticky="nsew")
    lname_entry = tk.Entry(inner_frame, width=60)
    lname_entry.grid(row=4, column=0, columnspan=2, padx=10,pady=(5, 20))

    # birthdate entry
    bdate_label = tk.Label(inner_frame, text="Enter your birthdate (YYYY-MM-DD)", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    bdate_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    bdate_entry = tk.Entry(inner_frame, width=60)
    bdate_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 15))

    # email entry
    email_label = tk.Label(inner_frame, text="Enter your email *", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    email_label.grid(row=7, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    email_entry = tk.Entry(inner_frame, width=60)
    email_entry.grid(row=8, column=0, columnspan=2, padx=10, pady=(5, 15))

    # password entry
    pword_label = tk.Label(inner_frame, text="Enter your password *", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    pword_label.grid(row=9, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")
    pword_entry = tk.Entry(inner_frame, width=60, show="*")
    pword_entry.grid(row=10, column=0, columnspan=2, padx=10, pady=(5, 15))


    # Button to register
    btn_register = tk.Button(inner_frame, text="Register", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    btn_register.grid(row=11, column=0, pady=(20, 20))

    # function to switch to registration page
    def switch_login():
        outer_frame.destroy()
        from Login import login_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        login_window(win)

    # Button to cancel
    btn_cancel = tk.Button(inner_frame, text="Cancel", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000", command=switch_login)
    btn_cancel.grid(row=11, column=1, pady=(20, 20))

    # required fields label
    rf_label = tk.Label(inner_frame, text="Fields marked with an * \nare mandatory", width=20, height=2, font=("Arial", 10), fg="#000000")
    rf_label.grid(row=12, column=0, columnspan=2, padx=10, pady=(15, 15), sticky="n")