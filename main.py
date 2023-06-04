import customtkinter
from CTkMessagebox import CTkMessagebox


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label_heading = customtkinter.CTkLabel(self, text="Enter Details", font=('Monospace', 30), width=10, justify='center')
        self.label_heading.place(relx=0.5, rely=0.1, anchor='n')

        self.label_name = customtkinter.CTkLabel(self, text="Full Name:")
        self.label_name.place(relx=0.15, rely=.2, anchor='nw')
        self.entry_name = customtkinter.CTkEntry(self, placeholder_text="Full Name", width=200)
        self.entry_name.place(relx=.15, rely=.25, anchor='nw')

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

        self.button_logs = customtkinter.CTkButton(self, text="Old Logs")
        self.button_logs.place(relx=0.7, rely=0.90, anchor='s')

    def save_button(self):
        if self.entry_name.get() and self.entry_amount.get() and self.textbox_reason.get("1.0",'end-1c'):
            CTkMessagebox(title="Info", message="Added to Database Successfully")
            self.entry_name.delete(0, 'end')
            self.entry_amount.delete(0, 'end')
            self.textbox_reason.delete('1.0', 'end')



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