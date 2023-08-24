BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
card = {}
current_card = {}

def french_word():
    global card, flip_timer
    window.after_cancel(flip_timer)
    import random
    card = random.choice(current_card)
    canvas.itemconfig(canvas_text_1, text="French", fill="black")
    canvas.itemconfig(canvas_text_2, text=card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=img_photo_old)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=img_photo_new)
    canvas.itemconfig(canvas_text_1, text="English", fill="White")
    canvas.itemconfig(canvas_text_2, text=card["English"], fill="White")

def is_known():

    current_card.remove(card)
    data = pandas.DataFrame(current_card)
    data.to_csv("data/words_to_learn.csv")
    french_word()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
try:
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    current_card = original_data.to_dict(orient="records")
else:
    current_card = data.to_dict(orient="records")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
img_photo_old = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=img_photo_old)

img_photo_new = PhotoImage(file="images/card_back.png")


canvas_text_1 = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_text_2 = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, command=is_known)
button_right.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, command=french_word)
button_wrong.grid(row=1, column=0)



french_word()
window.mainloop()