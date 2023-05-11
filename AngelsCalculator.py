import tkinter as tk

# AboutWindow: A subclass of Toplevel that displays information about the calculator
class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("About")
        self.geometry("200x100")

        # Create a label with the application's name and version
        about_label = tk.Label(self, text="Angel's Calculator\nVersion 1.0")
        about_label.pack(expand=True, fill=tk.BOTH)

# SimpleCalculator: A subclass of Tk that represents the main calculator window
class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Angel's Calculator")
        self.geometry("300x200")

        # Create the calculator's widgets (buttons, entry field, etc.)
        self.create_widgets()

    # create_widgets: Set up the calculator's interface by configuring the background, creating buttons, and setting up grid layout
    def create_widgets(self):
        self.configure(bg="black")

        # result_var: A StringVar that stores the text displayed in the entry field
        self.result_var = tk.StringVar()

        # Create an Entry widget for displaying the calculation result
        self.entry = tk.Entry(self, textvariable=self.result_var, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, sticky='news')

        # Define the buttons and their corresponding grid positions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 1, 4), ('%', 2, 4), ('±', 3, 4),
        ]

        # Create the buttons and add them to the grid
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, command=lambda t=text: self.on_button_click(t), bg="blue", fg="white")
            button.grid(row=row, column=col, sticky='news')

        # Create an About button that opens the AboutWindow
        about_button = tk.Button(self, text="About", command=self.open_about_window, bg="blue", fg="white")
        about_button.grid(row=4, column=4, sticky='news')

        # Configure the grid rows and columns to have equal weight
        for i in range(5):
            self.rowconfigure(i, weight=1)

        for i in range(5):
            self.columnconfigure(i, weight=1)

        # on_button_click: Handle button clicks by performing the corresponding operation or updating the entry field
    def on_button_click(self, button_text):
        # If '=' button is clicked, try to evaluate the expression in the entry field
        if button_text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                # If there's an error in the expression, display "Error"
                self.result_var.set("Error")
        # If 'C' button is clicked, clear the entry field
        elif button_text == 'C':
            self.result_var.set("")
        # If '%' button is clicked, divide the current value in the entry field by 100
        elif button_text == '%':
            try:
                result = float(self.result_var.get()) / 100
                self.result_var.set(result)
            except Exception:
                # If there's an error in the expression, display "Error"
                self.result_var.set("Error")
        # If '±' button is clicked, change the sign of the current value in the entry field
        elif button_text == '±':
            try:
                result = -float(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                # If there's an error in the expression, display "Error"
                self.result_var.set("Error")
        else:
            # Append the button_text to the existing text in the entry field
            current_text = self.result_var.get()
            self.result_var.set(current_text + button_text)

    # open_about_window: Open the AboutWindow when the "About" button is clicked
    def open_about_window(self):
        AboutWindow(self)

# Main entry point: Create an instance of SimpleCalculator and start the application's event loop
if __name__ == "__main__":
    app = SimpleCalculator()
    app.mainloop()
