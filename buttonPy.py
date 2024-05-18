from tkinter import *
from PIL import  Image, ImageTk



count = 0

def click():
     global count
     count += 1
     print(count)

window = Tk()
image =  Image.open("car.png")
icon = ImageTk.PhotoImage(image)

button  = Button(window,
                 text="click me",
                 command=click,
                 font=("Comic Sans",30),
                 fg="#00ff00",
                 bg="black",
                 activeforeground="#00ff00",
                 activebackground="black",
                 state=ACTIVE,
                 image=icon,
                 compound="top"
                 )

button.pack()

window.mainloop()

