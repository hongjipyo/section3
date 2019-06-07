from tkinter import*
import json

def printHello() :
    print('Hi')

root = Tk()

w = Label(root, text="Python test")
b = Button(root, text="hello python", command = printHello)
c = Button(root, text="Quit", command= root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()


#기초 Gui 설정
