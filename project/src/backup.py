# backup file


from os import *
from classes import *
from functools import partial
from tkinter.filedialog import *
from sys import version_info
if version_info.major == 2:
    from Tkinter import *
    from tkMessageBox import *
elif version_info.major == 3:
    from tkinter import *
    from tkinter.messagebox import *

def askPathMc(e1):

    folder = askdirectory(title = "Select the minecraft folder")

    e1.delete(0, END)
    e1.insert(0, folder)

def askPathBc(e2):

    folder = askdirectory(title = "Select the backup folder")

    e2.delete(0, END)
    e2.insert(0, folder)

def saveWorld():
    pass

def makeBackup(e1, e2):

    print(path.dirname(e1.get()))
    if path.basename(e1.get()) != ".minecraft":
        showerror("Error", "Minecraft folder hasn't been found.")
        return

    w = Tk()
    w.geometry('330x90')
    w.resizable(0, 0)

    filenames = listdir(e1.get())
    liste = Listbox(w, width = 50, height = 3)
    for i in filenames:
        liste.insert(i)
    liste.pack()
    bB = Button(w, text = "Select", command = saveWorld).pack(side = BOTTOM, pady = 10)

def main():

    window = Tk()
    window.geometry('330x120')
    window.resizable(0, 0)

    label = Label(window, text="Minecraft folder").place(x=0, y=0)
    labe2 = Label(window, text="Backup Folder").place(x=0, y=30)
    e1 = Entry(window, width = 30)
    e2 = Entry(window, width = 30)
    e1.place(x=100, y=0)
    e2.place(x=100, y=30)
    bP1 = Button(window, text = "...", command = partial(askPathMc, e1)).place(x=300, y=0)
    bP2 = Button(window, text = "...", command = partial(askPathBc, e2)).place(x=300, y=30)
    bB = Button(window, text = "Backup", command = partial(makeBackup, e1, e2)).pack(side = BOTTOM, pady = 10)
    window.mainloop()

if __name__ == "__main__":
    main()