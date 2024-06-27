import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# example of copied password

# (o%:FbB}p>
# AMI",}IOouxi'!n(FSfo

# end of the example

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''
    
    all_chars = lower + upper + digits + special
    
    if not all_chars:
        raise ValueError("No characters available to generate password. Adjust your settings.")
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate_and_display_passwords():
    length = length_var.get()
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_special = special_var.get()

    if length <= 0:
        messagebox.showerror("Error", "Password length must be a positive integer.")
        return

    options_selected = sum([use_uppercase, use_numbers, use_special])
    if options_selected < 1:
        messagebox.showerror("Error", "Please select at least three options.")
        return

    try:
        password1 = generate_password(length, use_uppercase, use_numbers, use_special)
        password2 = generate_password(length, use_uppercase, use_numbers, use_special)
        password3 = generate_password(length, use_uppercase, use_numbers, use_special)
        password_var1.set(password1)
        password_var2.set(password2)
        password_var3.set(password3)
        copy_button1.config(text="Copy")
        copy_button2.config(text="Copy")
        copy_button3.config(text="Copy")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard(password, button):
    pyperclip.copy(password)
    button.config(text="Copied")

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x450") 
  
root.resizable(False, False)

length_var = tk.IntVar(value=12)
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
password_var1 = tk.StringVar()
password_var2 = tk.StringVar()
password_var3 = tk.StringVar()

tk.Label(root, text="Password Length:").pack(pady=5)
tk.Entry(root, textvariable=length_var).pack(pady=5)

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=5)

tk.Checkbutton(checkbox_frame, text="Uppercase", variable=uppercase_var).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame, text="Numbers", variable=numbers_var).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame, text="Special Characters", variable=special_var).pack(side=tk.LEFT, padx=5)

btn1 = tk.Button(root, text="Generate Passwords", command=generate_and_display_passwords).pack(pady=5)

password_frame1 = tk.Frame(root)
password_frame1.pack(pady=5)
tk.Entry(password_frame1, textvariable=password_var1, state='readonly', width=60).pack(side=tk.LEFT, padx=5)
copy_button1 = tk.Button(password_frame1, text="Copy", command=lambda: copy_to_clipboard(password_var1.get(), copy_button1))
copy_button1.pack(side=tk.LEFT, padx=5)

password_frame2 = tk.Frame(root)
password_frame2.pack(pady=5)
tk.Entry(password_frame2, textvariable=password_var2, state='readonly', width=60).pack(side=tk.LEFT, padx=5)
copy_button2 = tk.Button(password_frame2, text="Copy", command=lambda: copy_to_clipboard(password_var2.get(), copy_button2))
copy_button2.pack(side=tk.LEFT, padx=5)

password_frame3 = tk.Frame(root)
password_frame3.pack(pady=5)
tk.Entry(password_frame3, textvariable=password_var3, state='readonly', width=60).pack(side=tk.LEFT, padx=5)
copy_button3 = tk.Button(password_frame3, text="Copy", command=lambda: copy_to_clipboard(password_var3.get(), copy_button3))
copy_button3.pack(side=tk.LEFT, padx=5)

root.mainloop()
