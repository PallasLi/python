'''
Created on 2016年3月24日

@author: lyt
'''
import pygal
import pygal_maps_ch
line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012']
line_chart.add('Firefox', [1, 2, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [3, 2, 5, 77, 43, 22,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render()
line_chart.render_to_file("line_chart1.html")
# import os
# f=open('aaa.html','w')
# f.write(line_chart.render())
# f.close()
 
line_chart = pygal.Line()
line_chart.title = 'xiaorui.cc'
line_chart.x_labels = ['2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012']
line_chart.add('Firefox', [1, 2, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [3, 2, 5, 77, 43, 22,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
# return line_chart.render()
line_chart.render()
line_chart.render_to_file("line_chart2.html")


line_chart = pygal.StackedLine(fill=True)
line_chart.title = 'xiaorui.cc'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
# return line_chart.render()
line_chart.render()
line_chart.render_to_file("line_chart3.html")


pie_chart = pygal.Pie()
pie_chart.title = 'xiaorui.cc'
pie_chart.add('IE', 19.5)
pie_chart.add('Firefox', 36.6)
pie_chart.add('Chrome', 36.3)
pie_chart.add('Safari', 4.5)
pie_chart.add('Opera', 2.3)
# return pie_chart.render()
pie_chart.render()
pie_chart.render_to_file("pie_chart.html")
 

import pygal_maps_world.maps 
worldmap_chart = pygal_maps_world.maps.World()
worldmap_chart.title = 'Some countries'
worldmap_chart.add('F countries', ['fr', 'fi'])
worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
                               'mk', 'ml', 'mm', 'mn', 'mo',
                               'mr', 'mt', 'mu', 'mv', 'mw',
                               'mx', 'my', 'mz'])
worldmap_chart.add('U countries', ['ua', 'ug',  'uy', 'uz' ])
worldmap_chart.add('中国',{'us':2016,'jp':2016,'tw':2016,'hk':2016,'cn':2016})
# return worldmap_chart.render()
worldmap_chart.render()
worldmap_chart.render_to_file("world.svg")
# worldmap_chart.render_in_browser()

 