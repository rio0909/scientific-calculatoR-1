import tkinter as tk
from math import sin, cos, tan, log, radians

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        if 'sin' in expression:
            angle = float(expression.split('sin(')[1].strip(')'))
            result = sin(radians(angle))
        elif 'cos' in expression:
            angle = float(expression.split('cos(')[1].strip(')'))
            result = cos(radians(angle))
        elif 'tan' in expression:
            angle = float(expression.split('tan(')[1].strip(')'))
            result = tan(radians(angle))
        elif 'log' in expression:
            value = float(expression.split('log(')[1].strip(')'))
            result = log(value)
        else:
            result = eval(expression)  # Use eval with caution
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg='lightblue')

# Create an entry widget for displaying calculations
entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons with enhanced styles
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'sin(', 'cos(', 'tan(', 'C'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        b = tk.Button(root, text=button, command=calculate, bg='green', fg='white', font=('Arial', 14))
    elif button == 'C':
        b = tk.Button(root, text=button, command=clear, bg='red', fg='white', font=('Arial', 14))
    else:
        b = tk.Button(root, text=button, command=lambda b=button: button_click(b), bg='lightgray', font=('Arial', 14))
    
    b.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Adjust grid weights for resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Start the main loop
root.mainloop()