from tkinter import *
from tkinter import messagebox
import string
import random
desired_length=10


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_it():
    website_entryy= website_entry.get()
    password_entryy= password_entry.get()
    email_entryy= email_entry.get()

    if not website_entryy.strip() or not password_entryy.strip() or not email_entryy.strip():
     messagebox.showinfo(title="Oops", message= "Please make sure you haven't made any fields empty")
    else:
        is_ok= messagebox.askokcancel(title=website_entryy, message=f"These are the details entered: \n {website_entryy} |{email_entryy} | {password_entryy} \n Is it okay to save?")
        if is_ok:
                file= open("Password GUI/password-manager-start/savedata.txt", mode= "a")
                file.write(f"{website_entryy} |{email_entryy} | {password_entryy} \n")
                file.close()


# ----------------\----------- UI SETUP ------------------------------- #
def generate_random_password(length=10):
    password_entry.delete(0, END)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.insert(0,password)




window= Tk()


window.title("Password Manager")
window.config(padx= 50, pady= 50, bg="white")

canvas= Canvas(width= 200, height= 200, bg="white", highlightbackground="white")
pass_img= PhotoImage(file="Password GUI/password-manager-start/logo.png")
canvas.create_image(100,100, image=pass_img)
canvas.grid(column=1, row=0)

website_label= Label(text="Website")
website_label.grid(row=1, column=0)
email_label= Label(text="Email/Username")
email_label.grid(row=2, column=0)
passoword_label= Label(text="password")
passoword_label.grid(row=3, column=0)

#entry
website_entry= Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
email_entry= Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0,"insa@gmail.com")
password_entry= Entry(width=21)
password_entry.grid(row=3,column=1)

#buttons
generate_pass_button= Button(text="Generate Password",command=generate_random_password)
generate_pass_button.grid(row=3, column=2)
add_button= Button(text="Add",width=36, command=add_it)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()