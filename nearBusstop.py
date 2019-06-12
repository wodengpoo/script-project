from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from openAPI import *
from searchBus import *


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
        self.bsid = None
        self.curstid = self.retStid()
        print(self.stid[self.busstopindex])
        if self.citycombobox.get() == "서울특별시":
            self.buses, self.bsid = Sgetbusnm(urllib.parse.quote(self.stid[self.busstopindex]))
            self.Infolist = SgetbusInfo(self.curstid, self.bsid, self.buses)
            print(self.Infolist)
            print(self.bsid)
        else:
            self.buses, self.bsid = Kgetbusnm(urllib.parse.quote(self.stid[self.busstopindex]))
            self.Infolist = KgetbusInfo(self.curstid, self.bsid, self.buses)
            print(self.Infolist)
            print(self.bsid)

        if self.buses != None:
            if len(self.buses) == 0:
                messagebox.showinfo("Search fail", "경유버스정보가 없습니다.")
                return
            self.passbylist.delete(0, END)
            for i in self.buses:
                self.passbylist.insert(END, i)
            self.drawGraph()
    def drawGraph(self):
        self.frame4.pack_forget()
        self.frame4 = Frame(self.window)
        self.frame4.pack(side=LEFT, padx=20)
        Label(self.frame4, text='버스번호별 남은시간 그래프').pack()
        Label(self.frame4, text='0으로 출력되는 경우, API에서 제공하지 않는 정보이거나, 운행이 종료된 버스입니다.').pack()

        self.width , self.height = 50 * len(self.buses), 200
        self.canvas = Canvas(self.frame4, width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.delete("histogram")
        histograms = []
        if self.passbylist.size() == 0 : return
        self.canvas.create_line(10, self.height - 10, self.width - 10, self.height - 10)
        for i in self.Infolist:
            if self.citycombobox.get() == "서울특별시":
                L = list(filter(str.isdigit, i[1]))
                histograms.append(L)
                if len(L) != 0:
                    L.pop()
                print(histograms)
            else:
                pass
        cnt = 0
        for i in histograms:
            if len(i) == 2:
                i.insert(1, '0')
            if len(i) == 1:
                i.append('00')
            if len(i) > 4:
                while(len(i) > 4):
                    i.pop()
            s = ''
            for j in i:
                s += j
            if s == '':
                s = 0
            histograms[cnt] = int(s)
            cnt += 1
        print(histograms)
        if len(histograms) == 1:
            barW = 30
        else:
            barW = (self.width - 50) / (len(histograms) + 1)
        maxCount = int(max(histograms))
        if maxCount == 0 or len(histograms) == 0:
            messagebox.showinfo("ShowInfo", "제공 데이터가 존재하지 않습니다.")
            return
        vacant = 10
        print(vacant)
        for i in range(len(histograms)):
            self.canvas.create_rectangle(10 + barW * i + vacant * i, min(self.height - 10, self.height - (self.height - 15) * histograms[i] / maxCount),
                                         10 + barW * (i + 1) + vacant * i, self.height - 10, tags="histogram")
            self.canvas.create_text(10 + (i+1) * barW - barW/2 + vacant * i, self.height - 5, text=self.buses[i], tags="histogram")
            self.canvas.create_text(10 + (i+1) * barW - barW/2 + vacant * i, min(self.height-20, self.height - (self.height - 15) * histograms[i] / maxCount - 5),
                                    text=str(histograms[i])
                                    , tags="histogram")
    def searchBus(self):
        if self.citycombobox.get() == "서울특별시":
            searchBus(self.Infolist[self.passbylist.curselection()[0]], self.buses[self.passbylist.curselection()[0]], '서울특별시')
        else:
            searchBus(self.Infolist[self.passbylist.curselection()[0]], self.buses[self.passbylist.curselection()[0]], '경기도')
    def retStid(self):
        if len(self.busstoplist.curselection()) == 0: return None
        return self.stid[self.busstoplist.curselection()[0]]

    def __init__(self):
        self.window = Tk()
        self.window.geometry("+200+300")

        self.frame1 = Frame(self.window)
        self.frame1.pack()

        self.frame2 = Frame(self.window)
        self.frame2.pack(side=LEFT, padx=20)

        self.frame3 = Frame(self.window)
        self.frame3.pack(side=LEFT, padx=20)

        self.frame4 = Frame(self.window)
        self.frame4.pack(side=LEFT, padx=20)

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

        self.window.mainloop()

class map:

    def __init__(self, x='40.714728', y='-73.998672'):
        window = Toplevel()
        Label(window, text="지도").pack(anchor='w')

        import requests

        api_key = 'AIzaSyCtpYG4bU7y4irUBh_YjNCQBVaZFWETWs0'
        url = 'http://maps.googleapis.com/maps/api/staticmap?'
        center = str(x) + ',' + str(y)
        zoom = '12'

        r = requests.get(url + "center=" + center + "&zoom=" +
                         zoom + "&size=400x400&key=" + api_key)
        f = open('m.gif', 'wb')

        print(r.content)
        f.write(r.content)

        f.close()

        imgsrc = PhotoImage(file="m.gif")
        Label(window, image=imgsrc).pack()


        window.mainloop()


if __name__ == "__main__":
    nearBusstop()
    #map()