from chart import get_song_list
from datetime import datetime

#today_date = datetime.today().strftime('%Y-%m-%d')

dates = ['2019-11-11', '2023-04-01']
suffix = "x"
song_list = get_song_list(suffix, dates)

#print(len((song_list)))


#print(today_date)


#from datetime import datetime, timedelta

#today_date = datetime.today()
#yesterday_date = today_date - timedelta(days=1)
#yesterday_date_str = yesterday_date.strftime('%Y-%m-%d')

#print("Today's date is:", today_date.strftime('%Y-%m-%d'))
#print("Yesterday's date is:", yesterday_date_str)
