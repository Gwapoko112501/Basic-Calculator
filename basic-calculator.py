import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create input field
expression_field = tk.Entry(window, width=30, borderwidth=5)
expression_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update the expression field
def button_click(char):
    expression_field.insert(tk.END, char)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(expression_field.get())
        expression_field.delete(0, tk.END)
        expression_field.insert(0, result)
    except:
        expression_field.delete(0, tk.END)
        expression_field.insert(0, "Error")

# Function to clear the expression field
def clear():
    expression_field.delete(0, tk.END)

# Create buttons
button_1 = tk.Button(window, text='1', padx=20, pady=20, command=lambda: button_click('1'))
button_2 = tk.Button(window, text='2', padx=20, pady=20, command=lambda: button_click('2'))
button_3 = tk.Button(window, text='3', padx=20, pady=20, command=lambda: button_click('3'))
button_4 = tk.Button(window, text='4', padx=20, pady=20, command=lambda: button_click('4'))
button_5 = tk.Button(window, text='5', padx=20, pady=20, command=lambda: button_click('5'))
button_6 = tk.Button(window, text='6', padx=20, pady=20, command=lambda: button_click('6'))
button_7 = tk.Button(window, text='7', padx=20, pady=20, command=lambda: button_click('7'))
button_8 = tk.Button(window, text='8', padx=20, pady=20, command=lambda: button_click('8'))
button_9 = tk.Button(window, text='9', padx=20, pady=20, command=lambda: button_click('9'))
button_0 = tk.Button(window, text='0', padx=20, pady=20, command=lambda: button_click('0'))
button_plus = tk.Button(window, text='+', padx=20, pady=20, command=lambda: button_click('+'))
button_minus = tk.Button(window, text='-', padx=20, pady=20, command=lambda: button_click('-'))
button_multiply = tk.Button(window, text='*', padx=20, pady=20, command=lambda: button_click('*'))
button_divide = tk.Button(window, text='/', padx=20, pady=20, command=lambda: button_click('/'))
button_equal = tk.Button(window, text='=', padx=20, pady=20, command=evaluate)
button_clear = tk.Button(window, text='Clear', padx=20, pady=20, command=clear)

# Place the buttons on the grid
button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_0.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2)
button_plus.grid(row=2, column=3)
button_minus.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)
button_equal.grid(row=6, column=0, columnspan=4)

window.mainloop()