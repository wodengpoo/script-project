from tkinter import *
from searchBus import *
from nearBusstop import *
from teller import *
#무조건 기능 많이 때려넣는게 장땡! 이왕이면 신박한 기술
class selectMenu:
    def exeBusstop(self):
        nearBusstop()
    def exeSearchBus(self):
        searchBus()

    def telegrambot(self):
        handle()

    def __init__(self):
        window = Tk()

        #getData() #도시 코드 정보를 가져옴
        image = PhotoImage(file='image/내버스야어디니.gif')
        Label(window, text='a',bg='white', image=image).pack()
        self.nB = Button(window, text="주변 정류소 검색", command=self.exeBusstop)
        self.nB.pack()
        self.sB = Button(window, text="버스 검색", bg='white',command=self.exeSearchBus)
        self.sB.pack()
        #민희쓰의 텔레그램봇
        self.TB = Button(window, text ="텔레그램봇과 연결",command = self.telegrambot)
        self.TB.pack()
        window.mainloop()

if __name__ == "__main__":
    selectMenu()
