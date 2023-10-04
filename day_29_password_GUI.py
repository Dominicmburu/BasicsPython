from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

## constants
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


## PASSWORD GENERATOR
def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!''#''$''%''&''('')''*''+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)



## SAVE PASSWORD
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("day_29_password.json", mode="r") as data_file:
                ##reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("day_29_password.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            ##updating old data
            data.update(new_data)
        
            with open("day_29_password.json", mode="w") as data_file:
                # saving the updated data
                json.dump(data, data_file, indent=4)
            
            messagebox.showinfo(title="Sucess", message="Data Saved Successfully.")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



## SEARCH PASSWORD
def find_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left this field empty.")
    else:
        try:
            with open("day_29_password.json", mode="r") as data_file:
                ##reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



## UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=210, height=210, bg=YELLOW, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(105, 105, image=pass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 12), bg=YELLOW)
website_label.grid(column=0, row=1)

website_entry = Entry(width=39)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12), bg=YELLOW)
email_label.grid(column=0, row=2)

email_entry = Entry(width=59)
email_entry.insert(0, "dominic@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=(FONT_NAME, 12), bg=YELLOW)
password_label.grid(column=0, row=3)

password_entry = Entry(width=39)
password_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", command=generate_password, width=15)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=50, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()






















