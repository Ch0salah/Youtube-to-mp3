import os
from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
from matplotlib import image
from moviepy import *
from moviepy.editor import VideoFileClip
from moviepy.editor import *


from pytube import YouTube
import shutil

from matplotlib.pyplot import title
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    if path == '':
        path_label.config(text='slect path for download')
    else:
        path_label.config(text=path)


#download function
def download_file():
    #get selected path
    user_path = path_label.cget("text")

    if user_path == 'slect path for download':
        messagebox.showinfo('path not detected', 'select path first !!')
    else:
        #get user path
        get_link = link_field.get()
        screen.title('Downloading...')
        #Download Video
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
        mp3_clip = mp4_video + '.mp3'
        vid_clip = VideoFileClip(mp4_video)
        audioclip = vid_clip.audio
        audioclip.write_audiofile(mp3_clip)
        audioclip.close()
        vid_clip.close()
        #move file to selected directory
        shutil.move(mp3_clip, user_path)
        os.remove(mp4_video)
        screen.title('Download Complete! Download Another File...')





screen = Tk()

screen.resizable(False,False)
screen.geometry("920x670+290+85")
screen.configure(bg="#0f1a2b")


title = screen.title('black hole') 

canvas = Canvas(screen,width=920,height=670)
canvas.configure(bg='#0f1a2b')

canvas.pack()

#top bar
top =PhotoImage(file="top.png")
top1=Label(screen,image=top,bg="#0f1a2b")
#lables
down_but = PhotoImage(file="Downl.png")
select_but = PhotoImage(file="path.png")
link_lable = Label(screen,text= "enter download link:" ,bg="#0f1a2b",fg="#7F00FF",font =('Arial' ,15))
link_field = Entry(screen ,font=("arial",15), width=60)
link_field.pack(ipady=5)
path_label = Label(screen,text= "slect path for download" ,bg="#0f1a2b",fg="#7F00FF",font =('Arial' ,15))
select_btn = Button(screen,image=select_but,bg="#0f1a2b",width=140,height=47,command=select_path)
download_btn = Button(screen,image=down_but, bg="#0f1a2b",width=140,height=47,command=download_file)
watermark = Label(screen,text= "@ch_a.ron_1/Python_X" ,bg="#0f1a2b",fg="#fff",font =('Arial' ,10))


canvas.create_window(450,290,window=link_lable)
canvas.create_window(450,400,window=path_label)
canvas.create_window(450,350,window=link_field)
canvas.create_window(450,470,window=select_btn)
canvas.create_window(450,560,window=download_btn)
canvas.create_window(90,650,window=watermark)
canvas.create_window(456,122.3,window=top1)
#title bar icon
image_icon = PhotoImage(file="download.png")
screen.iconphoto(False,image_icon)

#main logo
logo = PhotoImage(file='download.png')
Label(screen,image=logo, bg="#0f1a2b").place(x=90,y=100)


screen.mainloop()