from tkinter import *
import tkinter as tk
from pytube import *
from tkinter.ttk import *
from pytube import YouTube
import pytube
import os
import pathlib
import pathspec
import datetime
import dateutil
import sys
import sysconfig

#----------------#
#download setup#


def DownloadCommand360p():
    
    download_link = YouTube(str(link.get()))
    
    download_link.streams.filter(res="360p").first().download(r"C:\YTDownloads")

    msg = Text(win_gui,height=8,width=8)
    
    msg.pack()
    
    msg.insert('1.0', 'a done ')
    
    msg.get('1.0','end')
    

def DownloadCommand720p():
    
    download_link = YouTube(str(link.get()))
    
    download_link.streams.filter(res="720p").first().download(r"C:\YTDownloads")

    msg = Text(win_gui,height=8,width=8)
    
    msg.pack()
    
    msg.insert('1.0', 'a done ')
    
    msg.get('1.0','end')
    

def DownloadCommand1080p():
    
    download_link = YouTube(str(link.get()))
    
    download_link.streams.filter(res="1080p").first().download(r"C:\YTDownloads")

    msg = Text(win_gui,height=8,width=8)
    
    msg.pack()
    
    msg.insert('1.0', 'a done ')
    
    msg.get('1.0','end')


#----------------#
#win_gui stands from graphic user interface window#

win_gui = Tk()



#----------------#
#Window setup
win_gui.geometry("925x463")
gui_title1 = win_gui.title("pytube")
#----------------#


#----------------#
#window style set up#
win_gui.config(background="#FF00FF")
#----------------#



#----------------#
#window button
gui_btn = Button(win_gui,text='Exit from app here',command=win_gui.destroy)

gui_btn.pack(side=RIGHT, padx=15, pady=30)
#----------------#



#----------------#



#----------------#
#Checking some things in this libraries
#checker = print(dir(Tk))#
#checker_3 = print(dir(YouTube))#
#----------------#



#----------------#
#a text space for download the video#
win_gui.resizable(True,True)
win_gui.title("Downloader")
#----------------#

#I will create a widget to process the link i want my program download#

link = tk.StringVar()
tk.Label(win_gui,text="Put the video link:  ").place(x=10,y=10)
input_video = tk.Entry(win_gui,textvariable=link,width=50).place(x=30,y=30)




#----------------#
#lets put a different button from our another test i made#
        

dwd_button = Button(win_gui,text='Download 360p',compound=LEFT,command=DownloadCommand360p)

dwd_button.pack(
    ipadx=12,
    ipady=12)

dwd_button720p = Button(win_gui,text='Download 720p',compound=LEFT,command=DownloadCommand720p)

dwd_button720p.pack(
    ipadx=12,
    ipady=12)

dwd_button1080p = Button(win_gui,text='Download 1080p',compound=LEFT,command=DownloadCommand1080p)

dwd_button1080p.pack(
    ipadx=12,
    ipady=12)

#----------------#






#----------------#

#this piece here makes our code run

win_gui.mainloop()


#----------------#
