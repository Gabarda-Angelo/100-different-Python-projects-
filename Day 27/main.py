#Creating GUI lesson
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
#notes: some argument has default parameters value, and some argument  has "required arguments"
my_label.pack()

my_label["text"] = "New Text"
#they are only the same


#Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=18)
input.pack()






window.mainloop()