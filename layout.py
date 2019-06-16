
from tkinter import *

root = Tk()

"""topFrame = Frame(root)

topFrame.pack()

bottomFrame = Frame (root)

bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Button 1", fg = "red")
button2 = Button(topFrame, text = "Button 2", fg = "blue")
button3 = Button(topFrame, text = "Button 3", fg = "yellow")
button4 = Button(topFrame, text = "Button 4", fg = "green")

button1.pack()
button2.pack()
button3.pack()
button4.pack()

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)"""

one = Label(root, text = "one", bg = "red", fg = "white")
one.pack()

two = Label(root, text = "two", bg = "green", fg = "black")
two.pack(fill = X)

three = Label(root, text = "three", bg = "blue", fg = "white")
three.pack(side = LEFT, fill = Y)


root.mainloop()
