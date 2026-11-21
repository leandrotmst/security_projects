import tkinter as tk
from tkinter import ttk

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
    if len(password) < 8:
        status.set("Password is too short! (min 8 characters)")
    else:
        status.set("Password length looks good.")


def generate_password():
    contents.set("Test")
    status.set("Generated a sample password.")


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
ttk.Label(frame, textvariable=status).grid(
    row=3, column=0, columnspan=2, pady=(12, 0)
)

root.mainloop()
