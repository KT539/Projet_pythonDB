import tkinter as tk

from DB_managment import concerts_requests

'''used both ChatGPT and official doc to learn how to connect to a database
   with Python and understand the basics of the mysql.connector library'''
def concerts_window(win):

    # create an outer frame
    outer_frame = tk.Frame(win)
    outer_frame.grid(row=0, column=0, sticky="nsew")

    # title label
    label_title = tk.Label(outer_frame, text="Concerts", width=10, height=1, font=("Arial", 25, "bold"), fg="#000000")
    label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="n")

    # embed the canvas and scrollbar in the outer frame
    canvas = tk.Canvas(outer_frame, width=360, height=535)
    scrollbar = tk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky="ns")
    canvas.grid(row=1, column=0, sticky="nsew", padx=5, pady=10)

    # make the outer frame resizable
    outer_frame.grid_rowconfigure(1, weight=1)
    outer_frame.grid_columnconfigure(0, weight=1)

    # create a frame for bottom buttons
    buttons_frame = tk.Frame(outer_frame)
    buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

    # function to switch to new reservation page
    def switch_makeReservation():
        outer_frame.destroy()
        from MakeReservation import makeReservation_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        makeReservation_window(win)

    # make a reservation button
    btn_res = tk.Button(buttons_frame, text="Make a reservation", font=("Arial", 12), fg="#000000", command=switch_makeReservation)
    btn_res.grid(row=0, column=0, padx=5, pady=(5, 15))

    # function to switch to reservation deletion page
    def switch_deleteReservation():
        outer_frame.destroy()
        from DeleteReservation import deleteReservation_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        deleteReservation_window(win)

    # delete a reservation button
    btn_cancel = tk.Button(buttons_frame, text="Cancel a reservation", font=("Arial", 12), fg="#000000", command=switch_deleteReservation)
    btn_cancel.grid(row=0, column=1, padx=5, pady=(5, 15))

    # function to switch to Home page
    def switch_HomePage():
        outer_frame.destroy()
        from HomePage import homepage_window  # moved the import statement here on ChatGPT's suggestion, after experiencing circular import issues
        homepage_window(win)

    # return to HomePage button
    btn_return = tk.Button(buttons_frame, text="Return to Home Page", font=("Arial", 12), fg="#000000", command=switch_HomePage)
    btn_return.grid(row=1, column=0, columnspan=2, pady=10)

    # embed an inner frame in the canvas
    inner_frame = tk.Frame(canvas, bg="lightgray", bd=2, relief="groove")
    canvas_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    concerts=concerts_requests()

    # put the widgets in the inner frame
    for i, concert in enumerate(concerts): # loop structure from ChatGPT
        cnrt_id, cnrt_name, cnrt_date, cnrt_scene = concert
        widgets = tk.Button(inner_frame, text=f"{cnrt_id} | Concert name : {cnrt_name}\nConcert date : {cnrt_date}\nLocation : scene n° {cnrt_scene}", bg="white", bd=1, relief="solid", padx=10, pady=10)
        widgets.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

    # stretch the widgets horizontally inside the frame
    inner_frame.grid_columnconfigure(0, weight=1)

    # update the scrollregion
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", update_scrollregion)

    # adjust widgets dynamic width
    def resize_inner_frame(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize_inner_frame)



