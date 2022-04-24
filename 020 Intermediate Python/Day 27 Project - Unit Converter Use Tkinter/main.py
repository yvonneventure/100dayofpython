from tkinter import *  #import all classes in tkinster

window=Tk()
window.title("Mile to Km Converter")
window.minsize(300,300)
window.config(padx=20,pady=20)  #add some margin/edge/space to the screen


label1 = Label(text="Miles",font=("Arial",24,"normal"))
label1.grid(column=3,row=1)
label2 = Label(text="is equal to",font=("Arial",24,"normal"))
label2.grid(column=1,row=2)
label3 = Label(text="0", font=("Arial", 24, "normal"))
label3.grid(column=2, row=2)

label4 = Label(text="Km",font=("Arial",24,"normal"))
label4.grid(column=3,row=2)

def buttonclick():
    label3 = Label(text=f"{int(input.get())*1.3}", font=("Arial", 24, "normal"))
    label3.grid(column=2, row=2)

input = Entry(width=10)

input.grid(column=2,row=1)




button=Button(text="calculate",command=buttonclick)
button.grid(column=2,row=3)

window.mainloop()