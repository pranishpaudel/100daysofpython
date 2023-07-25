from tkinter import *

window= Tk()

window.title("Mile to Km Convertor")
window.config(padx=20, pady=20)

def miles_to_km(miles):
    kilometers = float(miles) * 1.60934
    return kilometers



miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

def calculated():
    mile= miles_input.get()
    eq_km =miles_to_km(mile)
    kilometer_result_label["text"]= eq_km
    

calculate_button= Button(text="calculate", command=calculated)
calculate_button.grid(column=1, row=2)





window.mainloop()