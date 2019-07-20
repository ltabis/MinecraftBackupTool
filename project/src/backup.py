# backup file

from os import *
from functools import partial
from tkinter.filedialog import *
from sys import version_info
from shutil import *
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

def saveWorld(input, e1, e2, w):

    try:
        if e2.get() == "":
            copytree(e1.get() + "/saves/" + input.get(input.curselection()), "./" + input.get(input.curselection()))
        else:
            copytree(e1.get() + "/saves/" + input.get(input.curselection()), e2.get() + "/" + input.get(input.curselection()))
    except Error as e:
        showerror("Error", 'Directory not copied. Error: %s' % e)
    except OSError as e:
        showerror("Error", 'Directory not copied. Error: %s' % e)
    w.destroy()
    showinfo("Success", "Backup done.")


def checkFolder(e1):

    filenames = listdir(e1.get())

    for i in filenames:
        if i == "saves":
            return True
    return False

def makeBackup(e1, e2):

    if checkFolder(e1) == False:
        showerror("Error", "Minecraft folder isn't right.")
        return

    w = Tk()
    w.geometry('330x90')
    w.resizable(0, 0)

    filenames = listdir(e1.get() + "/saves")
    liste = Listbox(w, width = 50, height = 3)
    nb = 0
    for i in filenames:
        liste.insert(nb, i)
        nb += 1
    liste.pack()
    Button(w, text = "Select", command = partial(saveWorld, liste, e1, e2, w)).pack(side = BOTTOM, pady = 10)
    w.mainloop()

def main():

    window = Tk()
    window.geometry('330x120')
    window.resizable(0, 0)

    Label(window, text="Minecraft folder").place(x=0, y=0)
    Label(window, text="Backup Folder").place(x=0, y=30)
    e1 = Entry(window, width = 30)
    e2 = Entry(window, width = 30)
    e1.place(x=100, y=0)
    e2.place(x=100, y=30)
    Button(window, text = "...", command = partial(askPathMc, e1)).place(x=300, y=0)
    Button(window, text = "...", command = partial(askPathBc, e2)).place(x=300, y=30)
    Button(window, text = "Backup", command = partial(makeBackup, e1, e2)).pack(side = BOTTOM, pady = 10)
    window.mainloop()

if __name__ == "__main__":
    main()