import tkinter as tk
from tkinter import *
from tkinter import ttk
import pytube
from pytube import YouTube
from tkinter import messagebox,filedialog

def BROWSE():
    download=filedialog.askdirectory(title="Save Video")
    Label(root, text="Video saved here: " + download).pack()

def Download():
    messagebox.showerror("Message", "Your file download has started!")
    choice = ytQuality.get()
    url = ytLink.get()
    yt = YouTube(url)
    print(len(yt))
    if (len(url) > 1):
        ytError.config(text="")
        yt = YouTube(url)
        if (choice == options[0]):
            select = yt.streams.filter(progressive=True).first()
        elif (choice == options[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()
        elif (choice == options[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytError.config(text="Paste Link again!!", fg="red")
    developerlabel = Label(root, text="Your file is downloaded!!", font=("jost", 15))
    developerlabel.grid()
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")
    #Message that the video downloaded with a smooth message with LOCATION
    messagebox.showinfo("Video Downloaded and Saved in\n"+downloadFolder)

# Main window
root=tk.Tk()
root.geometry("600x600")
root.resizable(0,0)
root.title("Youtube Video Downloader")
# root.config(background="Yellow")

#head
Label(root,text="YouTube Video Downloader",font="Ariel 20 bold",fg='Blue').pack()

#CopyLink
Label(root,text="Paste the link here",font="Ariel 15 bold",fg='Black').pack(padx=0,pady=20)
link=StringVar()
ytLink=Entry(root,textvariable=link,font="Ariel 15 bold",fg='Black',width=40)
ytLink.pack()

#Destination where the video is to be saved
Label(root,text="Destination Folder",font="Ariel 20 bold",fg='Black').pack(padx=0,pady=5)
buttons=Button(root,text='Browse',command=BROWSE,relief=GROOVE).pack()

#Yt error
ytError = Label(root,text="Enter the correct URL to your video",fg="black",font=("jost",10)).pack()

#Quality of the Video
Label(root,text="Select the quality of the video",font="Ariel 20 bold",fg='Black').pack(padx=0,pady=15)
options=['480','720','1080']
ytQuality=ttk.Combobox(root,values=options)
ytQuality.pack()

#Progress bar to see video is downloading
bar=ttk.Progressbar(root,length=400).pack(pady=10)

# Download Button
Button(root, text="DOWNLOAD", command=Download, width=15, relief=GROOVE, font="Ariel 20 bold", fg='Black').pack(pady=15)
#Creating tkinter variable
# videoLink=StringVar()
# downloadPath=StringVar()



root.mainloop()