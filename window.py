# from tkinter import *



# window = Tk();
# window.geometry("420x420")

# window.title("Nick widnow  ")

# icon = PhotoImage(file='car.png')

# window.iconphoto(True,icon)
# window.mainloop()

# window.config(background="#eeefff")

from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("420x420")
window.title("Nick window")

# Use Pillow to open the image
image = Image.open('car.png')
icon = ImageTk.PhotoImage(image)

window.iconphoto(True, icon)
window.config(background="#eeefff")

window.mainloop()
