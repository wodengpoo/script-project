from tkinter import *
from openAPI import *

class searchBus:
    def __init__(self):
        window = Tk()

        self.frame1 = Frame(window)
        self.frame1.pack()

        self.busNumlabel = Label(self.frame1, text="버스 번호", width=10)
        self.busNumlabel.pack(side=LEFT)
        self.busNumentry = Entry(self.frame1, text="", width=5)
        self.busNumentry.pack(side=LEFT)

        self.frame2 = Frame(window)
        self.frame2.pack()

        self.destlabel = Label(self.frame2, text="목적지", width=10)
        self.destlabel.pack(side=LEFT)
        self.destentry = Entry(self.frame2, text="", width=5)
        self.destentry.pack()

        self.frame3 = Frame(window)
        self.frame3.pack()

        self.searchbutton = Button(self.frame3, text="정보 검색")
        self.searchbutton.pack()
        self.Infolabel= Label(self.frame3, text="버스 정보", width=10)
        self.Infolabel.pack()

        self.canvas = Canvas(self.frame3, width=150, height=150, bg='white')
        self.canvas.pack()

        self.frame4 = Frame(window)
        self.frame4.pack()

        self.mailbutton = Button(self.frame4, text="도착5분전 메일알림요청")
        self.mailbutton.pack()

        window.mainloop()

if __name__ == "__main__":
    searchBus()