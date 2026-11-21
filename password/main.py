import tkinter as tk
from tkinter import ttk
import string
import secrets

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x200")

# Use a Frame with padding so widgets aren't stuck to the window edges.
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Make both columns share the available width equally.
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Application variables
contents = tk.StringVar()
status = tk.StringVar(value="Enter a password or click Generate.")

# Row 0: Text field spanning both columns
entry = ttk.Entry(frame, textvariable=contents)
entry.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 12))


def validate_password():
    password = contents.get()
    if not _password_validator(password):
        status.set("Password should contain at least 8 characters, one number, one capital letter, and one special character!")
        return
    status.set("Password is valid.")


def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(10))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c in string.punctuation for c in password)
                and sum(c.isdigit() for c in password)):
            break
    if not _password_validator(password):
        status.set("Generated password is not valid.")
        return
    contents.set(password)
    status.set("Generated a sample password.")


def _password_validator(password):
    if len(password) < 8:
        return False
    
    numbers = 0
    capital_letters = 0
    special_characters = 0
    lower_letters = 0

    for letter in password:
        if letter.isnumeric():
            numbers += 1
        elif letter.islower():
            lower_letters += 1
        elif letter.isupper():
            capital_letters += 1
        elif letter in string.punctuation:
            special_characters += 1

    if numbers == 0 or capital_letters == 0 or special_characters == 0:
        return False

    return True

def clear():
    contents.set("")
    status.set("")


# Row 1: Validate (left) and Generate (right)
ttk.Button(frame, text="Validate", command=validate_password).grid(
    row=1, column=0, sticky="ew", padx=(0, 6), pady=(0, 8)
)
ttk.Button(frame, text="Generate", command=generate_password).grid(
    row=1, column=1, sticky="ew", padx=(6, 0), pady=(0, 8)
)

# Row 2: Clear (left) and Quit (right)
ttk.Button(frame, text="Clear", command=clear).grid(
    row=2, column=0, sticky="ew", padx=(0, 6)
)
ttk.Button(frame, text="Quit", command=root.destroy).grid(
    row=2, column=1, sticky="ew", padx=(6, 0)
)

# Row 3: Feedback label spanning both columns
ttk.Label(frame, textvariable=status, wraplength=360).grid(
    row=3, column=0, columnspan=2, pady=(12, 0)
)

root.mainloop()
