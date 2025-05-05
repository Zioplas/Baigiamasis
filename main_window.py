from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry("500x500")

# Load images
image1 = ImageTk.PhotoImage(Image.open(r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\dollar.png").resize((100,100)))
image2 = ImageTk.PhotoImage(Image.open(r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\dollar.png").resize((100,100)))
image3 = ImageTk.PhotoImage(Image.open(r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\dollar.png").resize((100,100)))

frame = Frame(window)
frame.pack()

label1 = Label(frame, image=image1, relief="sunken")
label2 = Label(frame, image=image2, relief="sunken")
label3 = Label(frame, image=image3, relief="sunken")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

window.mainloop()
