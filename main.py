import customtkinter
from CTkMessagebox import CTkMessagebox
from pymongo.mongo_client import MongoClient
from tkinter import ttk
from datetime import datetime

url = "mongodb+srv://mongodb:mongodb@tally.i6wfrlt.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client['Punekar']
collec = db['Tally']

class LogFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.my_tree = ttk.Treeview(self)
        self.my_tree["columns"] = ("Department", "Date_time", "Resort Name", "Person Name", "Amount", "Payment_type", "Approved", "Paid")

        self.my_tree.column("#0", anchor='w', width=70)
        self.my_tree.column("Department", anchor='w', width=70)
        self.my_tree.column("Date_time", anchor='center', width=120)
        self.my_tree.column("Resort Name", anchor='center', width=200)
        self.my_tree.column("Person Name", anchor='w', width=200)
        self.my_tree.column("Amount", anchor='w', width=100)
        self.my_tree.column("Payment_type", anchor='w', width=100)
        self.my_tree.column("Approved", anchor='w', width=60)
        self.my_tree.column("Paid", anchor='w', width=60)

        self.my_tree.heading("#0", text="Label", anchor='w')
        self.my_tree.heading("Department", text="Department", anchor='w')
        self.my_tree.heading("Date_time", text="Date&Time", anchor='center')
        self.my_tree.heading("Resort Name", text="Resort Name", anchor='center')
        self.my_tree.heading("Person Name", text="Person Name", anchor='w')
        self.my_tree.heading("Amount", text="Amount", anchor='w')
        self.my_tree.heading("Payment_type", text="Payment Type", anchor='w')
        self.my_tree.heading("Approved", text="Approved", anchor='w')
        self.my_tree.heading("Paid", text="Paid", anchor='w')

        self.my_tree["height"] = 34
        try:
            for one_collec in collec.find():
                self.my_tree.insert(parent='', index='end', text="Parent", values=(one_collec["Department"],
                                                                                            one_collec["Date_time"],
                                                                                            one_collec["Resort Name"], 
                                                                                            one_collec["Person Name"],
                                                                                            one_collec["Amount"],
                                                                                            one_collec["Payment_type"],
                                                                                            one_collec["Approved"],
                                                                                            one_collec["Paid"],
                                                                                            one_collec["Signature"]))
        except Exception:
            CTkMessagebox(title="Error", message=Exception)


        self.my_tree.pack(pady=10)

        self.style = ttk.Style()
            
        self.style.theme_use("default")

        self.style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0)
        self.style.map('Treeview', background=[('selected', '#22559b')])

        self.style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        self.style.map("Treeview.Heading",
                    background=[('active', '#3484F0')])
        
        self.style.configure("Treeview", height=700)

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label_heading = customtkinter.CTkLabel(self, text="Enter Details", font=('Monospace', 30), width=10, justify='center')
        self.label_heading.place(relx=0.5, rely=0.1, anchor='n')


        self.label_name = customtkinter.CTkLabel(self, text="Client Name:")
        self.label_name.place(relx=0.15, rely=.2, anchor='nw')
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Resort 1", "Resort 2", "Client 1", "Client 2"])
        self.optionmenu.place(relx=.15, rely=.25, anchor='nw')
        # self.entry_name = customtkinter.CTkEntry(self, placeholder_text="Client Name", width=200)

        self.label_amount = customtkinter.CTkLabel(self, text="Amount (Rs.)")
        self.label_amount.place(relx=0.15, rely=.3, anchor='nw')
        self.entry_amount = customtkinter.CTkEntry(self, placeholder_text="Amount (Rs)", width=140)
        self.entry_amount.place(relx=.15, rely=.35, anchor='nw')

        self.label_reason = customtkinter.CTkLabel(self, text="Reason:")
        self.label_reason.place(relx=0.15, rely=.4, anchor='nw')
        self.textbox_reason = customtkinter.CTkTextbox(master=self, width=400, corner_radius=8)
        self.textbox_reason.place(relx=.15, rely=.45, anchor='nw')

        self.button_save = customtkinter.CTkButton(self, text="Save", command=self.save_button)
        self.button_save.place(relx=0.3, rely=0.90, anchor='s')

        self.button_logs = customtkinter.CTkButton(self, text="Old Logs", command=self.open_logs)
        self.button_logs.place(relx=0.7, rely=0.90, anchor='s')

        self.logs_window = None

    def save_button(self):
        dic = {
            "Department": "Indoor",
            "Date_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Client Name": self.optionmenu.get(),
            "Person Name": "",
            "Amount": self.entry_amount.get(),
            "Reason": self.textbox_reason.get(1.0, "end-1c"),
            "Payment_from": "",
            "Payment_to": "",
            "Approved": 0,
            "Paid": 0,
            "Signature": 0,
            "Signature_Image": ""
        }
        if self.optionmenu.get() and self.entry_amount.get() and self.textbox_reason.get("1.0",'end-1c'):
            try:
                # Check weather the amount is in integer or not
                int(self.entry_amount.get())
                collec.insert_one(dic)
                CTkMessagebox(title="Info", message="Added to Database Successfully")
                self.optionmenu.set('Resort 1')
                self.entry_amount.delete(0, 'end')
                self.textbox_reason.delete('1.0', 'end')
            except Exception:
                CTkMessagebox(title="Error", message="Please Enter all values properly or try again later")

    def open_logs(self):
        self.logs_window = customtkinter.CTkToplevel(self)
        self.logs_window.geometry("1000x750")
        self.logs_window.focus()
        self.logs_window.resizable(False, False)

        self.frame = LogFrame(master=self.logs_window, border_color='blue')
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="e")

        self.button_frame = customtkinter.CTkFrame(master=self.logs_window, height=710, width=150, corner_radius=10)
        self.button_frame.grid(row=0, column=1)
        
        # self.sort_btn = customtkinter.CTkButton(master=self.button_frame, text="Sort", corner_radius=10).pack()




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()