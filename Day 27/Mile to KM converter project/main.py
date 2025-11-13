from tkinter import *

KM = 1.6
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=30)

def button_clicked():
    result = mile_to_km(float(entry.get()))
    output_label.config(text=f"{result:.2f}")

def mile_to_km(mile=0.0):
    calculate = mile * KM
    return calculate


#is Equal to
ie_label = Label(text="is equal to", font=("Arial", 10, "bold"))
ie_label.grid(column=0, row = 1)

#Entries of number
entry = Entry(width=10,)
#Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=1, row = 0)

#output number label
output_label = Label(text="0", font=("Arial", 10, "bold"))
output_label.grid(column=1, row = 1)

#Miles label
miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row = 0)

#km label
km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=2, row =1)

#calculate button
button_calculate = Button(text="Calculate", command=button_clicked)
button_calculate.grid(column=1, row = 2)
window.mainloop()