from tkinter import *
from openAPI import *
from nearBusstop import *

class searchBus:
    def __init__(self,  busNM='None'):
        window = Tk()
        window.geometry("+610+300")

        self.busnum = busNM
        self.frame1 = Frame(window)
        self.frame1.pack()

        self.busNumlabel = Label(self.frame1, text=self.busnum + " 정보", width=len(self.busnum) + 5)
        self.busNumlabel.pack(side=LEFT)

        self.frame2 = Frame(window)
        self.frame2.pack()

        self.canvas = Canvas(self.frame2, width=150, height=150, bg='white')
        self.canvas.pack()

        self.frame3 = Frame(window)
        self.frame3.pack()

        self.mailbutton = Button(self.frame3, text="도착5분전 메일알림요청")
        self.mailbutton.pack()

        window.mainloop()

if __name__ == "__main__":
    searchBus()