from tkinter import *




clickss= "HI"
window= Tk()

window.title("My first GUI")

window.minsize(width= 500, height=300)


label= Label(text=clickss, font=("Arial",24,"bold"))
label.place(x=0,y=150)



def button_clicked():
    new_text= input.get()
    label["text"]= new_text

button= Button(text="Click Me", command= button_clicked, background="yellow")
button.pack()


input= Entry(width=10)

input.pack()
print(input.get())


window.mainloop()