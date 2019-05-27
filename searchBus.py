from tkinter import *
from openAPI import *
from nearBusstop import *

class searchBus:
    def __init__(self, stid='23139', bsid='100100020', busNM='141', sk='s'):
        window = Tk()
        window.geometry("+610+300")

        self.stid = stid
        self.bsid = bsid
        self.busnum = busNM
        self.frame1 = Frame(window)
        self.frame1.pack()

        self.busNumlabel = Label(self.frame1, text=self.busnum + " 정보", width=len(self.busnum) + 5)
        self.busNumlabel.pack(side=LEFT)

        self.frame2 = Frame(window)
        self.frame2.pack()

        if sk == 's':
            self.Infolist = SgetbusInfo(self.stid, self.bsid, self.busnum)
        elif sk == 'k':
            self.Infolist = KgetbusInfo(self.stid, self.bsid, self.busnum)
        print(self.Infolist)

        Label(self.frame2, text="남은시간 = " + self.Infolist[1]).pack()
        Label(self.frame2, text="첫차/막차 시간 = " + self.Infolist[3] + "/" + self.Infolist[4]).pack()
        Label(self.frame2, text="배차간격 = " + self.Infolist[0] + "분").pack()
        Label(self.frame2, text="다음정류장 = " + self.Infolist[2]).pack()


        self.frame3 = Frame(window)
        self.frame3.pack()

        self.mailbutton = Button(self.frame3, text="도착5분전 메일알림요청")
        self.mailbutton.pack()

        window.mainloop()

if __name__ == "__main__":
    searchBus()