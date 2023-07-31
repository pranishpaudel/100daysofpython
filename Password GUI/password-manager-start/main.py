# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

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
website_entry.grid(row=1,column=1)
email_entry= Entry(width=35)
email_entry.grid(row=2,column=1)
password_entry= Entry(width=21)
password_entry.grid(row=3,column=1)

window.mainloop()