from tkinter import Tk, Canvas, PhotoImage, Button
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    quote_data = response.json()
    canvas.itemconfig(quote_text, text=quote_data["quote"])

window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady=50)

# Update the file path for background.png to its full path
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="/Users/benlinn/Python Course/100DaysOfCode/Solution+kanye-quotes-end (1)/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click Kanye for a quote!", width=250, font=("Arial", 24, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Update the file path for kanye.png to its full path
kanye_img = PhotoImage(file="/Users/benlinn/Python Course/100DaysOfCode/Solution+kanye-quotes-end (1)/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()
