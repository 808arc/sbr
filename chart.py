#statistic and research part for defining a right song 
import billboard
from datetime import datetime

# create an empty list to store the chart data
list2 = [] #list of all 
list1 = [] #list of all original items

track_name = []
track_artist = []

dates = ['2009-07-07', '2009-09-08']

for custom_date in dates:

#custom_date = datetime.today().strftime('%Y-%m-%d')
#custom_date = '2007-07-07'

    chart = billboard.ChartData('hot-100', date=custom_date)

# iterate over the chart data and append each item to the song_list
    for song in chart:
    #    song_list.append(song.title)
    #    song_list.append(song.artist)
        list2.append(song.title + " - " + song.artist)
    


x = "x" # define x as the fixed letter you want to add

for i in range(len(list2)):
    list2[i] = str(list2[i]) + x

print(f"w new values: {list2}")

for item in list2:
    if item not in list1:
        list1.append(item)
    else:
        print(f"{item} is duplicating an item in list1")
