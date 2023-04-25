import time
from youtubesearchpython import VideosSearch

track_info_list = list1
link_list = []

for Prod_Name in track_info_list:
    videosSearch = VideosSearch(Prod_Name, limit=1)
    try:
        first_result = videosSearch.result()["result"][0]
        link_list.append(first_result["link"])
    except IndexError:
        print(f"No video link found for {Prod_Name}")
    time.sleep(1)

print(link_list)