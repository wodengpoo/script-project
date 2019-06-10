from tkinter import *
from openAPI import *
from nearBusstop import *
from PIL import ImageTk, Image
from navermail import *

class searchBus:
    def sendEmail(self):
        sendMessage(self.mailentry.get(),
                    "남은시간 = " + self.info[1] + "\n" +
                    "첫차/막차 시간 = " + self.info[3] + "/" + self.info[4] + "\n" +
                    "배차간격 = " + self.info[0] + "분" + "\n" +
                    "다음정류장 = " + self.info[2])
    def __init__(self, Info=(('0', '0', '0', '0' '0', '1')), busnm='0', region='0'):
        window = Toplevel()
        window.geometry("+610+300")

        self.info = Info
        self.frame1 = Frame(window)
        self.frame1.pack()

        self.busNumlabel = Label(self.frame1, text=busnm + " 정보", width=len(busnm) + 5)
        self.busNumlabel.pack(side=LEFT)

        self.frame2 = Frame(window)
        self.frame2.pack()

        Label(self.frame2, text="남은시간 = " + Info[1]).pack()
        Label(self.frame2, text="첫차/막차 시간 = " + Info[3] + "/" + Info[4]).pack()
        Label(self.frame2, text="배차간격 = " + Info[0] + "분").pack()
        Label(self.frame2, text="다음정류장 = " + Info[2]).pack()


        self.frame3 = Frame(window)
        self.frame3.pack()

        Label(self.frame3, text='버스 유형').pack()

        imgsrc = PhotoImage(file="image/" + str(Info[-1]) + ".gif")
        Label(self.frame3, image=imgsrc).pack()

        Label(self.frame3, text="받을 메일 : ").pack(side=LEFT)
        self.mailentry = Entry(self.frame3, width=8)
        self.mailentry.pack(side=LEFT)
        self.mailbutton = Button(self.frame3, text="정보 메일로 전송", command=self.sendEmail)
        self.mailbutton.pack()

        window.mainloop()

if __name__ == "__main__":
    searchBus()