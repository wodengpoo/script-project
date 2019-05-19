from tkinter import *
from tkinter import ttk
from openAPI import *
import folium


class nearBusstop:
    def drawMap(self):
        #folium.Map(location = [37.568477,126.981611].zoom_start=13)
        #folium.Marker([37.568477,126.981611],popup = 'Mt.Hood Meadows').add_to(map_osm)
        #map_osm.save('osm.html')

        #folium.Marker([37.568477, 126.981611], popup='Mt. Hood Meadows').add_to(map_osm)
        #map_osm.save('osm.html')

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