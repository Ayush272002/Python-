from tkinter import *
from datetime import datetime

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To Do Application")
        
        self.frame = Frame(self.master)
        self.frame.pack(pady=20)
        
        self.listbox = Listbox(self.frame, width=30, height=10, bd=1, relief=SOLID, highlightthickness=0)
        self.listbox.pack(padx=20, pady=20, side=LEFT, fill=BOTH, expand=True)

        self.scrollbar_y = Scrollbar(self.frame, orient=VERTICAL)
        self.scrollbar_y.pack(pady=20, side=RIGHT, fill=Y)
        
        self.scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scrollbar_x.pack(padx=20, side=BOTTOM, fill=X)

        self.scrollbar_y.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar_x.set)
        
        self.entry = Entry(self.master, width=30, bd=1, relief=SOLID, highlightthickness=0)
        self.entry.pack(pady=20)
        
        self.button_frame = Frame(self.master)
        self.button_frame.pack(pady=20)
        
        self.add_button = Button(self.button_frame, text="Add Task", width=10, command=self.add_task)
        self.add_button.pack(padx=10, pady=10, side=LEFT)
        
        self.remove_button = Button(self.button_frame, text="Remove Task", width=10, command=self.remove_task)
        self.remove_button.pack(padx=10, pady=10, side=LEFT)

        self.datetime_label = Label(self.master, text="", font=("Helvetica", 10))
        self.datetime_label.pack()

        self.update_datetime()
        self.master.after(1000, self.update_datetime)  # Update every 1000 milliseconds (1 second)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def remove_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            self.listbox.delete(selected_task)

    def update_datetime(self):
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
        current_day = now.strftime("%A")

        datetime_str = f"Date: {current_date} | Time: {current_time} | Day: {current_day}"
        self.datetime_label.config(text=datetime_str)

        self.master.after(1000, self.update_datetime)  # Schedule the next update

if __name__ == "__main__":
    root = Tk()
    app = ToDoApp(root)
    root.mainloop()
