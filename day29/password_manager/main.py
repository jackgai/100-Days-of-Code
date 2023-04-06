from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_data():
    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as f:
        save_content = f"{website} | {email} | {password}\n"
        f.write(save_content)
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

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
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

generate_button = Button(text="Generate Password", width=10)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=write_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
