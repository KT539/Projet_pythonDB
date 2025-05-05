import tkinter as tk
from HomePage import homepage_window

# create the main window
def main():
    win = tk.Tk()
    win.title("Festival App")
    win.geometry("400x700")
    win.resizable(False, False)
    homepage_window(win)
    win.mainloop()

main()