from tkinter import *
import PackageDatabase as db


class GUI:
    role_defined = False
    role = ""

    def __init__(self, root):
        root.title("Command Line Interface")
        root.geometry("800x450")
        root.minsize(400, 200)

        Label(root, text=" Command: ").grid(row=1)

        self.output = Text(root)
        self.output.configure(state="disabled")

        scroll = Scrollbar(root, command=self.output.yview)
        self.output['yscrollcommand'] = scroll.set

        self.entry = Entry(root)
        enter = Button(root, text="Enter", command=self.submit)

        self.output.grid(row=0, column=0, columnspan=3, padx=10, sticky=E + W)
        self.entry.grid(row=1, column=1, padx=0, pady=10, sticky=E + W)
        scroll.grid(row=0, column=3, padx=5, pady=10, sticky=N + S)
        enter.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky=E+W)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

        root.bind('<Return>', lambda _: self.submit())

        self.terminal_write("Welcome to the Package Delivery System Interface\nWhat is your role?")


    def submit(self):
        input = self.entry.get()
        self.terminal_write("> " + input)
        if self.role_defined:
            if input != "":
                db.parse_and_execute(self.role, input)
        else:
            input = input.lower()
            if input == "admin" or input == "customer" or input == "employee":
                self.role = input
                response = "You are successfully recognized as a"
                if self.role == "customer":
                    response += " "
                else:
                    response += "n "
                self.terminal_write(response + self.role())
            else:
                self.terminal_write("'input'" + " is not a valid role.\nWhat is your role? (admin/customer/employee)")
        self.entry.delete(0, 'end')

    def terminal_write(self, text):
        self.output.configure(state="normal")
        self.output.insert(index=END, chars=(text+'\n'))
        self.output.configure(state="disabled")
        self.output.yview_moveto(1)


root = Tk()
gui = GUI(root)
root.mainloop()
