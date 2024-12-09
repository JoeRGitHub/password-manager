from tkinter import *
from tkinter import messagebox
import string
import random
import json


# ---------------------------- SEARCH ------------------------------- #


def search_record():
    website_search_record = website_entry.get().lower()
    try:
        with open("db.json", "r") as data_file:
            for key, value in json.load(data_file).items():
                if key == website_search_record:
                    email = value["Email"]
                    password = value["Password"]
                    messagebox.showinfo(title=f'{key}', message=f'Email:{email} \nPassword:{password}')
                    website_entry.delete(0, 'end')
                    break
            else:
                messagebox.showinfo(title="Oops", message="No record:" f'\n{website_search_record}')
    except FileNotFoundError:
        if website_search_record == '':
            messagebox.showinfo(title="No Data", message="Please add data to search")
        else:
            messagebox.showinfo(title="No Data", message="No record:" f'\n{website_search_record}')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password with X length
# The password will be created from s1 to s4 list
# All characters will be random from all lists - Uppercase, Lowercase, Numbers Symbols
db_digit = string.printable #ascii

def create_random_pass(password_length=10):
    password = random.choices(db_digit, k=password_length) # With 'choices' no need the loop
    return ''.join(password) # Generate the password as a single string


def password_manager():
    new_pass = create_random_pass()
    pass_entry.delete(0, 'end')  # Clear the previous password in the entry
    pass_entry.insert(0, new_pass)  # Insert the newly generated password
    pass_entry.clipboard_clear()
    pass_entry.clipboard_append(new_pass)  # Copy the string to clipboard
    # print(new_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # print(use_email_entry.get())
    # print(website_entry.get())
    # print(pass_entry.get())
    website = website_entry.get().lower()
    email = use_email_entry.get().lower()
    password = pass_entry.get()
    new_data = {
        website:{
            'Email': email,
            'Password': password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        #print(len(website), len(email), len(password))
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        if messagebox.askokcancel(title="Info", message=f"Save info?\n "
                                                  f"Web: {website}"
                                                  f"\nEmail: {email}"
                                                  f"\nPass: {password}"):

            messagebox.showinfo(title="Info", message="Password saved!")
            # Save data to file.text
            # with open("db.txt", "a") as database_file:
            #     database_file.write(f'\n{website} | {email} | {password}')

            # Save data to json file
            try:
                with open("db.json", "r") as data_file:
                    data = json.load(data_file)
                    # data.update(new_data)
                    print(data)

            except FileNotFoundError:
                with open("db.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            # If no data in file
            except json.decoder.JSONDecodeError:
                with open("db.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("db.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, 'end')
                pass_entry.delete(0, 'end')
            #popup()

# וUsed this solution before found messagebox
# def popup():
#     global top
#     top = Toplevel(windows)
#     top.geometry("350x100")
#     top.title("Approved Window")
#     Label(top, text="Info Saved!", font=('Ariel', 16, 'bold')).place(x=132, y=15)
#     Button(top, text="Close", font=('Poppins bold', 16), command=close_win).place(x=140, y=55)
#     top.transient(windows)  # set to be on top of the main window
#     top.grab_set()  # hijack all commands from the master (clicks on the main window are ignored)
#     windows.wait_window(top)  # pause anything on the main window until this one closes

# def close_win():
#     top.destroy()

# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title("Password Manager")
windows.config(padx=30, pady=30)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid (row=0,column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
use_email_label = Label(text="Email/Username:")
use_email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
## Add cursor to entry
website_entry.focus()
website_entry.insert(END, "")
use_email_entry = Entry(width=35)
use_email_entry.grid(row=2, column=1, columnspan=2)
use_email_entry.insert(END, "default_email@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)
pass_entry.insert(END, "")

# Button's
search_button = Button(text="Search", command=search_record, width=10)
search_button.grid(row=1, column=2, columnspan=2)
generate_button = Button(text="Generate Pass", command=password_manager, width=10)
generate_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)


windows.mainloop()