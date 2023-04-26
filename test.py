#for test purposes only 
import billboard

# create an empty list to store the chart data
list2 = [] #list of all songs for current date 

# get the dates you want to search for
dates = ['2009-07-07', '2009-09-08']

# retrieve song titles from the Billboard API for each date
for custom_date in dates:
    chart = billboard.ChartData('hot-100', date=custom_date)
    # iterate over the chart data and append each item to list2
    for song in chart:
        list2.append(song.title)

# remove any duplicate song titles from list2
list2 = list(set(list2))

# write the unique song titles to song_titles.txt
with open("song_titles.txt", "w") as f:
    for title in list2:
        f.write(title + "\n")

# print the unique song titles
print(f"New values in song_titles.txt: {list2}")
