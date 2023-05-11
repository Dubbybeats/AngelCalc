import tkinter as tk

class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("About")
        self.geometry("200x100")

        about_label = tk.Label(self, text="Angel's Calculator\nVersion 1.0")
        about_label.pack(expand=True, fill=tk.BOTH)

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Angel's Calculator")
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        self.configure(bg="black")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(self, textvariable=self.result_var, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, sticky='news')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 1, 4), ('%', 2, 4), ('±', 3, 4),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, command=lambda t=text: self.on_button_click(t), bg="blue", fg="white")
            button.grid(row=row, column=col, sticky='news')

        about_button = tk.Button(self, text="About", command=self.open_about_window, bg="blue", fg="white")
        about_button.grid(row=4, column=4, sticky='news')

        for i in range(5):
            self.rowconfigure(i, weight=1)

        for i in range(5):
            self.columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif button_text == 'C':
            self.result_var.set("")
        elif button_text == '%':
            try:
                result = float(self.result_var.get()) / 100
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif button_text == '±':
            try:
                result = -float(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button_text)

    def open_about_window(self):
        AboutWindow(self)

if __name__ == "__main__":
    app = SimpleCalculator()
    app.mainloop()
