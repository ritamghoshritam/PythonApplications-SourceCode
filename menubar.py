from tkinter import *


def doNothing():
    print("Ok Ok Ok I won't !!!")
    
root = Tk()
menu = Menu(root)

root.config(menu = menu)

subMenu = Menu(menu)

menu.add_cascade(label = "File", menu = subMenu)

subMenu.add_command(label = "New Project...", command = doNothing)

subMenu.add_separator()

subMenu.add_command(label = "Exit", command = doNothing)

editMenu = Menu(menu)

menu.add_cascade(label = "Redo", command = doNothing)



toolbar = Frame(root, bg = "blue")

insertButt = Button(toolbar, text = "Insert Mapping", command = doNothing)

insertButt.pack(side = LEFT, padx = 2, pady = 2)

printButt = Button(toolbar, text = "Print", command = doNothing)

printButt.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)



status = Label(root, text = "Preparing for GATE", bd = 1, relief = SUNKEN, anchor = W)

status.pack(side = BOTTOM, fill = X)

root.mainloop()

                    
