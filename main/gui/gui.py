from domain.notifications import Notifications
from tkinter import *
from tkinter import ttk

class GUI:

    def __init__(self, notifications: Notifications):
        self.notifications = notifications

    
    

    def run(self):
        root = Tk()
        root.title("New Notification")

        def new_notification(*args):
            try:
                split_time = timer.get().split(":")
                time_in_seconds = 0
                time_in_seconds += int(split_time[-1])
                time_in_seconds += 60*int(split_time[-2]) if len(split_time)>1 else 0
                time_in_seconds += 60**2*int(split_time[0]) if len(split_time)>2 else 0
                self.notifications.add_notification(name,time_in_seconds)
                name.set("")
                timer.set("")
            except Exception as e:
                print("something went wrong..")
                print(e)
                pass

        mainframe = ttk.Frame(root, padding="0 0 0 0")
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        
        name = StringVar()
        timer = StringVar()

        name_entry = ttk.Entry(mainframe, width=20, textvariable=name)
        name_entry.grid(column=1,row=2,sticky=(W,E))

        timer_entry = ttk.Entry(mainframe, width=20, textvariable=timer)
        timer_entry.grid(column=1,row=4,sticky=(W,E))

        ttk.Label(mainframe, text="What do you want to be notified for:").grid(column=1,row=1, sticky=W)
        ttk.Label(mainframe, text="When do you want to be notified (format hours:minutes:seconds)").grid(column=1,row=3,sticky=W)
        ttk.Button(mainframe, text="Notify me!", command=new_notification).grid(column=1,row=5,sticky=E)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5,pady=5)

        name_entry.focus()
        root.bind("<Return>", new_notification)

        root.mainloop()
