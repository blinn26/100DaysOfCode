from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
flip_timer = None

# Base directory path
BASE_PATH = "/Users/benlinn/Python Course/100DaysOfCode/Solution+-+flash-card-project-end"


def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)

    if not to_learn:  # Check if the list is empty
        return

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    if current_card in to_learn:
        to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv(f"{BASE_PATH}/data/words_to_learn.csv", index=False)
    next_card()


# Load data and handle potential FileNotFoundError
try:
    data = pandas.read_csv(f"{BASE_PATH}/data/words_to_learn.csv")
    if data.empty:
        raise pandas.errors.EmptyDataError
    to_learn = data.to_dict(orient="records")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv(f"{BASE_PATH}/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

# GUI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=f"{BASE_PATH}/images/card_front.png")
card_back_img = PhotoImage(file=f"{BASE_PATH}/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=f"{BASE_PATH}/images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=f"{BASE_PATH}/images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()
