from tkinter import Tk, Button, Label, StringVar, Entry
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube

root = Tk()
root.title('Youtube video downloader')
root.configure(background='LightYellow')
root.minsize(width=600, height=100)
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

link_lbl = Label(root, text="Enter Link", bg='Purple',font= 'Helvetica 15')
link_lbl.grid(row=1, column=0)

link = StringVar()
link_entry  = Entry(root, textvariable=link, width=50, borderwidth=4)
link_entry.grid(row=1, column=1)

select_dir = Button(root, text="Choose Directory", bg='Green', width=15, command=open_file)
select_dir.grid(row=1, column=2)

download_btn = Button(root, text="Download",bg='Red', width=10, command=download_file)
download_btn.grid(row=2, column=1)

root.mainloop()