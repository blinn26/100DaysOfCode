from tkinter import *
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# You can fill this in later.

# ---------------------------- SAVE PASSWORD ------------------------------- #
# You can fill this in later.

# ---------------------------- UI SETUP ------------------------------- #


def get_image_path(filename):
    """
    Returns the absolute path of the given filename if it exists in the same directory as the script.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, filename)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)

# Try to load the logo using the absolute path
logo_img_path = get_image_path("logo.png")

if os.path.exists(logo_img_path):  # Check if the file exists before loading it
    logo_img = PhotoImage(file=logo_img_path)
    canvas.create_image(100, 100, image=logo_img)
else:
    print(f"Error: '{logo_img_path}' does not exist!")

canvas.pack()
window.mainloop()
