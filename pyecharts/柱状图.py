# coding=utf-8
from pyecharts import Bar
from pyecharts import Line
#from pyecharts import Overlap
'''
attr = ["Poland", "Hungary", "Kazakhstan", "United States",
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
        "Ecuador", "Bolivian",]
'''
attr2= ["Poland", "Hungary", "Kazakhstan", "United States",
        "Malaysia", "Russia", "United Kingdom", "Pakistan", "Italy",
        "Kuwait", "Fiji", "Thailand", "Saudi Arabia", "Singapore",
        "Qatar", "The United Arab Emirates", "Cambodia",
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
v1 = [2, 2, 6, 13, 3, 10, 11, 12, 28,
      5, 3, 7, 1, 2, 2, 1, 5,
      9, 7, 8, 5, 17, 2, 5, 9, 2, 2,
      4, 1, 3, 6, 4, 4, 1, 2, 3, 1,
      1, 3, 1, 1, 4, 1, 1, 3, 2, 3,
      1, 3, 1, 3, 1, 5, 2, 3, 2, 1,
      3, 1, 2, 1, 1, 0, 0, 0, 0, 0,
      0, 0]
v2 = [0, 0, 1, 74, 7, 1, 1, 5, 3,
      0, 0, 0, 0, 1, 0,  0, 0,
      4, 1, 1, 2, 0, 0, 2, 0, 0, 0,
      0, 0, 0, 0, 4, 0, 0, 0, 0, 3,
      2, 0, 0, 0, 0, 0, 0, 1, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 1, 1, 4, 4, 1,
      2, 2]
v3 = [92, 93, 86, 15, 30, 91, 92, 71, 90,
      87, 92, 97, 91, 67, 93, 94, 93,
      69, 88, 89, 71, 91, 93, 71, 97, 90, 92,
      93, 91, 92, 93, 50, 96, 94, 94, 92, 25,
      33, 98, 92, 91, 93, 92, 91, 75, 100, 94,
      93, 92, 92, 91, 92, 93, 94, 92, 98, 91,
      93, 94, 92, 92, 96, 15, 12, 7, 6, 8,
      4, 8]
v3 = [v3[i]/5 for i in range(len(v3))]
#print(len(v1),len(v2),len(v3))
bar = Bar("主要国家的舆论倾向数据展示")
bar.add("积极", attr2, v1, mark_point=["average"], is_stack=True)
bar.add("消极", attr2, v2, mark_line=["min", "max"], is_stack=True,is_label_show=False,is_datazoom_show=True)
line = Line("")
line.add("积极占比",attr2,v3,is_stack=True,is_label_show=False,is_datazoom_show=True)
bar.render('柱形图.html')