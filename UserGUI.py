from tkinter import *

class GUI:

    def __init__(self, root):
        root.title("Command Line Interface")
        root.geometry("800x450")

        Label(root, text=" Command: ").grid(row=1)

        self.output = Text(root)
        self.output.configure(state="disabled")
        self.entry = Entry(root, )
        enter = Button(root, text="Enter", command=self.submit)

        self.output.grid(row=0, column=0, columnspan=3, padx=10, sticky=E + W)
        self.entry.grid(row=1, column=1, padx=0, pady=10, sticky=E + W)
        enter.grid(row=1, column=2, padx=10, pady=10, sticky=E+W)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

        root.bind('<Return>', lambda _: self.submit())

    def submit(self):
        if self.entry.get() != "":
            self.terminal_write(self.entry.get())
            self.entry.delete(0, 'end')


    def terminal_write(self, text):
        self.output.configure(state="normal")
        self.output.insert(index=END, chars=(text+'\n'))
        self.output.configure(state="disabled")

root = Tk()
gui = GUI(root)
root.mainloop()