from tkinter import Tk, Button, Label, StringVar, Entry
import moviepy.editor as mp
import os
import re
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube

root = Tk()
root.title('Youtube video downloader or MP4 to MP3 Converter')
root.configure(background='LightYellow')
root.minsize(width=800, height=200)
root.resizable(width=False, height=False)

def open_file():
    global directory
    directory = askdirectory()
    print(directory)

def download_file():
    if len(link.get()) == 0:
        messagebox.showerror("Link is empty","Link cannot be found")
    else:
        YouTube(link.get()).streams.get_highest_resolution().download(directory)
        messagebox.showinfo("Complete","Video Downloaded Successfully")
        link_entry.delete(0)
        
def open_mp4_folder():
    global mp4_directory
    mp4_directory=askdirectory()
    print(mp4_directory)

def open_mp3_folder():
    global mp3_directory
    mp3_directory=askdirectory()
    print(mp3_directory)
    
def convert():
    for file in [n for n in os.listdir(mp4_directory) if re.search('.mp4',n)]:
        full_path = os.path.join(mp4_directory,file)
        output_path = os.path.join(mp3_directory, os.path.splitext(file)[0]+ '.mp3' )
        audioclip = mp.AudioFileClip(full_path)
        audioclip.write_audiofile(output_path)
        messagebox.showinfo("Complete", "Mp4 file converted to Mp3 Successfully")


link_lbl = Label(root, text="Enter Link", bg='Purple',fg="White",font= 'Helvetica 15')
link_lbl.grid(row=2, column=0)

link = StringVar()
link_entry  = Entry(root, textvariable=link, width=50, borderwidth=4)
link_entry.grid(row=2, column=1)

select_dir = Button(root, text="Choose Directory", bg='Green',fg="White", width=15, command=open_file)
select_dir.grid(row=2, column=2)

download_btn = Button(root, text="Download",bg='Red',fg="White", width=15, command=download_file)
download_btn.grid(row=3, column=1)

or_lbl = Label(root, text="OR", bg='Orange', width=15)
or_lbl.grid(row=5, column=1)

mp4_btn = Button(root,text="Choose Mp4 Folder",width=25, command=open_mp4_folder,bg="blue",fg="White")
mp4_btn.grid(row=6,column=0,padx = 15, pady =15)

mp3_btn = Button(root,text="Choose Mp3 Folder",width=25, command=open_mp3_folder,bg="brown",fg="White")
mp3_btn.grid(row=6,column=2)

convert_btn = Button(root,text="Convert Mp4 to Mp3",width=25, command=convert,bg="black",fg="White")
convert_btn.grid(row=7,column=1)

exit_btn = Button(root,text="Exit Application",width=25, command=root.destroy,bg="purple",fg="White")
exit_btn.grid(row=8,column=1)

root.mainloop()