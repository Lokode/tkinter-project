from tkinter import *
root = Tk()     #you must create an instance of Tk() first

image = PhotoImage(file='zigzag.png')
larger_image = image.zoom(2, 2)         #create a new image twice as large as the original
smaller_image = image.subsample(2, 2) 

root.mainloop()