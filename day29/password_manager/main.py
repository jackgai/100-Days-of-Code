from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave website name empty!")
        return

    try:
        with open("data.json", "r") as f:
            data = json.load(f)

            if website not in data:
                messagebox.showinfo(title="Error", message="No details for the website exists")
                return

            data_detail = data[website]
            password = data_detail["password"]
            email = data_detail["email"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Empty Data File")
    else:
        messagebox.showinfo(title="Find Result", message=f"Email: {email} \nPassword: {password}")
    finally:
        website_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_data():
    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
        return

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open("data.json", "w") as f:
            json.dump(new_data, f, indent=4)
    else:
        # update old data with new data
        data.update(new_data)

        with open("data.json", "w") as f:
            # save updated data
            json.dump(data, f, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

user_name_label = Label(text="Email/Username:")
user_name_label.grid(column=0, row=2)

user_name_entry = Entry(width=35)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "haha@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=10, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=write_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="search", width=10, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
