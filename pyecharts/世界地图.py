from pyecharts import Map,Geo
value = [95 ,92 ,93 ,86 ,15, 30 ,91 ,92 ,71 ,90 ,87 ,92 ,97 ,91 ,67 ,93 ,100 ,96 ,94 ,93 ,69 ,88 ,89 ,71 ,91 ,93 ,71 ,
         97 ,90 ,92 ,93 ,91 ,92 ,93 ,50 ,96 ,94 ,94 ,92 ,25 ,33 ,98 ,92 ,91 ,93 ,92 ,91 ,75 ,100 ,94 ,93 ,92 ,92 ,91 ,
         92 ,93 ,94 ,92 ,98 ,91 ,93 ,94 ,92 ,92 ,96 ,15 ,12 ,7 ,6 ,8 ,4 ,8 ,]
attr = ["China", "Poland", "Hungary", "Kazakhstan", "United States",
        "Malaysia", "Russia", "United Kingdom", "Pakistan", "Italy",
        "Kuwait", "Fiji", "Thailand", "Saudi Arabia", "Singapore",
        "Qatar", "Tanzania", "Africa", "The United Arab Emirates", "Cambodia",
        "Germany", "New Zealand", "Japan", "Australia", "France",
        "Israel", "Greece", "Mongolia", "Afghanistan", "Kyrgyzstan",
        "Tanzania", "Milan", "Mexico", "Egypt", "Kenya",
        "Laos", "Slovakia", "Ethiopia", "Nepal", "Sri Lanka",
        "Latin America", "Panama", "The Republic of Korea", "Luxembourg", "Spain",
        "Serbia", "Monaco", "Vietnam", "Belgium", "Switzerland",
        "Uruguay", "Argentina", "Peru", "Brazil", "South Africa",
        "Cuba", "Portugal", "Sultan", "The People's Republic of Bangladesh", "Madagascar",
        "Nigeria", "Azerbaijan", "Uzbekistan", "Tehran", "Chile",
        "Columbia", "Turkey", "Canada", "India", "Myanmar",
        "Ecuador", "Bolivian"]
map0 = Map("面向“一带一路”的国内外舆论倾向性分布情况",title_pos="center",  title_text_size=25, width=1200, height=600)
map0.add("积极舆论占比", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000', is_map_symbol_show=False,visual_range=[0,100],legend_pos="right")
map0.render(path="世界地图.html")
