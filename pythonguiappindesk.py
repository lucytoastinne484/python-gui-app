from tkinter import *
from pytube import *


#win_gui stands from graphic user interface window#

win_gui = Tk()

#Window setup

win_gui.geometry("925x463")

gui_title1 = win_gui.title("pytube")

#window style set up#
win_gui.config(background="#FF00FF")

#window button
gui_btn = Button(win_gui,text='Download here',command=win_gui.destroy)

gui_btn.pack(side=RIGHT, padx=15, pady=30)

#window text#


txt = Canvas(win_gui,height=30,width=60)
txt.create_text(100,100,text="Welcome to Pytube Downloader",font='Helvetica 15 bold')
txt.pack()

#with this piece i create the widgets#

class Widgets(root):
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome to pytube")
        
        Main_Frame = Frame(self.root,bd=5,relief=RIDGE)
        Main_Frame.pack()
        Main_Frame.grid(row=10,pady=20,padx=50)
        
        lblTitle = Label(Main_Frame,font=('arial',30,'bold','underline'))
        
        
        
    

#this piece here makes our code run

win_gui.mainloop()



