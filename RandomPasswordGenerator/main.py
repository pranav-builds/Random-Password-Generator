import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
from datetime import datetime

# Function to generate password
def generate_password():
    char_set = ""
    if uppercase_var.get():
        char_set += string.ascii_uppercase
    if lowercase_var.get():
        char_set += string.ascii_lowercase
    if digits_var.get():
        char_set += string.digits
    if symbols_var.get():
        char_set += string.punctuation

    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for length")
        return

    if not char_set:
        messagebox.showerror("Error", "Select at least one character type")
        return

    if length <= 0:
        messagebox.showerror("Error", "Length must be greater than 0")
        return

    password = ''.join(random.choice(char_set) for _ in range(length))
    password_var.set(password)
    update_strength_label(password)

# Function to copy password
def copy_to_clipboard():
    pwd = password_var.get()
    if pwd:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy")

# Function to save password
def save_to_file():
    pwd = password_var.get()
    if pwd:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("data/passwords.txt", "a") as f:
            f.write(f"{now} - {pwd}\n")
        messagebox.showinfo("Saved", "Password saved to file!")
    else:
        messagebox.showwarning("Warning", "No password to save")

# Function to update strength label
def update_strength_label(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    types = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and types >= 3:
        strength_label.config(text="Strength: Strong", fg="green")
    elif length >= 8 and types >= 2:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Weak", fg="red")

# Create window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x450")
root.configure(bg="white")

# Title Label
title_label = tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"), bg="white")
title_label.pack(pady=10)

# Checkboxes
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, bg="white").pack()
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var, bg="white").pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg="white").pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="white").pack()

# Password length
length_label = tk.Label(root, text="Password Length:", bg="white")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Password output
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=30)
password_entry.pack(pady=10)

# Strength Label
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12), bg="white")
strength_label.pack(pady=5)

# Buttons
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white")
generate_btn.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="green", fg="white")
copy_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save to File", command=save_to_file, bg="purple", fg="white")
save_btn.pack(pady=5)

# Run the application
root.mainloop()