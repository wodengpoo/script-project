from tkinter import *
from tkinter import ttk
from openAPI import *

class nearBusstop:
    def drawMap(self):
        map()
    def __init__(self):
        window = Tk()

        self.frame1 = Frame(window)
        self.frame1.pack()

        self.frame2 = Frame(window)
        self.frame2.pack(side=LEFT, padx=20)

        self.frame3 = Frame(window)
        self.frame3.pack(side=LEFT, padx=20)

        Label(self.frame1, text="도시선택", width=10).pack(side=LEFT)

        self.citycombobox = ttk.Combobox(self.frame1, width=10, height=10, textvariable=str)
        self.citycombobox["values"] = tuple(cityStrToCode.keys())
        self.citycombobox.pack(side=LEFT, padx=10)

        Label(self.frame1, text="위치값", width=10).pack(side=LEFT)

        self.posEntry = Entry(self.frame1, width=10)
        self.posEntry.pack(side=LEFT, padx=10)

        Button(self.frame1, text="검색", width=5).pack(side=LEFT)

        Label(self.frame2, text="주변정류소", width=10).pack()

        self.busstopframe = Frame(self.frame2)
        self.busstopframe.pack()
        self.scrollbar1 = Scrollbar(self.busstopframe)
        self.scrollbar1.pack(side="right", fill="y")
        self.busstoplist = Listbox(self.busstopframe, yscrollcommand=self.scrollbar1.set)
        self.busstoplist.pack()

        Label(self.frame3, text="경유 버스 목록", width=10).pack()

        self.passbyframe = Frame(self.frame3)
        self.passbyframe.pack()
        self.scrollbar2 = Scrollbar(self.passbyframe)
        self.scrollbar2.pack(side="right", fill="y")
        self.passbylist = Listbox(self.passbyframe, yscrollcommand=self.scrollbar2.set)
        self.passbylist.pack()

        Button(self.frame3, text="지도 보기", command=self.drawMap).pack()

        window.mainloop()

class map:
    def __init__(self):
        window = Tk()
        Label(window, text="지도").pack(anchor='w')
        self.canvas = Canvas(window, width=200, height=200, bg='white')
        self.canvas.pack()
        window.mainloop()

if __name__ == "__main__":
    nearBusstop()