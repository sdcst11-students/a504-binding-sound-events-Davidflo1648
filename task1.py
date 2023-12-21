from tkinter import *
import playsound as ps

win = Tk()
win.title('Sound Board')

def play_cosound():
    ps.playsound('mooing-cow.mp3')
def play_dusound():
    ps.playsound('quacking-duck.mp3')
def play_shsound():
    ps.playsound('sound-sheep.mp3')
def play_dosound():
    ps.playsound('bray-donkey.mp3')
def play_husound():
    ps.playsound('screaming-huggus.mp3')

cow_img = PhotoImage(file='cow300.png')
b_cow = Button(win,image=cow_img, command=play_cosound)
duck_img = PhotoImage(file='duck300.png')
b_duck = Button(win,image=duck_img, command=play_dusound)
sheep_img = PhotoImage(file='sheep300.png')
b_sheep = Button(win,image=sheep_img, command=play_shsound)
donkey_img = PhotoImage(file='donkey300.png')
b_donkey = Button(win,image=donkey_img, command=play_dosound)
huggus_img = PhotoImage(win,file='huggus300.png')
b_huggus = Button(win,image=huggus_img, command=play_husound)

b_cow.grid(row=1,column=1)
b_duck.grid(row=2,column=1)
b_sheep.grid(row=3,column=1)
b_donkey.grid(row=1,column=2)

b_huggus.grid(row=3,column=2)

win.mainloop()