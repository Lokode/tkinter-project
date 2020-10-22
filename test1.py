# import tkinter as tk
# import yogaposes
# from PIL import ImageTk, Image


# app = tk.Tk()


# def newbutton():  
#     newbtn = tk.Button(app, text = "button1", command =btn3)
#     newbtn.pack() 
#     newbtn2 = tk.Button(app, text = "button2")
#     newbtn2.pack() 
#     buttonExample.config(state=tk.DISABLED)
        
# def btn3():
#     newbtn3 = tk.Button(app, text = "button3")
#     newbtn3.pack() 
#     newbutton.newbtn.config(state=tk.DISABLED)


# buttonExample = tk.Button(app, text="Create new window", command=newbutton)
# buttonExample.pack()

# app.mainloop()
# --------------------------------------
# from tkinter import *
# fenster = Tk()
# fenster.title("Window")

# def switch():
#     b1["state"] = DISABLED

# #--Buttons
# b1=Button(fenster, text="Button")
# b1.config(height = 5, width = 7)
# b1.grid(row=0, column=0)    

# b2 = Button(text="disable", command=switch)
# b2.grid(row=0,column=1)

# fenster.mainloop()
# --------------------------
# import tkinter as tk
# from tkinter.filedialog import askdirectory
# import os

# img_list = []

# def save_to_list(event):
#     click_loc = [event.x, event.y]
#     print ("you clicked on", click_loc)
#     img_list.append(click_loc)

# def next_img():
#     img_label.img = tk.PhotoImage(file=next(imgs))
#     img_label.config(image=img_label.img)

# root = tk.Tk()
# root.geometry('500x500')
# # Choose multiple images
# img_dir = askdirectory(parent=root, initialdir="./yoga_Images/", title='Choose folder')
# os.chdir(img_dir)
# imgs = iter(os.listdir(img_dir))

# img_label = tk.Label(root)
# img_label.pack()
# img_label.bind("<Button-1>",save_to_list)

# btn = tk.Button(root, text='Next image', command=next_img)
# btn.pack()

# next_img() # load first image

# root.mainloop()

# print (img_list)
# --------------------------
# import tkinter as tk
# import glob
# from PIL import Image, ImageTk
# root = tk.Tk()
# root.geometry('600x600')


# pics = glob.glob("./yoga_Images/*.png")
# photosresized = []
# basewidth = 20
# for i in pics:
#     single_image = Image.open(i)
#     wpercent = (basewidth / float(single_image.size[0]))
#     hsize = int((float(single_image.size[1]) * float(wpercent)))
#     changed_size = single_image.resize((basewidth,hsize),Image.ANTIALIAS)
#     pid = ImageTk.PhotoImage(single_image.resize((basewidth,hsize),Image.ANTIALIAS))
#     photosresized.append(pid)
# label = tk.Label()
# label.photosresized = photosresized
# label.counter = 0
# def changeimage():
#     label['image'] = label.photosresized[label.counter%len(label.photosresized)]
#     label.after(3000, changeimage)
#     label.counter += 1
# label.pack()
# changeimage()

# root.mainloop()
# ----------------------------------------------------------------
# import tkinter as tk
# from PIL import Image, ImageTk
# import glob, os

# # --- functions ---

# def on_click(event=None):
#     print("image clicked")

# # --- main ---

# # init    
# root = tk.Tk()

# # load image
# pics = glob.glob("./Visionboard/*.png")
# photo = [tk.PhotoImage(file=x) for x in pics]
# l = tk.Label(root, image=photo)
# l.photo = photo
# l.counter = 0
# def changeimage():
# 	l['image'] = l.photo[l.counter%len(l.photo)]
# 	l.after(8000, changeimage)
# 	l.counter += 1
# l.pack()
# changeimage()

# # bind click event to image
# l.bind('<Button-1>', on_click)

# # button with image binded to the same function 
# b = tk.Button(root, image=photo, command=on_click)
# b.pack()

# # button with text closing window
# b = tk.Button(root, text="Close", command=root.destroy)
# b.pack()

# # "start the engine"
# root.mainloop()
# --------------------------------------
# import tkinter as tk
# import glob
# root = tk.Tk()
# from PIL import ImageTk, Image
# import random

# root.geometry('600x600')

# pics = glob.glob("./yoga_Images/*.png")
# photos = [tk.PhotoImage(file=x) for x in pics]
# random.shuffle(photos)
# label = tk.Label(root)
# label.photos = photos
# label.counter = 0
# def changeimage():
#     label['image'] = label.photos[label.counter%len(label.photos)]
#     label.after(8000, changeimage)
#     label.counter += 1
# label.pack(padx=10, pady=10)
# changeimage()
# root.mainloop()
# ------------------------------------------
# from PIL import ImageTk, Image
# import tkinter as tk
# import webbrowser, glob

# def example():
#     webbrowser.open_new('https://www.google.com')

# root = tk.Tk()

# # image = glob.glob("*.png")
# # btnPhoto = [ImageTk.PhotoImage(file=x) for x in image]
# image = glob.glob("*.png")
# btnPhoto= ImageTk.PhotoImage(image)

# imgBtn = tk.Button(root, image=btnPhoto, command=example)
# imgBtn.pack()

# root.mainloop()

# ///////////
# from io import BytesIO
# import tkinter as tk
# import urllib.request
# from PIL import Image, ImageTk

# root = tk.Tk()
# url = "http://imgs.xkcd.com/comics/python.png"

# u = urllib.request.urlopen(url)
# raw_data = u.read()
# u.close()

# im = Image.open(BytesIO(raw_data))
# image = ImageTk.PhotoImage(im)
# label = tk.Label(image=image)
# label.pack()
# root.mainloop()
# ----------------------
# from tkinter import *
# from glob import glob

# class ImageFrame(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.images = glob("./Visionboard/*.png")
#         self.cur = 0
#         # label showing the image
#         self.image = PhotoImage()
#         imagelabel = Label(self, image=self.image)
#         imagelabel.grid(row=1, column=1)
#         # button cycling through the images
#         button = Button(self, text="NEXT", command=self.show_next)
#         button.grid(row=2, column=1)
#         # layout and show first image
#         self.grid()
#         self.show_next()

#     def show_next(self):
#         self.cur = (self.cur + 1) % len(self.images)
#         self.image.configure(file=self.images[self.cur])

# ImageFrame().mainloop()

# ----
# import tkinter as tk
# from PIL import Image, ImageTk
# import yoga_Images
# import yogaposes
# import time

# root = tk.Tk()
# frame1 = tk.Frame(root)
# frame1.pack(anchor='center')

# frame2 = tk.Frame(root)
# frame2.pack(anchor='center')

# print("What shall I remind you about?")
# text = str(input())
# print("In how many minutes?")
# local_time = float(input())
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)


# def hamstringdrops():
#     hamstring_opt = o
#     hamstring_opt.config(width=50, font=('Helvetica', 12))
#     hamstring_opt.pack(side = 'top')

# def backdrops():
#     back_opt = b
#     back_opt.config(width=50, font=('Helvetica', 12))
#     back_opt.pack(side = 'top')

# def hamstring_images(b1):
#     print(b1)  # selected option
#     my_image.config(image=yoga_dict1[b1])
    
# def backposes_images(b2):
#     print(b2)  # selected option
#     backposesimg.config(image=yoga_dict2[b2])

# yoga_dict1 = {}
# for yoga_name1 in yogaposes.hamstringposes:
#     yoga_dict1[yoga_name1] = ImageTk.PhotoImage(Image.open("./yoga_Images/{}.png".format(yoga_name1)))

# yoga_dict2 = {}
# for yoga_name2 in yogaposes.backposeslist:
#     yoga_dict2[yoga_name2] = ImageTk.PhotoImage(Image.open("./yoga_Images/{}.png".format(yoga_name2)))
    
# variable1 = tk.StringVar(root)
# variable1.set(yogaposes.hamstringposes[0])

# variable2 = tk.StringVar(root)
# variable2.set(yogaposes.backposeslist[0])

# o = tk.OptionMenu(frame1, variable1, *yogaposes.hamstringposes, command=hamstring_images)
# b = tk.OptionMenu(frame2, variable2, *yogaposes.backposeslist, command=backposes_images)

# my_image = tk.Label(frame1)
# my_image.pack(side = 'bottom')
# backposesimg = tk.Label(frame2)
# backposesimg.pack(side = 'bottom')

# def refreshhamstring():
#     frame1.pack_forget() if frame1.winfo_manager() else frame1.pack(anchor='center')

# def refreshbackposes():
#     frame2.pack_forget() if frame2.winfo_manager() else frame2.pack(anchor='center')
    
# hamstring_k = tk.Button(root, text="Hamstring", command=lambda:[hamstringdrops(), refreshhamstring()])
# hamstring_k.pack(side = 'top')

# backposes_k = tk.Button(root, text="Back and Hips", command=lambda:[backdrops(), refreshbackposes()])
# backposes_k.pack(side='top')
# root.mainloop()
# ----------------------
# import tkinter as tk, threading
# import imageio
# from PIL import Image, ImageTk

# video_name = "/Users/loh/Documents/Python/Project_tkinter/Ilayaraja.mp4" #This is your video file path
# video = imageio.get_reader(video_name)

# def stream(label):

#     for image in video.iter_data():
#         frame_image = ImageTk.PhotoImage(Image.fromarray(image))
#         label.config(image=frame_image)
#         label.image = frame_image

# if __name__ == "__main__":

#     root = tk.Tk()
#     my_label = tk.Label(root)
#     my_label.pack()
#     thread = threading.Thread(target=stream, args=(my_label,))
#     thread.daemon = 1
#     thread.start()
#     root.mainloop()
# ----------------------
# import PySimpleGUI as sg

# sg.theme('DarkAmber')	# Add a touch of color
# # All the stuff inside your window.
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]

# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])

# window.close()
# ----------------------------

# import tkinter as tk
# import os
 
 
# def add(event):
#     "add item to listbox with entry when Return is pressed"
 
#     lst.insert(tk.END, entry.get())
#     v.set("")
 
 
# def delete(event):
#     "deletes items in listbox with double click on item"
#     lst.delete(tk.ANCHOR)
 
 
# def save(event):
#     "saves memos in listbox"
#     with open("data.txt", "w") as file:
#         file.write("\n".join(lv.get()))
#     label["text"] = "Data saved"
 
 
# def getdata():
#     "grab saved data"
#     if "data.txt" in os.listdir():
#         with open("data.txt") as file:
#             for line in file:
#                 lst.insert(tk.END, line.strip())
 
 
# root = tk.Tk()
# root.title("To do list in Python")
# lab1 = tk.Label(
#     root, text="Enter to add items, \nSelect to delete Items, ctr+s to save")
# lab1.pack()
 
# v = tk.StringVar()
# entry = tk.Entry(root, textvariable=v)
# entry.pack()
 
 
# lv = tk.Variable()
# lst = tk.insert(root, listvariable=lv, width = 30)
# lst.pack()
# lst.bind("<Double-Button>", delete)
 
# entry.bind("<Return>", add)
# root.bind("<Control-s>", save)
 
# label = tk.Label(root)
# label.pack()
 
# # Grab the saved data
# getdata()
 
# root.mainloop()

# ---------------------------------

# import tkinter as tk
# import tradinglists
# import musiclists
# from PIL import ImageTk, Image


# quoteswidth = 500
# btnsize_width = 20
# btnsize_height = 2
# artbtn_width = 14
# padylength = 10
# padxwidth = 10
# root = tk.Tk()
# root.geometry('800x700')
# root.title('Evrything')


# def importImageWithResize(filename):
#     img = Image.open(filename)
#     width, height = img.size
#     ratio = width / height
#     new_height = 300
#     new_width = int(new_height * ratio)
#     return img.resize((new_width, new_height ))

# class ShowHideButton(tk.Button):
#     def __init__(self, parent, target_widget, *args, **kwargs):
#         self.target = target_widget
#         super().__init__(parent, *args, **kwargs)
#         self.config(command=self.toggle)
#     def toggle(self, force_off = False):
#         if force_off or self.target.winfo_manager():
#             self.target.pack_forget()
#         else:
#             self.target.pack()
#         if isinstance(self.target, ShowHideButton):
#             self.target.toggle(force_off=True)


# def mt_images(m1t):
#     print(m1t)  # selected option
#     mt_label.config(image=mtimgz[m1t])
# mt_label = tk.Label(root)
# mt_label.pack(side = 'bottom', pady=10)
# mtimgz = {}
# for mt_name in tradinglists.retracements:
#     mtimgz[mt_name] = ImageTk.PhotoImage(root("/Users/loh/Documents/Python/Project_tkinter/Stocks/Retracements/{}.png".format(mt_name)))
# mtvar = tk.StringVar(root)
# mtvar.set(tradinglists.retracements[0])
# mt = tk.OptionMenu(root, mtvar, *tradinglists.retracements, command=mt_images)
# mt_opt = mt
# mt_opt.config(width=50, font=('Helvetica', 12))
# mt_opt.pack()   

# def mtcomp_images(mtcomp1t):
#     print(mtcomp1t)  # selected option
#     mtcomp_label.config(image=mtcompimgz[mtcomp1t])
# mtcomp_label = tk.Label(root)
# mtcomp_label.pack(side = 'bottom', pady=10)
# mtcompimgz = {}
# for mtcomp_name in musiclists.composition:
#     mtcompimgz[mtcomp_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Music_images/Composition/{}.png".format(mtcomp_name)))
# mtcompvar = tk.StringVar(root)
# mtcompvar.set(musiclists.composition[0])
# mtcomp = tk.OptionMenu(root, mtcompvar, *musiclists.composition, command=mtcomp_images)
# mtcomp_opt = mtcomp
# mtcomp_opt.config(width=50, font=('Helvetica', 12))
# mtcomp_opt.pack()   

# btnsize_width = 20
# btnsize_height = 2
# padylength = 10
# padxwidth = 10

# piano_k = tk.Button(root, text="Piano", width = btnsize_width, height = btnsize_height)
# piano_k.pack(side='left', padx=10, pady=10)

# guitar_k = tk.Button(root, text="Guitar", width = btnsize_width, height = btnsize_height)
# guitar_k.pack(side='left', padx=padxwidth, pady=padylength)

# production = tk.Button(root, text="Production", width = btnsize_width, height = btnsize_height)
# production.pack(side='left', padx=padxwidth, pady=padylength)

# theory_k_sightreading_k = ShowHideButton(root, mt_opt, text='Sight Reading')
# theory_k_composition_k = ShowHideButton(root, mtcomp_opt, text='Composition')
# theory_k = ShowHideButton(root, theory_k_sightreading_k, text='Music theory')
# theory_k.pack(side='left', padx=padxwidth, pady=padylength)

# root.mainloop()
# 
# -----------------------------

# import tkinter as tk
# import tkinter.scrolledtext as ScrolledText

# # def copy_command():
# #     root.clipboard_clear()
# #     text = textPad.get("sel.first", "sel.last")
# #     root.clipboard_append(text)

# # def paste_command():
# #     text = root.selection_get(selection='CLIPBOARD')
# #     textPad.insert('insert', text)

# root = tk.Tk(className=" PyWriter")

# textPad = ScrolledText.ScrolledText(root, width=100, height=80)

# menu = tk.Menu(root)
# root.config(menu=menu)

# # filemenu = tk.Menu(menu)
# # menu.add_cascade(label="File", menu=filemenu)
# # filemenu.add_command(label="Copy", command=copy_command)
# # filemenu.add_command(label="Paste", command=paste_command)

# textPad.pack()

# # # Grab the saved data
# # getdata()
# root.mainloop() 
# ----------
# from tkinter import *

# root = Tk()

# with open("savedtext.txt", "r") as f:
#     Label(root, text=f.read()).pack()

# root.mainloop()

# ------------

def zoom_at(img, x, y, zoom):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)