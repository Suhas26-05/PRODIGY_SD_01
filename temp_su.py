import tkinter as tk
from tkinter import messagebox

# Function to convert temperatures
def convert_temp():
    try:
        if celsius_entry.get():
            celsius = float(celsius_entry.get())
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
            fahrenheit_entry.delete(0, tk.END)
            fahrenheit_entry.insert(0, "%.2f" % fahrenheit)
            kelvin_entry.delete(0, tk.END)
            kelvin_entry.insert(0, "%.2f" % kelvin)
            result_label.config(text="Converted Successfully!", fg="red", font=("Times New Roman", 12, "bold"))

        elif fahrenheit_entry.get():
            fahrenheit = float(fahrenheit_entry.get())
            celsius = (fahrenheit - 32) * 5/9
            kelvin = celsius + 273.15
            celsius_entry.delete(0, tk.END)
            celsius_entry.insert(0, "%.2f" % celsius)
            kelvin_entry.delete(0, tk.END)
            kelvin_entry.insert(0, "%.2f" % kelvin)
            result_label.config(text="Converted Successfully!", fg="red", font=("Times New Roman", 12, "bold"))

        elif kelvin_entry.get():
            kelvin = float(kelvin_entry.get())
            celsius = kelvin - 273.15
            fahrenheit = (kelvin * 9/5) - 459.67
            celsius_entry.delete(0, tk.END)
            celsius_entry.insert(0, "%.2f" % celsius)
            fahrenheit_entry.delete(0, tk.END)
            fahrenheit_entry.insert(0, "%.2f" % fahrenheit)
            result_label.config(text="Converted Successfully!", fg="red", font=("Times New Roman", 12, "bold"))

        else:
            result_label.config(text="Please enter a value!", fg="red", font=("Times New Roman", 12, "bold"))

    except ValueError:
        # Clear all fields and show an error message if invalid input is entered
        celsius_entry.delete(0, tk.END)
        fahrenheit_entry.delete(0, tk.END)
        kelvin_entry.delete(0, tk.END)
        result_label.config(text="Invalid Input!", fg="red", font=("Times New Roman", 12, "bold"))

def clear_fields():
    # Clear all input fields and reset the result message
    celsius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)
    kelvin_entry.delete(0, tk.END)
    result_label.config(text="")

def show_intro():
    # Create an introductory window
    intro = tk.Toplevel()
    intro.title("Welcome")
    intro.geometry("300x150")
    intro.configure(bg='#f0f0f0')

    # Introductory message
    intro_label = tk.Label(intro, text="Welcome to the Temperature Converter!\n\nThis application converts temperatures between Celsius, Fahrenheit, and Kelvin.",
                           bg='#f0f0f0', wraplength=280, justify="center")
    intro_label.pack(padx=10, pady=20)

    # Close button
    close_button = tk.Button(intro, text="Start", command=lambda: [intro.destroy(), root.deiconify()])
    close_button.pack(pady=10)

    # Hide the main window while showing the intro window
    root.withdraw()
    intro.mainloop()

# Creating Tk window
root = tk.Tk()

# Setting geometry of Tk window
root.geometry('400x250')
root.configure(bg='#f0f0f0')

# Using title() to display a message in the title bar
root.title('Temperature Converter')

# Description label
description_label = tk.Label(root, text="This application converts temperatures between Celsius, Fahrenheit, and Kelvin.",
                             bg='#f0f0f0', wraplength=380, justify="left")
description_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Labels and entry fields
celsius_label = tk.Label(root, text="Celsius", bg='#f0f0f0')
celsius_label.grid(row=1, column=0, padx=10, pady=5, sticky='W')
celsius_entry = tk.Entry(root)
celsius_entry.grid(row=1, column=1, padx=10, pady=5)

fahrenheit_label = tk.Label(root, text="Fahrenheit", bg='#f0f0f0')
fahrenheit_label.grid(row=2, column=0, padx=10, pady=5, sticky='W')
fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=2, column=1, padx=10, pady=5)

kelvin_label = tk.Label(root, text="Kelvin", bg='#f0f0f0')
kelvin_label.grid(row=3, column=0, padx=10, pady=5, sticky='W')
kelvin_entry = tk.Entry(root)
kelvin_entry.grid(row=3, column=1, padx=10, pady=5)

# Result label
result_label = tk.Label(root, bg='#f0f0f0')
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temp)
convert_button.grid(row=4, column=1, pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=4, column=0, pady=10)

# Show the introductory window
show_intro()

# Infinite loop which is required to run tkinter program infinitely
root.mainloop()
