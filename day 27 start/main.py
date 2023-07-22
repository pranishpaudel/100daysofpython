import tkinter
window= tkinter.Tk()

window.title("My first GUI")

window.minsize(width= 500, height=300)

label= tkinter.Label(text="I am a label", font=("Arial",24,"bold"))
label.pack()


window.mainloop()