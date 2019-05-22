from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from openAPI import *
from searchBus import *
#import folium


class nearBusstop:
    def drawMap(self):
        #folium.Map(location = [37.568477,126.981611].zoom_start=13)
        #folium.Marker([37.568477,126.981611],popup = 'Mt.Hood Meadows').add_to(map_osm)
        #map_osm.save('osm.html')

        #folium.Marker([37.568477, 126.981611], popup='Mt. Hood Meadows').add_to(map_osm)
        #map_osm.save('osm.html')

        map()

    def searchBusstop(self):
        self.sttns = None
        if self.posEntry.get() == '':
            messagebox.showinfo("Search fail", "키워드를 적어야 합니다.")
            return
        if self.citycombobox.get() == '':
            messagebox.showinfo("Search fail", "도시를 선택해야 합니다.")
            return
        elif self.citycombobox.get() == "서울특별시":
            self.sttns, self.stid = Sgetsttn(urllib.parse.quote(self.posEntry.get()))
        else:
            self.sttns, self.stid = Kgetsttn(urllib.parse.quote(self.posEntry.get()))

        if self.sttns != None:
            if len(self.sttns) == 0:
                messagebox.showinfo("Search fail", "검색 결과가 없습니다.")
                return
            self.busstoplist.delete(0, END)
            for i in self.sttns:
                self.busstoplist.insert(END, i)

    def printpassbyBuslist(self, evt):
        lb = evt.widget
        if len(lb.curselection()) == 0 : return
        self.busstopindex = lb.curselection()[0]
        # print(self.sttns[self.busstopindex])
        #print(self.stid)
        self.buses = None
        if self.citycombobox.get() == "서울특별시":
            self.buses = Sgetbusnm(urllib.parse.quote(self.stid[self.busstopindex]))
        else:
            self.buses = Kgetbusnm(urllib.parse.quote(self.stid[self.busstopindex]))

        if self.buses != None:
            if len(self.buses) == 0:
                messagebox.showinfo("Search fail", "경유버스정보가 없습니다.")
                return
            self.passbylist.delete(0, END)
            for i in self.buses:
                self.passbylist.insert(END, i)
    def searchBus(self):
        searchBus(self.retBusNM())
    def retBusNM(self):
        if len(self.passbylist.curselection()) == 0 : return None
        return self.buses[self.passbylist.curselection()[0]]

    def __init__(self):
        window = Tk()
        window.geometry("+200+300")

        self.frame1 = Frame(window)
        self.frame1.pack()

        self.frame2 = Frame(window)
        self.frame2.pack(side=LEFT, padx=20)

        self.frame3 = Frame(window)
        self.frame3.pack(side=LEFT, padx=20)

        Label(self.frame1, text="도시선택", width=10).pack(side=LEFT)

        self.citycombobox = ttk.Combobox(self.frame1, width=10, height=10, textvariable=str)
        self.citycombobox["values"] = tuple(("서울특별시", "경기도"))
        self.citycombobox.pack(side=LEFT, padx=10)

        Label(self.frame1, text="키워드", width=10).pack(side=LEFT)

        self.posEntry = Entry(self.frame1, width=10)
        self.posEntry.pack(side=LEFT, padx=10)

        Button(self.frame1, text="검색", width=5, command=self.searchBusstop).pack(side=LEFT)

        Label(self.frame2, text="주변정류소", width=10).pack()

        self.busstopframe = Frame(self.frame2)
        self.busstopframe.pack()
        self.scrollbar1 = Scrollbar(self.busstopframe)
        self.scrollbar1.pack(side="right", fill="y")
        self.busstoplist = Listbox(self.busstopframe, yscrollcommand=self.scrollbar1.set)
        self.busstoplist.bind("<<ListboxSelect>>", self.printpassbyBuslist)
        self.busstoplist.pack()

        Label(self.frame3, text="경유 버스 목록", width=10).pack()

        self.passbyframe = Frame(self.frame3)
        self.passbyframe.pack()
        self.scrollbar2 = Scrollbar(self.passbyframe)
        self.scrollbar2.pack(side="right", fill="y")
        self.passbylist = Listbox(self.passbyframe, yscrollcommand=self.scrollbar2.set)
        self.passbylist.pack()

        Button(self.frame3, text="버스 검색", command=self.searchBus).pack(side=LEFT)
        Button(self.frame3, text="지도 보기", command=self.drawMap).pack()

        window.mainloop()

class map:

    def __init__(self):
        window = Tk()
        Label(window, text="지도").pack(anchor='w')
        self.canvas = Canvas(window, width=400, height=400, bg='white')
        map_pos = [35.689551,139.700602]
        map_osm = folium.Map(location=map_pos, zoom_start=17)
        folium.CircleMarker(map_pos,radius= 100, color = '#3186cc',fill_color ='#3186cc').add_to(map_osm)

        marker_pos1= [35.686626,139.699062]
        folium.Marker(marker_pos1, popup= 'shinjuku Maynds Tower').add_to(map_osm)
        map_osm.save('osm.html')
        self.canvas = map_osm

        self.canvas.pack()
        window.mainloop()


if __name__ == "__main__":
    nearBusstop()