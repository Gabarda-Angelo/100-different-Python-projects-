from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FG_COLOR_WHITE = "#FFFFFF"

current_card = {}
to_learn = {}
flip_timer = None

try: #see if words_to_learn.csv is existing
    data = pandas.read_csv("data/french_words.csv")

except FileNotFoundError:#If the words_to_learn.csv does not exist (i.e., the first time the program is run)
    original_data = pandas.read_csv("data/french_words.csv")
    #convert from Data frame to dictionary
    to_learn = original_data.to_dict(orient="records")
else:
    #convert from Data frame to dictionary
    to_learn = data.to_dict(orient="records")


# ----------------------------Save your progress------------------------------- #
def is_known():
    # Removes the current card from the list and saves progress


    # Removes the current card from the list
    to_learn.remove(current_card)

    # Convert the updated list back to a DataFrame
    new_data = pandas.DataFrame(to_learn)

    # Save the updated list into words_to_learn.csv
    '''
        By default, Pandas automatically includes an index when saving a DataFrame to a CSV 
        unless you explicitly tell it not to by setting index=False.
        you don't want to have this like a three column. 
        
        , French,English
        0,chaque,each
        1,parlé,speak
        2,arrivé,come
    '''
    new_data.to_csv("data/words_to_learn.csv", index=False)

    print("Progress saved. Removed:", current_card)
    next_card()



# ---------------------------- Flip the Cards------------------------------- #
def flip_card():
    global current_card

    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, fill=FG_COLOR_WHITE)
    canvas.itemconfig(card_word, fill=FG_COLOR_WHITE)

    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])





# ---------------------------- Create New Flash Cards ------------------------------- #
def next_card():
    global current_card,flip_timer
    '''why to cancel the timer?
       -The problem arises if next_card() is called again before the 3-second timer completes. 
       EX: User clicks the “right” or “wrong” button (calling next_card()) before the 3-second timer finishes.
       -This starts a new timer (overwriting timer with a new ID) but leaves the previous window.after(3000, flip_card) timer running.
       -If the old timer isn’t canceled, it could trigger flip_card() unexpectedly, causing the card to flip at the wrong time (e.g., flipping a new card prematurely).
       '''
    # Cancel previous timer safely if it exists
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    # Pick a random word
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)

    # Start a new timer to flip after 3 seconds
    flip_timer = window.after(3000, flip_card)







# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")
# window.minsize(width=800, height=526)
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)




canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
#image
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")


canvas_image = canvas.create_image(400,263, image=front_img)

canvas.grid(row=0,column=0, columnspan=2)


#Text
card_title = canvas.create_text(400, 150, text="",font=("Arial",40,"italic"))
card_word = canvas.create_text(400, 263, text="",font=("Arial",60,"bold"))


#Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, borderwidth=0, command=next_card)  # Added command for testing
unknown_button.grid(row=1, column=0)# Place button on canvas

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, borderwidth=0, command=is_known)  # Added command for testing
known_button.grid(row=1, column=1)# Place button on canvas



next_card()
window.mainloop()


'''
Yes, the line timer = window.after(3000, flip_card) schedules the flip_card() function to 
execute after a 3-second delay, but it does not block the execution of other code. 
The window.after method is non-blocking, meaning it sets up a timer in the Tkinter event loop and immediately 
continues with the next line of code. In this case, after scheduling flip_card(), the program proceeds to execute 
next_card() without waiting for the 3-second delay to complete.
'''


'''
The mainloop() method starts an infinite event loop that keeps the window open and responsive to user interactions,
 but it does not repeatedly execute the code that comes before it. Any function, like next_card(), 
 placed before window.mainloop() will execute only once as part of the program's normal flow, 
 before the event loop starts.

'''

