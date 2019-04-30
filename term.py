from tkinter import *
from tkinter import ttk

class RestArea:
    def __init__(self):
        window = Tk()

        image = PhotoImage(file='image/kpu.gif')
        image2 = PhotoImage(file='image/great.gif')
        self.WindowWidth, self.WindowHeight = 400, 500
        window.geometry(str(self.WindowWidth) + 'x' + str(self.WindowHeight))

        self.LeftFrame = Frame(window, padx=20, pady=10)
        self.LeftFrame.pack(side=LEFT)

        self.RightFrame = Frame(window, padx=20, pady=10)
        self.RightFrame.pack(side=RIGHT)

        self.LeftPictureFrame = Frame(self.LeftFrame)
        self.LeftPictureFrame.pack()
        Label(self.LeftPictureFrame, text='a', image=image2).pack()

        self.RightPictureFrame = Frame(self.RightFrame, pady=15)
        self.RightPictureFrame.pack()
        Label(self.RightPictureFrame, text='a', image=image).pack()

        self.LeftComboFrame = Frame(self.LeftFrame, pady=30)
        self.LeftComboFrame.pack()

        self.country = ttk.Combobox(self.LeftComboFrame, height=10, textvariable=str)
        self.country['values'] = ('서울특별시', '경기도', '강원도', '경상북도', '경상남도', '전라북도', '전라남도')
        self.country.pack()

        self.LeftListFrame = Frame(self.LeftFrame)
        self.LeftListFrame.pack()

        self.scrollbar = Scrollbar(self.LeftListFrame)
        self.scrollbar.pack(side="right", fill="y")

        self.Llistbox = Listbox(self.LeftListFrame, yscrollcommand=self.scrollbar.set)
        self.Llistbox.pack()

        self.RightButtonFrame = Frame(self.RightFrame, pady=30)
        self.RightButtonFrame.pack()

        Button(self.RightButtonFrame, text='한식').pack(side=LEFT)
        Button(self.RightButtonFrame, text='중식').pack(side=LEFT)
        Button(self.RightButtonFrame, text='양식').pack(side=LEFT)
        Button(self.RightButtonFrame, text='화장실').pack(side=LEFT)

        self.RightInfoFrame = Frame(self.RightFrame)
        self.RightInfoFrame.pack()

        self.Rlistbox = Listbox(self.RightInfoFrame, height=5)
        self.Rlistbox.pack()
        print(self.Rlistbox.winfo_reqheight())
        self.canvas = Canvas(self.RightInfoFrame, bg='white', width=self.Rlistbox.winfo_reqwidth(), height=self.Rlistbox.winfo_reqheight())
        self.canvas.pack()



        window.mainloop()
RestArea()