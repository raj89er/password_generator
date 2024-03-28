import tkinter as tk
from tkinter import messagebox
import random
import string

pwd_min = 6
pwd_max = 99

# Function to generate a random password
def generate_password():
    length_str = length_entry.get()
    if not length_str.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a valid number for password length.")
        return
    
    length = int(length_str)
    if length < pwd_min or length > pwd_max:
        messagebox.showwarning("Invalid Length", f"Password length should be between {pwd_min} and {pwd_max}.")
        return
    
    include_lower = lower_var.get()
    include_upper = upper_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()
    
    chars = ''
    if include_lower:
        chars += string.ascii_lowercase
    if include_upper:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += "!@#$%^&*"
    
    if not chars:
        messagebox.showwarning("Character Types", "Please select at least one character type.")
        return
    
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
    # Adjust width of password entry field based on password length
    password_entry.config(width=len(password) + 2)  # Adding extra space for visibility toggle button


# Function to toggle password visibility
def toggle_password_visibility():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        show_password_button.config(text="Show Password")
    else:
        password_entry.config(show="")
        show_password_button.config(text="Hide Password")

# Create tkinter window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x250")

# Label and Entry for password length
length_label = tk.Label(window, text="How long do you want your password to be? (6-99)")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Checkbuttons for character types
lower_var = tk.BooleanVar()
lower_check = tk.Checkbutton(window, text="Include lowercase letters?", variable=lower_var)
lower_check.pack()

upper_var = tk.BooleanVar()
upper_check = tk.Checkbutton(window, text="Include uppercase letters?", variable=upper_var)
upper_check.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(window, text="Include digits?", variable=digits_var)
digits_check.pack()

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(window, text="Include symbols? (!@#$%^&*)", variable=symbols_var)
symbols_check.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Entry to display generated password
password_entry = tk.Entry(window, show='*', width=10)
password_entry.pack()

# Button to show/hide password
show_password_button = tk.Button(window, text="Show Password", command=toggle_password_visibility)
show_password_button.pack()

# Start the tkinter event loop
window.mainloop()
