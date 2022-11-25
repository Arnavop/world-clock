from datetime import datetime, time
import pytz
from tkinter import * 
import time

root = Tk()
root.title("World clock") #rename window
root.geometry("400x250") #window size

def world_time():
    country = pytz.timezone("Asia/Kolkata")
    country_time = datetime.now(country)
    current = country_time.strftime("%H:%M:%S")
    clock.config(text=current)
    name.config(text="India")
    

    country = pytz.timezone("Greenwich")
    country_time = datetime.now(country)
    current = country_time.strftime("%H:%M:%S")
    clock1.config(text=current)
    name1.config(text="UTC")

    country = pytz.timezone("US/Arizona")
    country_time = datetime.now(country)
    current = country_time.strftime("%H:%M:%S")
    clock2.config(text=current)
    name2.config(text="USA")

    country = pytz.timezone("Asia/Dubai")
    country_time = datetime.now(country)
    current = country_time.strftime("%H:%M:%S")
    clock3.config(text=current)
    name3.config(text="Dubai")

    clock.after(200,world_time) #to make clock run

#Structure of world clock (font,text,position)
#Made by Arnav Kamra
name = Label(root,font=("times",20,"bold"))
name.place(x=30,y=5)
clock = Label(root,font=("times",25,"bold"))
clock.place(x=10,y=40)
samp = Label(root,text="Hours minutes seconds",font="times 10 bold")
samp.place(x=10,y=80)

name1 = Label(root,font=("times",20,"bold"))
name1.place(x=290,y=5)
clock1 = Label(root,font=("times",25,"bold"))
clock1.place(x=260,y=40)
samp = Label(root,text="Hours minutes seconds",font="times 10 bold")
samp.place(x=260,y=80)


name2 = Label(root,font=("times",20,"bold"))
name2.place(x=30,y=140)
clock2 = Label(root,font=("times",25,"bold"))
clock2.place(x=10,y=180)
samp = Label(root,text="Hours minutes seconds",font="times 10 bold")
samp.place(x=10,y=220)


name3 = Label(root,font=("times",20,"bold"))
name3.place(x=290,y=140)
clock3 = Label(root,font=("times",25,"bold"))
clock3.place(x=260,y=180)
samp = Label(root,text="Hours minutes seconds",font="times 10 bold")
samp.place(x=260,y=220)
world_time()
clock.after(200,world_time)
root.mainloop()



'''for names in pytz.all_timezones: #use for knowing all timezone names
    print(names)'''

#you can even make it 12 hour clock by modifying with suitable code 
