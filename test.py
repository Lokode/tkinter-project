import tkinter as tk
from tkinter import ttk
import webbrowser
import os
import subprocess
from tkinter import messagebox
import random
import Spiritualquotes
import poems
import tradingquotes
from ttkthemes import ThemedStyle
import glob
import general_motivation
from PIL import ImageTk, Image
import yogaposes
import tradinglists
import musiclists

HEIGHT = 1000
WIDTH = 600

quoteswidth = 500
btnsize_width = 20
btnsize_height = 2
artbtn_width = 14
padylength = 10
padxwidth = 10
root = tk.Tk()
root.geometry('800x700')
root.title('Evrything')
style = ThemedStyle(root)
#Themes: breeze, arc, radiance
style.set_theme("breeze")

# ---------------------------------------------TAB 1---------------------------------------------

def importImageWithResize(filename):
    # img = Image.open(filename)
    # width, height = img.size
    # ratio = width / height
    # new_height = 380
    # new_width = int(new_height * ratio)
    # return img.resize((new_width, new_height ))
    abasewidth = 400
    imgr = Image.open(filename)
    w_percent = (abasewidth/float(imgr.size[0]))
    h_size = int((float(imgr.size[1])*float(w_percent)))
    return imgr.resize((abasewidth,h_size), Image.ANTIALIAS)


    
new = 1
def quicktradesetup():
    websites = ["https://www.tradingview.com/chart/I1C6VoNA/", "https://www.questrade.com", "https://docs.google.com/spreadsheets/d/1Bi8qv2YrXalvY88Sw0AhxjOnCS7xBbya5eMVCJ1rP4Q/edit?hl=en#gid=1240544488"]
    for urls in websites:
        webbrowser.open(urls, new=new)
        
def ytplaylist_web():
    ytplaylist_vibes = 'https://www.youtube.com/watch?v=FARTQn9JGEA&list=PLs0V5ImUmSnqfq0ZEN7vbbIldaP21yfJ9'
    webbrowser.open(ytplaylist_vibes, new=new)

def ambience_knowledge():
    ak = ["https://www.youtube.com/watch?v=WvQMiqNlKMM&list=PLs0V5ImUmSnqvDZ6orxyAdfSQRu6CVj5C", "https://www.youtube.com/watch?v=2IcrboiYDIQ&list=PLs0V5ImUmSnrFLalbjovnq0hXphi3Utid"]
    for urls in ak:
        webbrowser.open(urls, new=new)

def QA_Interview_notes():
    ak = ["https://www.youtube.com/watch?v=WvQMiqNlKMM&list=PLs0V5ImUmSnqvDZ6orxyAdfSQRu6CVj5C", "https://www.youtube.com/watch?v=EJm-N4B_odA&list=PLs0V5ImUmSnrFLalbjovnq0hXphi3Utid&index=13"]
    for urls in ak:
        webbrowser.open(urls, new=new)

def close_all_browsers():
    os.system("killall -9 'Google Chrome'")

tabControl=ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Quick Access")
tabControl.pack(expand=6, fill='both')

tab1btnsframe = tk.Frame(tab1)
tab1btnsframe.pack(anchor='center')
todolistframe = tk.Frame(tab1)
todolistframe.pack(anchor='center')

#Quick Access
tradesetup_button = tk.Button(tab1btnsframe, text="Trading setup", width = btnsize_width, height = btnsize_height, command=quicktradesetup)
tradesetup_button.pack(side = 'left', pady=padylength)

ytplaylist_button = tk.Button(tab1btnsframe, text="Vibes Playlist (YT)", width = btnsize_width, height = btnsize_height,command=ytplaylist_web)
ytplaylist_button.pack(side = 'left', pady=padylength)

ambience_k = tk.Button(tab1btnsframe, text="Ambience + Inner quest", width = btnsize_width, height = btnsize_height, command=ambience_knowledge)
ambience_k.pack(side = 'left', pady=padylength)

#Trading tab
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Trade setup")
tabControl.pack(expand=5, fill='both')

def openfolder():
    file_to_show = "/Users/loh/Documents/Python/Project_tkinter/test/"
    subprocess.call(["open", "-R", file_to_show])

def tradinv_tab2():
    tv_ = 'https://www.tradingview.com/chart/I1C6VoNA/'
    webbrowser.open(tv_, new=new)

def optionschain_tab2():
    opchain = 'https://www.td.com/ca/markets-research/options/options.jsp'
    webbrowser.open(opchain, new=new)

def watchlist_tab2():
    opchain = 'https://docs.google.com/spreadsheets/d/1Bi8qv2YrXalvY88Sw0AhxjOnCS7xBbya5eMVCJ1rP4Q/edit?hl=en#gid=1240544488'
    webbrowser.open(opchain, new=new)

# -----todo list-----
def add(event):
    "add item to listbox with entry when Return is pressed"

    lst.insert(tk.END, entry.get())
    v.set("")

def delete(event):
    "deletes items in listbox with double click on item"
    lst.delete(tk.ANCHOR)

def save(event):
    "saves memos in listbox"
    with open("data.txt", "w") as file:
        file.write("\n".join(lv.get()))
    label["text"] = "Data saved"

def getdata():
    "grab saved data"
    if "data.txt" in os.listdir():
        with open("data.txt") as file:
            for line in file:
                lst.insert(tk.END, line.strip())

lab1 = tk.Label(
    todolistframe, text="Enter to add tasks, \nDouble click to delete Items, ctr+s to save")
lab1.pack()

v = tk.StringVar()
entry = tk.Entry(todolistframe, textvariable=v, width = 30)
entry.pack() 

lv = tk.Variable()
lst = tk.Listbox(todolistframe, listvariable=lv, width = 30)
lst.pack()
lst.bind("<Double-Button>", delete)

entry.bind("<Return>", add)
root.bind("<Control-s>", save)

label = tk.Label(todolistframe)
label.pack()

# Grab the saved data
getdata()
# -----------    

#close all browser
closebrowsers = tk.Button(tab1, text="Close all browsers", width = btnsize_width, height = btnsize_height, command=close_all_browsers, justify="center")
closebrowsers.pack(padx=padxwidth, pady=50)


# ---------------------------------------------TAB2---------------------------------------------
# trading quotes   
frame_dd = tk.Frame(tab2)
frame_dd.place(relx = 0.5, rely = 0.7, anchor = "center")

label_dd = tk.Label(frame_dd,font="helvetica 14", wraplength=quoteswidth, justify="center")
label_dd.pack()
def kfbafter():
    label_dd.config(text=random.choice(tradingquotes.knowledgefrombooks))
    root.after(16000, kfbafter)
kfbafter()

ttk.Separator(tab2).place(x=0, y=550, relwidth=1)

frame_d = tk.Frame(tab2)
frame_d.place(relx = 0.5, rely = 0.9, anchor = "center")

label_d = tk.Label(frame_d,font="helvetica 14", wraplength=quoteswidth, justify="center")
label_d.pack()
def afterd():
    label_d.config(text=random.choice(tradingquotes.tradingquotes))
    root.after(15000, afterd)
afterd()


# tab2 buttons
tradingbtnframe = tk.Frame(tab2,bg='#ebf4f6')
tradingbtnframe.pack(side="top")
openfolder_btn = tk.Button(tradingbtnframe, text="Open folder", width = btnsize_width, height = btnsize_height, command=openfolder)
openfolder_btn.pack(side='left', padx=padxwidth, pady=padylength)
tradingview_btn = tk.Button(tradingbtnframe, text="Trading view", width = btnsize_width, height = btnsize_height, command=tradinv_tab2)
tradingview_btn.pack(side='left', padx=padxwidth, pady=padylength)
options_btn = tk.Button(tradingbtnframe, text="Options Chain", width = btnsize_width, height = btnsize_height, command=optionschain_tab2)
options_btn.pack(side='left', padx=padxwidth, pady=padylength)
watchlistxl_btn = tk.Button(tradingbtnframe, text="Watchlist xls", width = btnsize_width, height = btnsize_height, command=optionschain_tab2)
watchlistxl_btn.pack(side='left', padx=padxwidth, pady=padylength)

ttk.Separator(tab2).place(x=0, y=45, relwidth=1)

# -----waves buttons-------
wavebtnspadx = 2
wave1frame = tk.Frame(tab2)
wave1frame.pack(anchor='center')
wavebtnframe = tk.Frame(tab2)
wavebtnframe.pack(anchor='center')
waveABCframe = tk.Frame(tab2)
waveABCframe.pack(anchor='center',)
waveretraceframe = tk.Frame(tab2)
waveretraceframe.pack(anchor='center')
otherframe = tk.Frame(tab2)
otherframe.pack(anchor='center')

def wavesdrops():
    waves_opt = w
    waves_opt.config(width=50, font=('Helvetica', 12))
    waves_opt.pack()   
def waves_images(w1):
    print(w1)  # selected option
    waves_label.config(image=waves[w1])
waves_label = tk.Label(wave1frame)
waves_label.pack(side = 'bottom', pady=padylength)
waves = {}
for waves_name in tradinglists.allwavesimages:
    waves[waves_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Stocks/Waves/{}.png".format(waves_name)))
wavevariable = tk.StringVar(tab2)
wavevariable.set(tradinglists.allwavesimages[0])
w = tk.OptionMenu(wave1frame, wavevariable, *tradinglists.allwavesimages, command=waves_images)
def refreshwave():
    wave1frame.pack_forget() if wave1frame.winfo_manager() else wave1frame.pack(anchor='center')
wave_k = tk.Button(wavebtnframe, text="Waves", width = artbtn_width, height = btnsize_height, command=lambda:[wavesdrops(), refreshwave()])
wave_k.pack(side = 'left', padx=wavebtnspadx, pady=padylength)

def wavesABCdrops():
    wavesABC_opt = wABC
    wavesABC_opt.config(width=50, font=('Helvetica', 12))
    wavesABC_opt.pack()   
def wavesABC_images(w1ABC):
    print(w1ABC)  # selected option
    wavesABC_label.config(image=wavesABC[w1ABC])
wavesABC_label = tk.Label(waveABCframe)
wavesABC_label.pack(side = 'bottom', pady=padylength)
wavesABC = {}
for wavesABC_name in tradinglists.waveabcimages:
    wavesABC[wavesABC_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Stocks/ABC/{}.png".format(wavesABC_name)))
wavevariableABC = tk.StringVar(tab2)
wavevariableABC.set(tradinglists.waveabcimages[0])
wABC = tk.OptionMenu(waveABCframe, wavevariableABC, *tradinglists.waveabcimages, command=wavesABC_images)
def refreshwaveABC():
    waveABCframe.pack_forget() if waveABCframe.winfo_manager() else waveABCframe.pack(anchor='center')
waveABC_k = tk.Button(wavebtnframe, text="Corrective", width = artbtn_width, height = btnsize_height, command=lambda:[wavesABCdrops(), refreshwaveABC()])
waveABC_k.pack(side = 'left', padx=wavebtnspadx, pady=padylength)
    
def wavesretracedrops():
    wavesretrace_opt = wretrace
    wavesretrace_opt.config(width=50, font=('Helvetica', 12))
    wavesretrace_opt.pack()   
def wavesretrace_images(w1retrace):
    print(w1retrace)  # selected option
    wavesretrace_label.config(image=wavesretrace[w1retrace])
wavesretrace_label = tk.Label(waveretraceframe)
wavesretrace_label.pack(side = 'bottom', pady=padylength)
wavesretrace = {}
for wavesretrace_name in tradinglists.retracements:
    wavesretrace[wavesretrace_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Stocks/Retracements/{}.png".format(wavesretrace_name)))
wavevariableretrace = tk.StringVar(tab2)
wavevariableretrace.set(tradinglists.retracements[0])
wretrace = tk.OptionMenu(waveretraceframe, wavevariableretrace, *tradinglists.retracements, command=wavesretrace_images)
def refreshwaveretrace():
    waveretraceframe.pack_forget() if waveretraceframe.winfo_manager() else waveretraceframe.pack(anchor='center')
waveretrace_k = tk.Button(wavebtnframe, text="Retracements", width = artbtn_width, height = btnsize_height, command=lambda:[wavesretracedrops(), refreshwaveretrace()])
waveretrace_k.pack(side = 'left', padx=wavebtnspadx, pady=padylength)

def otherdrops():
    other_opt = wother
    other_opt.config(width=50, font=('Helvetica', 12))
    other_opt.pack()   
def other_images(wother):
    print(wother)  # selected option
    other_label.config(image=other[wother])
other_label = tk.Label(otherframe)
other_label.pack(side = 'bottom', pady=padylength)
other = {}
for other_name in tradinglists.tradingotherimages:
    other[other_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Stocks/Other/{}.png".format(other_name)))
    # other[other_name] = ImageTk.PhotoImage(Image.open("/Users/loh/Documents/Python/Project_tkinter/Stocks/Other/{}.png".format(other_name)))
othervariable = tk.StringVar(tab2)
othervariable.set(tradinglists.tradingotherimages[0])
wother = tk.OptionMenu(otherframe, othervariable, *tradinglists.tradingotherimages, command=other_images)
def refreshother():
    otherframe.pack_forget() if otherframe.winfo_manager() else otherframe.pack(anchor='center')
other_k = tk.Button(wavebtnframe, bg = "red", text="Other", width = artbtn_width, height = btnsize_height, command=lambda:[otherdrops(), refreshother()])
other_k.pack(side = 'left', padx=wavebtnspadx, pady=padylength)
# ---------------------------------------------SPIRITUAL TAB3---------------------------------------------
#Spirituality Tab
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Inner-quest")
tabControl.pack(expand=5, fill='both')
frame_c = tk.Frame(tab3)
frame_c.place(relx = 0.5, rely = 0.5, anchor = "center")
spiritframe = tk.Frame(tab3)
spiritframe.pack(side = 'top')
wordsframe = tk.Frame(tab3)
wordsframe.pack(anchor='center', pady=20)

def video():
    os.startfile('/Users/loh/Documents/Python/Project_tkinter/Ilayaraja.mp4')

vid = tk.Button(spiritframe, text="Play", width = btnsize_width, height = btnsize_height, command=video)
vid.pack(side='left', padx=padxwidth, pady=padylength)

def spirituality():
    label_c=tk.Label(wordsframe,text=random.choice(Spiritualquotes.foo), font="helvetica 14", wraplength=quoteswidth, justify="center")
    label_c.pack()
    root.after(7000, label_c.destroy)
myButton=tk.Button(spiritframe, text="Guide me", width = btnsize_width, height = btnsize_height, command=spirituality)
myButton.pack(side='left', padx=padxwidth, pady=padylength)

def poemsfortheeartandmind():
    label_c=tk.Label(wordsframe,text=random.choice(poems.poems), font="helvetica 14", wraplength=quoteswidth, justify="center")
    label_c.pack()
    root.after(10000, label_c.destroy)
myButton=tk.Button(spiritframe,text="Poem", width = btnsize_width, height = btnsize_height, command=poemsfortheeartandmind)
myButton.pack(side='left', padx=padxwidth, pady=padylength)


# ---------------------------------------------YOGA TAB4---------------------------------------------
#Yoga tab
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text="Yoga")
tabControl.pack(expand=5, fill='both')

def importyogaImageWithResize(filename):
    abasewidthy = 250
    imgy = Image.open(filename)
    w_percenty = (abasewidthy/float(imgy.size[0]))
    h_sizey = int((float(imgy.size[1])*float(w_percenty)))
    return imgy.resize((abasewidthy,h_sizey), Image.ANTIALIAS)

# dropdown
frame1 = tk.Frame(tab4)
frame1.pack(anchor='center')
frame2 = tk.Frame(tab4)
frame2.pack(anchor='center')
frame3 = tk.Frame(tab4)
frame3.pack(anchor='center')
frame4 = tk.Frame(tab4)
frame4.pack(anchor='center')

def hamstringdrops():
    hamstring_opt = o
    hamstring_opt.config(width=50, font=('Helvetica', 12))
    hamstring_opt.pack()

def backdrops():
    back_opt = b
    back_opt.config(width=50, font=('Helvetica', 12))
    back_opt.pack()

def energydrops():
    energy_opt = e
    energy_opt.config(width=50, font=('Helvetica', 12))
    energy_opt.pack()
    
def hamstring_images(b1):
    print(b1)  # selected option
    my_image.config(image=yoga_dict1[b1])
    
def backposes_images(b2):
    print(b2)  # selected option
    backposesimg.config(image=yoga_dict2[b2])

def energyposes_images(b3):
    print(b3)  # selected option
    energyposesimg.config(image=yoga_dict3[b3])

yoga_dict1 = {}
for yoga_name1 in yogaposes.hamstringposes:
    yoga_dict1[yoga_name1] = ImageTk.PhotoImage(importyogaImageWithResize("./yoga_Images/{}.png".format(yoga_name1)))

yoga_dict2 = {}
for yoga_name2 in yogaposes.backposeslist:
    yoga_dict2[yoga_name2] = ImageTk.PhotoImage(importyogaImageWithResize("./yoga_Images/{}.png".format(yoga_name2)))
    
yoga_dict3 = {}
for yoga_name3 in yogaposes.Energyposes:
    yoga_dict3[yoga_name3] = ImageTk.PhotoImage(importyogaImageWithResize("./yoga_Images/{}.png".format(yoga_name3)))

variable1 = tk.StringVar(tab4)
variable1.set(yogaposes.hamstringposes[0])

variable2 = tk.StringVar(tab4)
variable2.set(yogaposes.backposeslist[0])

variable3 = tk.StringVar(tab4)
variable3.set(yogaposes.Energyposes[0])

o = tk.OptionMenu(frame1, variable1, *yogaposes.hamstringposes, command=hamstring_images)
b = tk.OptionMenu(frame2, variable2, *yogaposes.backposeslist, command=backposes_images)
e = tk.OptionMenu(frame4, variable3, *yogaposes.Energyposes, command=energyposes_images)

my_image = tk.Label(frame1)
my_image.pack(side = 'bottom', pady=padylength)
backposesimg = tk.Label(frame2)
backposesimg.pack(side = 'bottom', pady=padylength)
energyposesimg = tk.Label(frame4)
energyposesimg.pack(side = 'bottom', pady=padylength)

def refreshhamstring():
    frame1.pack_forget() if frame1.winfo_manager() else frame1.pack(anchor='center')

def refreshbackposes():
    frame2.pack_forget() if frame2.winfo_manager() else frame2.pack(anchor='center')

def refreshenergyposes():
    frame4.pack_forget() if frame4.winfo_manager() else frame4.pack(anchor='center')
    
hamstring_k = tk.Button(frame3, text="Hamstring", width = artbtn_width, height = btnsize_height, command=lambda:[hamstringdrops(), refreshhamstring()])
hamstring_k.pack(side = 'left', padx=padxwidth, pady=padylength)

backposes_k = tk.Button(frame3, text="Back and Hips", width = artbtn_width, height = btnsize_height, command=lambda:[backdrops(), refreshbackposes()])
backposes_k.pack(side = 'left', padx=padxwidth, pady=padylength)

energyposes_k = tk.Button(frame3, text="Energy", width = artbtn_width, height = btnsize_height, command=lambda:[energydrops(), refreshenergyposes()])
energyposes_k.pack(side = 'left', padx=padxwidth, pady=padylength)

yogatab_k = tk.Button(tab4, text="Ambience", width = btnsize_width, height = btnsize_height,  command=ambience_knowledge)
yogatab_k.pack(side = 'bottom', padx=padxwidth, pady=padylength)

# yoga quotes
frame_4 = tk.Frame(tab4)
frame_4.place(relx = 0.5, rely = 0.8, anchor = "center")
label_4 = tk.Label(frame_4,font="helvetica 14", wraplength=quoteswidth, justify="center")
label_4.pack()
def yogaafter():
    label_4.config(text=random.choice(yogaposes.Yogaquotes))
    root.after(7000, yogaafter)
yogaafter()

#--------------------------------------------Vision TAB5---------------------------------------------
tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text="Vision board")
tabControl.pack(expand=5, fill='both')

vpics = glob.glob("./Visionboard/*.png")
vphotos = [tk.PhotoImage(file=x) for x in vpics]
random.shuffle(vphotos)
visionlabel = tk.Label(tab5)
visionlabel.vphotos = vphotos
visionlabel.counter = 0
def visionimages():
	visionlabel['image'] = visionlabel.vphotos[visionlabel.counter%len(visionlabel.vphotos)]
	visionlabel.after(5000, visionimages)
	visionlabel.counter += 1
visionlabel.pack(padx=padxwidth, pady=padylength)
visionimages()

# affirmation quotes   
frame_f = tk.Frame(tab5)
frame_f.place(relx = 0.5, rely = 0.7, anchor = "center")
label_f = tk.Label(frame_f,font="helvetica 14", wraplength=quoteswidth, justify="center")
label_f.pack()
def aftermoti():
    label_f.config(text=random.choice(general_motivation.motivation))
    root.after(7000, aftermoti)
aftermoti()

#---------------------------------------------MUSIC TAB6---------------------------------------------
tab6 = ttk.Frame(tabControl)
tabControl.add(tab6, text="Music")
tabControl.pack(expand=5, fill='both')

# Option menu variable
optionVar = tk.StringVar()
optionVar.set("Piano")

# Create a option menu
option = tk.OptionMenu(tab6, optionVar, "Piano", "Guitar", "Music theory", "Production", "filmmusic", "Tutorials")
option.config(width=20, font=('Helvetica', 12))
option.pack(padx=20)

# dropdown
pianoframe = tk.Frame(tab6)
guitarframe = tk.Frame(tab6)
musictheoryframe = tk.Frame(tab6)
productionframe = tk.Frame(tab6)
filmmusicframe = tk.Frame(tab6)
tutorialsframe = tk.Frame(tab6)
sightreadingframe = tk.Frame(tab6)
mnmframe = tk.Frame(tab6)

# Create button with command
def show():
    print("Selected value :", optionVar.get())
    if optionVar.get() != "Piano": 
        pianodrops()
    else:
        refreshpiano()
    if optionVar.get() != "Guitar": 
        guitardrops()
    else:
        refreshguitar()
    if optionVar.get() != "Music theory": 
        musictheorydrops()
    else:
        refreshmusictheory()
    if optionVar.get() != "Production": 
        productiondrops()
    else:
        refreshproduction()
    if optionVar.get() != "Film music": 
        filmmusicdrops()
    else:
        refreshfilmmusic()
    if optionVar.get() != "Tutorials": 
        tutorialsdrops()
    else:
        refreshtutorials()
btnShow = tk.Button(tab6, text="Show", width = artbtn_width, height = btnsize_height, command=show)
btnShow.pack(padx=20)


def pianodrops():
    piano_opt = pianoo
    piano_opt.config(width=50, font=('Helvetica', 12))
    piano_opt.pack()
def pianoposes_images(piano3):
    print(piano3)  # selected option
    pianoposesimg.config(image=piano_dict3[piano3])
piano_dict3 = {}
for piano_name3 in yogaposes.Energyposes:
    piano_dict3[piano_name3] = ImageTk.PhotoImage(importImageWithResize("./yoga_Images/{}.png".format(piano_name3)))
pianovariable = tk.StringVar(tab6)
pianovariable.set(yogaposes.Energyposes[0])
pianoo = tk.OptionMenu(pianoframe, pianovariable, *yogaposes.Energyposes, command=pianoposes_images)
pianoposesimg = tk.Label(pianoframe)
pianoposesimg.pack(side = 'bottom', pady=padylength)
def refreshpiano():
    pianoframe.pack_forget() if pianoframe.winfo_manager() else pianoframe.pack(anchor='center')

def guitardrops():
    guitar_opt = guitarr
    guitar_opt.config(width=50, font=('Helvetica', 12))
    guitar_opt.pack()
def guitar_images(piano3):
    print(piano3)  # selected option
    guitarimg.config(image=guitar_dict3[piano3])
guitar_dict3 = {}
for guitar_name3 in yogaposes.Energyposes:
    guitar_dict3[guitar_name3] = ImageTk.PhotoImage(importImageWithResize("./yoga_Images/{}.png".format(guitar_name3)))
guitarvariable = tk.StringVar(tab6)
guitarvariable.set(yogaposes.Energyposes[0])
guitarr = tk.OptionMenu(guitarframe, pianovariable, *yogaposes.Energyposes, command=guitar_images)
guitarimg = tk.Label(guitarframe)
guitarimg.pack(side = 'bottom', pady=padylength)
def refreshguitar():
    guitarframe.pack_forget() if guitarframe.winfo_manager() else guitarframe.pack(anchor='center')
    
def musictheorydrops():
    musictheory_opt = musictheoryy
    musictheory_opt.config(width=50, font=('Helvetica', 12))
    musictheory_opt.pack()   
def musictheory_images(musictheory1):
    print(musictheory1)  # selected option
    musictheory_label.config(image=musictheory_dict[musictheory1])
musictheory_label = tk.Label(musictheoryframe)
musictheory_label.pack(side = 'bottom', pady=padylength)
musictheory_dict = {}
for musictheory_name in musiclists.musictheoryimglist:
    musictheory_dict[musictheory_name] = ImageTk.PhotoImage(importImageWithResize("./Music_images/Music_theory/{}.png".format(musictheory_name)))
musictheoryvariable = tk.StringVar(tab6)
musictheoryvariable.set(musiclists.musictheoryimglist[0])
musictheoryy = tk.OptionMenu(musictheoryframe, musictheoryvariable, *musiclists.musictheoryimglist, command=musictheory_images)
def refreshmusictheory():
    musictheoryframe.pack_forget() if musictheoryframe.winfo_manager() else musictheoryframe.pack(anchor='center')

def productiondrops():
    production_opt = productionn
    production_opt.config(width=50, font=('Helvetica', 12))
    production_opt.pack()   
def production_images(production1):
    print(production1)  # selected option
    production_label.config(image=production_dict[production1])
production_label = tk.Label(productionframe)
production_label.pack(side = 'bottom', pady=padylength)
production_dict = {}
for production_name in tradinglists.allwavesimages:
    production_dict[production_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Stocks/waves/{}.png".format(production_name)))
productionvariable = tk.StringVar(tab6)
productionvariable.set(tradinglists.allwavesimages[0])
productionn = tk.OptionMenu(productionframe, productionvariable, *tradinglists.allwavesimages, command=production_images)
def refreshproduction():
    productionframe.pack_forget() if productionframe.winfo_manager() else productionframe.pack(anchor='center')

def filmmusicdrops():
    filmmusic_opt = filmmusicc
    filmmusic_opt.config(width=50, font=('Helvetica', 12))
    filmmusic_opt.pack()   
def filmmusic_images(filmmusic1):
    print(filmmusic1)  # selected option
    filmmusic_label.config(image=filmmusic_dict[filmmusic1])
filmmusic_label = tk.Label(filmmusicframe)
filmmusic_label.pack(side = 'bottom', pady=padylength)
filmmusic_dict = {}
for filmmusic_name in tradinglists.allwavesimages:
    filmmusic_dict[filmmusic_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Stocks/waves/{}.png".format(filmmusic_name)))
filmmusicvariable = tk.StringVar(tab6)
filmmusicvariable.set(tradinglists.allwavesimages[0])
filmmusicc = tk.OptionMenu(filmmusicframe, filmmusicvariable, *tradinglists.allwavesimages, command=filmmusic_images)
def refreshfilmmusic():
    filmmusicframe.pack_forget() if filmmusicframe.winfo_manager() else filmmusicframe.pack(anchor='center')
    
def tutorialsdrops():
    tutorials_opt = tutorialss
    tutorials_opt.config(width=50, font=('Helvetica', 12))
    tutorials_opt.pack()   
def tutorials_images(tutorials1):
    print(tutorials1)  # selected option
    tutorials_label.config(image=tutorials_dict[tutorials1])
tutorials_label = tk.Label(tutorialsframe)
tutorials_label.pack(side = 'bottom', pady=padylength)
tutorials_dict = {}
for tutorials_name in tradinglists.allwavesimages:
    tutorials_dict[tutorials_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Stocks/waves/{}.png".format(tutorials_name)))
tutorialsvariable = tk.StringVar(tab6)
tutorialsvariable.set(tradinglists.allwavesimages[0])
tutorialss = tk.OptionMenu(tutorialsframe, tutorialsvariable, *tradinglists.allwavesimages, command=tutorials_images)
def refreshtutorials():
    tutorialsframe.pack_forget() if tutorialsframe.winfo_manager() else tutorialsframe.pack(anchor='center')

def sightreadingdrops():
    sightreading_opt = sightreadings
    sightreading_opt.config(width=50, font=('Helvetica', 12))
    sightreading_opt.pack()   
def sightreading_images(sightreading1):
    print(sightreading1)  # selected option
    sightreading_label.config(image=sightreading_dict[sightreading1])
sightreading_label = tk.Label(sightreadingframe)
sightreading_label.pack(side = 'bottom', pady=padylength)
sightreading_dict = {}
for sightreading_name in musiclists.Sightreadingimglist:
    sightreading_dict[sightreading_name] = ImageTk.PhotoImage(importImageWithResize("./Music_images/sight_reading/{}.png".format(sightreading_name)))
sightreadingvariable = tk.StringVar(tab6)
sightreadingvariable.set(musiclists.Sightreadingimglist[0])
sightreadings = tk.OptionMenu(sightreadingframe, sightreadingvariable, *musiclists.Sightreadingimglist, command=sightreading_images)
def refreshsightreading():
    sightreadingframe.pack_forget() if sightreadingframe.winfo_manager() else sightreadingframe.pack(anchor='center')

def mnmdrops():
    mnm_opt = mnms
    mnm_opt.config(width=50, font=('Helvetica', 12))
    mnm_opt.pack()   
def mnm_images(mnm1):
    print(mnm1)  # selected option
    mnm_label.config(image=mnm_dict[mnm1])
mnm_label = tk.Label(mnmframe)
mnm_label.pack(side = 'bottom', pady=padylength)
mnm_dict = {}
for mnm_name in musiclists.mnmimglist:
    mnm_dict[mnm_name] = ImageTk.PhotoImage(importImageWithResize("/Users/loh/Documents/Python/Project_tkinter/Music_images/mix_n_master/{}.png".format(mnm_name)))
mnmvariable = tk.StringVar(tab6)
mnmvariable.set(musiclists.mnmimglist[0])
mnms = tk.OptionMenu(mnmframe, mnmvariable, *musiclists.mnmimglist, command=mnm_images)
def refreshmnm():
    mnmframe.pack_forget() if mnmframe.winfo_manager() else mnmframe.pack(anchor='center')
    
# music quotes   
frame_musq = tk.Frame(tab6)
frame_musq.place(relx = 0.5, rely = 0.9, anchor = "center")

label_musq = tk.Label(frame_musq,font="helvetica 14", wraplength=quoteswidth, justify="center")
label_musq.pack()
def after():
    label_musq.config(text=random.choice(Spiritualquotes.musicquotes))
    root.after(15000, after)
after()
#---------------------------------------------TAB7---------------------------------------------
tab7 = ttk.Frame(tabControl)
tabControl.add(tab7, text="Art")
tabControl.pack(expand=5, fill='both')

pics = glob.glob("./Art_references/Random/*.png")
photosresized = []
for i in pics:
    baseheight= 550
    single_image = Image.open(i)
    hpercent = (baseheight/float(single_image.size[1]))
    wsize = int((float(single_image.size[0])*float(hpercent)))
    changed_size = single_image.resize((wsize, baseheight),Image.ANTIALIAS)
    pid = ImageTk.PhotoImage(single_image.resize((wsize, baseheight),Image.ANTIALIAS))
    photosresized.append(pid)
    random.shuffle(photosresized)

mech = glob.glob("./Art_references/Mechanical_references/*.png")
mechphotos = []
for i in mech:
    baseheight= 550
    single_image = Image.open(i)
    hpercent = (baseheight/float(single_image.size[1]))
    wsize = int((float(single_image.size[0])*float(hpercent)))
    changed_size = single_image.resize((wsize, baseheight),Image.ANTIALIAS)
    pid = ImageTk.PhotoImage(single_image.resize((wsize, baseheight),Image.ANTIALIAS))
    mechphotos.append(pid)
    random.shuffle(mechphotos)

anatomy = glob.glob("./Art_references/Anatomy_references/*.png")
anatomyphotos = []
for i in anatomy:
    baseheight= 550
    single_image = Image.open(i)
    hpercent = (baseheight/float(single_image.size[1]))
    wsize = int((float(single_image.size[0])*float(hpercent)))
    changed_size = single_image.resize((wsize, baseheight),Image.ANTIALIAS)
    pid = ImageTk.PhotoImage(single_image.resize((wsize, baseheight),Image.ANTIALIAS))
    anatomyphotos.append(pid)
    random.shuffle(anatomyphotos)
    
ct = glob.glob("./Art_references/Color_n_painting/*.png")
ctphotos = []
for i in ct:
    baseheight= 550
    single_image = Image.open(i)
    hpercent = (baseheight/float(single_image.size[1]))
    wsize = int((float(single_image.size[0])*float(hpercent)))
    changed_size = single_image.resize((wsize, baseheight),Image.ANTIALIAS)
    pid = ImageTk.PhotoImage(single_image.resize((wsize, baseheight),Image.ANTIALIAS))
    ctphotos.append(pid)
    random.shuffle(ctphotos)
    
drawinglessons = glob.glob("./Art_references/Drawing_lessons/*.png")
drawinglessonsphotos = []
for i in drawinglessons:
    baseheight= 550
    single_image = Image.open(i)
    hpercent = (baseheight/float(single_image.size[1]))
    wsize = int((float(single_image.size[0])*float(hpercent)))
    changed_size = single_image.resize((wsize, baseheight),Image.ANTIALIAS)
    pid = ImageTk.PhotoImage(single_image.resize((wsize, baseheight),Image.ANTIALIAS))
    drawinglessonsphotos.append(pid)
    random.shuffle(drawinglessonsphotos)
    
artinspirations = glob.glob("./Art_references/art_Inspirations/*.png")
artinspirationphotos = []
for i in artinspirations:
    baseheight= 550
    single_image = Image.open(i)
    hpercent = (baseheight/float(single_image.size[1]))
    wsize = int((float(single_image.size[0])*float(hpercent)))
    changed_size = single_image.resize((wsize, baseheight),Image.ANTIALIAS)
    pid = ImageTk.PhotoImage(single_image.resize((wsize, baseheight),Image.ANTIALIAS))
    artinspirationphotos.append(pid)
    random.shuffle(artinspirationphotos)
    
label = tk.Label(tab7)

label.photosresized = photosresized
label.mechphotos = mechphotos
label.ctphotos = ctphotos
label.anatomyphotos = anatomyphotos
label.drawinglessonsphotos = drawinglessonsphotos
label.artinspirationphotos = artinspirationphotos

label.counter = 0
def changeimage():
    label['image'] = label.photosresized[label.counter%len(label.photosresized)]
    # label.after(8000, changeimage)
    label.counter += 1

def mechanicalimages():
    label['image'] = label.mechphotos[label.counter%len(label.mechphotos)]
    # label.after(8000, changeimage)
    label.counter += 1

def anatomyimages():
    label['image'] = label.anatomyphotos[label.counter%len(label.anatomyphotos)]
    # label.after(8000, changeimage)
    label.counter += 1

def colortheorynwatercolorimages():
    label['image'] = label.ctphotos[label.counter%len(label.ctphotos)]
    # label.after(8000, changeimage)
    label.counter += 1

def drawinglessonsimages():
    label['image'] = label.drawinglessonsphotos[label.counter%len(label.drawinglessonsphotos)]
    # label.after(8000, changeimage)
    label.counter += 1

def artinspirationimages():
    label['image'] = label.artinspirationphotos[label.counter%len(label.artinspirationphotos)]
    # label.after(8000, changeimage)
    label.counter += 1
    
label.pack(side="top", pady=padylength)
changeimage()
mechanicalimages()
anatomyimages()
colortheorynwatercolorimages()
drawinglessonsimages()
artinspirationimages()

drawrandom_k = tk.Button(tab7, text="Random", width = artbtn_width, height = btnsize_height, command=changeimage)
drawrandom_k.pack(side="left",padx=padxwidth, pady=padylength)

mechanicalart_k = tk.Button(tab7, text="Mechanical", width = artbtn_width, height = btnsize_height, command=mechanicalimages)
mechanicalart_k.pack(side="left", pady=padylength)

anatomy_k = tk.Button(tab7, text="Anatomy", width = artbtn_width, height = btnsize_height, command=anatomyimages)
anatomy_k.pack(side="left", padx=padxwidth, pady=padylength)

colortheory_k = tk.Button(tab7, text="Colors & painting", width = artbtn_width, height = btnsize_height, command=colortheorynwatercolorimages)
colortheory_k.pack(side="left", padx=padxwidth, pady=padylength)

drawinglessons_k = tk.Button(tab7, text="Drawing Lessons", width = artbtn_width, height = btnsize_height, command=drawinglessonsimages)
drawinglessons_k.pack(side="left", padx=padxwidth, pady=padylength)

artinsp_k = tk.Button(tab7, text="Inspirations", width = artbtn_width, height = btnsize_height, command=artinspirationimages)
artinsp_k.pack(side="left", padx=padxwidth, pady=padylength)


#---------------------------------------------TAB8---------------------------------------------
tab7 = ttk.Frame(tabControl)
tabControl.add(tab7, text="Technology")
tabControl.pack(expand=5, fill='both')

def callback(url):
    webbrowser.open_new(url)
    
qtextnlinks = (('apple', 'google.com'), ('orange', 'bing.com'))
for label_text, url in qtextnlinks:
    label_p = tk.Label(tab7, text=label_text, fg="blue", cursor="hand2")
    label_p.pack()
    label_p.bind("<Button-1>", lambda e: callback(url))
    
# programming quotes   
frame_p = tk.Frame(tab7)
frame_p.place(relx = 0.5, rely = 0.9, anchor = "center")

label_p = tk.Label(frame_p,font="helvetica 14", wraplength=quoteswidth, justify="center")
label_p.pack()
def after():
    label_p.config(text=random.choice(qtextnlinks))
    root.after(15000, after)
after()

#---------------------------------------------TAB9---------------------------------------------
tab7 = ttk.Frame(tabControl)
tabControl.add(tab7, text="Writing")
tabControl.pack(expand=5, fill='both')

# writing quotes   
frame_w = tk.Frame(tab7)
frame_w.place(relx = 0.5, rely = 0.9, anchor = "center")

label_w = tk.Label(frame_w,font="helvetica 14", wraplength=quoteswidth, justify="center")
label_w.pack()
def after():
    label_w.config(text=random.choice(tradingquotes.tradingquotes))
    root.after(15000, after)
after()

#---------------------------------------------TAB8---------------------------------------------
tab7 = ttk.Frame(tabControl)
tabControl.add(tab7, text="Other")
tabControl.pack(expand=5, fill='both')

# other quotes   
frame_o = tk.Frame(tab7)
frame_o.place(relx = 0.5, rely = 0.9, anchor = "center")

label_o = tk.Label(frame_o,font="helvetica 14", wraplength=quoteswidth, justify="center")
label_o.pack()
def after():
    label_o.config(text=random.choice(tradingquotes.tradingquotes))
    root.after(15000, after)
after()

root.mainloop()