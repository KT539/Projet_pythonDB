import tkinter as tk
from tkinter import messagebox


def login_window(win):

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
    label_title = tk.Label(inner_frame, text="Login", width=10, height=1, font=("Arial", 25, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, padx=10, pady=(10, 60), sticky="n")

    # Email entry
    email_label = tk.Label(inner_frame, text="Enter your email", width=15, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    email_label.grid(row=1, column=0, padx=10,pady=(50, 5), sticky="nsew")
    email_entry = tk.Entry(inner_frame, width=40)
    email_entry.grid(row=2, column=0, padx=10,pady=(5, 30))

    # Password entry
    password_label = tk.Label(inner_frame, text="Enter your password", width=20, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    password_label.grid(row=3, column=0, columnspan=2,padx=10,pady=5)
    password_entry = tk.Entry(inner_frame, width=40, show="*")
    password_entry.grid(row=4, column=0, padx=10,pady=(5, 30))

    # function to switch to admin Home page
    def switch_HomePage_admin():
        outer_frame.destroy()
        from HomePage_admin import homepageAdmin_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepageAdmin_window(win)

    # function to switch to Home page
    def switch_HomePage():
        outer_frame.destroy()
        from HomePage import homepage_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepage_window(win)

    # function to check the login credentials and make the switch
    def check_login():
        email = email_entry.get()
        password = password_entry.get()
        from DB_managment import loginAdmin_request
        from DB_managment import login_request
        if loginAdmin_request(email, password):
            switch_HomePage_admin()
        elif login_request(email, password):
            switch_HomePage()
        else:
            messagebox.showerror("Invalid credentials, please try again")

    # Button to log in
    btn_login = tk.Button(inner_frame, text="Sign in", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000", command=check_login)
    btn_login.grid(row=5, column=0, padx=10,pady=(20, 60))

    # registration label
    label_title = tk.Label(inner_frame, text="Not registered yet ?", width=20, height=1, font=("Arial", 15), fg="#000000")
    label_title.grid(row=6, column=0, padx=10, pady=(60, 10), sticky="n")

    # Button to register
    btn_register = tk.Button(inner_frame, text="Sign up", width=10, height=1, font=("Arial", 15), bg="#FFFFFF", fg="#000000")
    btn_register.grid(row=7, column=0, padx=10,pady=(10, 50))
