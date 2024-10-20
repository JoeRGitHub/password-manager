from tkinter import *
from tkinter import messagebox
import string
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password with X length
# The password will be created from s1 to s4 list
# All characters will be random from all lists - Uppercase, Lowercase, Numbers Symbols
db_digit = string.printable


def create_random_pass(password_length=10):
    password = random.choices(db_digit, k=password_length) # With 'choices' no need the loop
    return ''.join(password) # Generate the password as a single string


def password_manager():
    new_pass = create_random_pass()
    pass_entry.delete(0, 'end')  # Clear the previous password in the entry
    pass_entry.insert(0, new_pass)  # Insert the newly generated password
    pass_entry.clipboard_clear()
    pass_entry.clipboard_append(new_pass)  # Copy the string to clipboard
    print(new_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    print(use_email_entry.get())
    print(website_entry.get())
    print(pass_entry.get())
    website = website_entry.get()
    email = use_email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        print(len(website), len(email), len(password))
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        if messagebox.askokcancel(title="Info", message=f"Confident with saving information?\n "
                                                  f"Web: {website}"
                                                  f"\nEmail: {email} "
                                                  f"\nPass: {password} "):
            # Save data to file.text
            messagebox.showinfo(title="Info", message="Your information has been saved successfully.")
            f = open("db.txt", "a")
            f.write(f'\n{website_entry.get()} | {use_email_entry.get()} | {pass_entry.get()}')
            f.close()
            website_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')
            #popup()

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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
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
generate_button = Button(text="Generate Pass", command=password_manager)
generate_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)


windows.mainloop()