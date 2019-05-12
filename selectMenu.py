from tkinter import *
from searchBus import *
from nearBusstop import *

class selectMenu:
    def exeBusstop(self):
        nearBusstop()
    def exeSearchBus(self):
        searchBus()
    def __init__(self):
        window = Tk()

        getData() #도시 코드 정보를 가져옴
        image = PhotoImage(file='image/kpu.gif')
        Label(window, text='a', image=image).pack()
        self.nB = Button(window, text="주변 정류소 검색", command=self.exeBusstop)
        self.nB.pack()
        self.sB = Button(window, text="버스 검색", command=self.exeSearchBus)
        self.sB.pack()

        window.mainloop()

if __name__ == "__main__":
    selectMenu()