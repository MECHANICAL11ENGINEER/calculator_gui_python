import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.expression = ""

        # Entry box to display the expression/result
        self.entry = tk.Entry(self.master, width=40, borderwidth=5, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define the buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_value = 1
        col_value = 0

        for button in buttons:
            tk.Button(self.master, text=button, width=10, height=3,
                      command=lambda bt=button: self.on_button_click(bt)).grid(row=row_value, column=col_value)
            col_value += 1
            if col_value > 3:
                col_value = 0
                row_value += 1

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif button_text == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(button_text)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()