# backup file

from classes import *
from tkinter import *
from tkinter.filedialog import *

def askPathMc():
    filepath = askdirectory(title = "Select the minecraft folder")

def askPathBc():
    filepath = askdirectory(title = "Select the backup folder")

def makeBackup():
    pass

def main():

    window = Tk()
    window.geometry('330x100')
    window.resizable(0, 0)

    label = Label(window, text="Minecraft folder").place(x=0, y=0)
    labe2 = Label(window, text="Backup Folder").place(x=0, y=30)
    e1 = Entry(window, width = 30).place(x=100, y=0)
    e2 = Entry(window, width = 30).place(x=100, y=30)
    bP1 = Button(window, text = "...", command = askPathMc).place(x=300, y=0)
    bP2 = Button(window, text = "...", command = askPathBc).place(x=300, y=30)
    bB = Button(window, text = "Backup", command = makeBackup).pack(side = BOTTOM, pady = 10)
    window.mainloop()

if __name__ == "__main__":
    main()