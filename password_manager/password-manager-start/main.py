from tkinter import *
import string
from tkinter import messagebox
import pyperclip

import random
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    a = random.randint(3,6)
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = random.sample(numbers, a)
    capital_letters = list(string.ascii_uppercase)
    uppercase = random.sample(capital_letters, a)
    small_letters = list(string.ascii_lowercase)
    lowercase = random.sample(small_letters, a)
    special_char = list(string.punctuation)
    characters = random.sample(special_char, a)
    un_pass = num + uppercase + lowercase + characters
    random.shuffle(un_pass)
    final_pass = "".join(map(str, un_pass))
    password_entry.insert(END, string=f"{final_pass}")
    pyperclip.copy(final_pass)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website,message=f"These are the details you entered\n Email : {email}.\n "
                                                         f"Password : {password}.\n Is it ok to save? ")
    if is_ok:
     with open("password.txt","a") as data_file:
        data_file.write(f"{website} | {email} | {password}.\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)







# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.geometry("600x600")

canvas = Canvas(width=200, height=200,highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_image)
canvas.grid(column=0,row=0)

website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_entry = Entry(width=35)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0,"tanishkothari324@gmail.com")
password_entry = Entry(width=21)
generate_button = Button(text="Generate", width=10,command=generate_password)
add_button = Button(text="Add",width=33,command=save_password)



website_label.grid(column=0,row=1)
email_label.grid(column=0,row=2)
password_label.grid(column=0,row=3)
website_entry.grid(column=1,row=1,sticky="w",columnspan=2)
email_entry.grid(column=1,row=2,sticky="w",columnspan=2)
password_entry.grid(column=1, row=3, sticky="w")
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, sticky="w", columnspan=2)

window.mainloop()