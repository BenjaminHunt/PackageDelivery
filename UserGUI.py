from tkinter import *
import PackageDatabase as db


class GUI:
    new = False
    role = ""
    id = ""

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

        self.terminal_write("Welcome to the Package Delivery System Interface.")
        self.terminal_write("Please enter your ID, or \"new\" if you are a new user.")

    def submit(self):
        input = self.entry.get()
        self.terminal_write("> " + input)

        if self.id != "":
            if input != "":
                if input == "role" or input == "myrole" or input == "getrole":
                    if self.role == "admin" or self.role == "employee":
                        self.terminal_write("You are an {}.".format(self.role))
                    else:
                        self.terminal_write("You are a {}.".format(self.role))
                elif input == "logout" or input == "log out":
                    self.id = ""
                    self.role = ""
                    self.terminal_write("You have been successfully logged out.")
                    self.terminal_write("To log in, please enter your ID, or \"new\" if you are a new user.")
                else:
                    response = db.parse_and_execute(input, self.id, self.role)
                    self.terminal_write(response)
        elif self.new:
            if input == "customer" or input == "employee" or input == "admin":
                self.role = input
                self.id = db.new(self.role)
                self.terminal_write("Your account has been created. You are logged in with the ID: {}. "
                                    "Use \"help\" for available commands".format(self.id))
            else:
                self.terminal_write("\"{}\" is not a valid role.".format(input))
                self.terminal_write("What is your role?")
        else:
            if input == "new":
                self.new = True
                self.terminal_write("What is your role? (customer/employee/admin)")
            elif db.login(input):
                self.id = input
                self.role = db.get_role(self.id)
                self.terminal_write("You have successfully been logged in.\nUse \"help\" for available commands.")
            else:
                self.terminal_write("'{}' is not a valid ID.".format(input))
                self.terminal_write("Please enter your ID, or \"new\" if you are a new user.")
        self.entry.delete(0, 'end')

    def terminal_write(self, text):
        self.output.configure(state="normal")
        self.output.insert(index=END, chars=(text+'\n'))
        self.output.configure(state="disabled")
        self.output.yview_moveto(1)


root = Tk()
gui = GUI(root)
root.mainloop()
