from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------------- READ DATA ------------------------------- #
try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    word_dict = data.to_dict(orient="records")


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------------------------- PICK CARD ------------------------------- #
def pick_card():
    global current_card, timer
    window.after_cancel(timer)

    current_card = choice(word_dict)
    canvas.itemconfig(canvas_img, image=card_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    window.after(3000, func=flip_card)


# ---------------------------- REMOVE CARDS ------------------------------- #
def remove_card():
    word_dict.remove(current_card)
    save_cards()


# ---------------------------- SAVE NEED TO LEARN CARDS ------------------------------- #
def save_cards():
    df = pd.DataFrame(word_dict)
    df.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_img = PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image(800 / 2, 526 / 2, image=card_img)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

check_img = PhotoImage(file="images/right.png")

right_button = Button(image=check_img, highlightthickness=0, command=lambda: [remove_card(), pick_card()])
right_button.grid(column=0, row=1)

cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=pick_card)
wrong_button.grid(column=1, row=1)

card_back_img = PhotoImage(file="images/card_back.png")

pick_card()

window.mainloop()
