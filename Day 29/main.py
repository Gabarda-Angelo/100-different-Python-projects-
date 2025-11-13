
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Combine characters into a single list

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_button_clicked():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()





    if len(website_text) == 0 or len(email_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Message", message="please don't leave any fields empty")
    else:
        is_ok = messagebox.showinfo(title="Message", message=f"These are the details entered: \nEmail: {email_text} "
                                                             f"\bPassword: {password_text}\nIs it ok to save?")
        if is_ok:
            save_to_files(website_text, email_text, password_text)
            clear_entries()





def save_to_files(website, email, password):
    new_account = f"{website} | {email} | {password}\n"
    # save into a file:
    with open(f"user_account.txt", mode="a") as file:
        file.write(new_account)

def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
accounts = []



canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0 )
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2, sticky="EW")
email_entry.insert(0, "angelo@gmail.com")
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1, sticky="W")

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=35, command=save_button_clicked)
add_button.grid(row=4, column=1,columnspan=2, sticky="EW")

window.mainloop()



