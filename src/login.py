import tkinter as tk
from tkinter import messagebox




# Main Window
root = tk.Tk()
root.title("Login / Register")
root.geometry("300x200")
root.resizable(False, False)

# Email
tk.Label(root, text="Email:").pack(pady=(10, 0))
email_entry = tk.Entry(root, width=30)
email_entry.pack()

# Password
tk.Label(root, text="Password:").pack(pady=(10, 0))
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

# Buttons
login_btn = tk.Button(root, text="Login")
login_btn.pack(pady=(10, 5))

register_btn = tk.Button(root, text="Register")
register_btn.pack()

root.mainloop()
