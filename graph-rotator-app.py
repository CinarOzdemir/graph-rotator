import tkinter as tk
from tkinter import messagebox
import pyperclip


# Convert the graph equation in the textbox
def convert_text(event=None):
    pyperclip.copy(
        entry.get()
        .replace("x", "(x*cos(a)-ğ*sin(a))")
        .replace("y", "(x*sin(a)+y*cos(a))")
        .replace("ğ", "y")
    )
    messagebox.showinfo(
        "Conversion Result", "Converted graph has been copied to clipboard"
    )


# Convert the graph equation in the clipboard
def convert_clipboard(event=None):
    pyperclip.copy(
        pyperclip.paste()
        .replace("x", "(x*cos(a)-ğ*sin(a))")
        .replace("y", "(x*sin(a)+y*cos(a))")
        .replace("ğ", "y")
    )
    messagebox.showinfo(
        "Conversion Result", "Converted graph has been copied to clipboard"
    )


# Create the main window
app = tk.Tk()
app.title("Graph Rotator App")

try:
    app.iconbitmap("icons8_rotate_left.ico")
except:
    ...
# Create and place a textbox in the window
entry = tk.Entry(app, width=40)
entry.pack(pady=10, padx=20)

# Bind the Enter key to the convert_text function
entry.bind("<Return>", convert_text)

# Create and place "Convert Clipboard" button
convert_clipboard_button = tk.Button(
    app, text="Convert Clipboard", command=convert_clipboard
)
convert_clipboard_button.pack(side=tk.BOTTOM, pady=10)

# Create and place "Convert Text" button
convert_button = tk.Button(app, text="Convert Text", command=convert_text)
convert_button.pack(side=tk.BOTTOM)

# Run the application
app.mainloop()
