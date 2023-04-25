#statistic and research part for defining a right song 
import billboard

def get_song_list(suffix, dates):
    # create an empty list to store the chart data
    list2 = [] #list of all 
    list1 = [] #list of all original items
#    dates = ['2009-07-07', '2009-09-08']

    for custom_date in dates:
        chart = billboard.ChartData('hot-100', date=custom_date)

    # iterate over the chart data and append each item to the song_list
        for song in chart:
        #    song_list.append(song.title)
        #    song_list.append(song.artist)
            list2.append(song.title + " - " + song.artist)

    for i in range(len(list2)):
        list2[i] = str(list2[i])

    print(f"w new values: {list2}")

    for item in list2:
        if item not in list1:
            list1.append(item)
        else:
            print(f"{item} is duplicating an item in list1")
    return list1