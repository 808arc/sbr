import billboard

def get_song_list_with_suffix(suffix, dates):
    """
    Returns a list of Billboard chart data with a given suffix for the song titles and artist names
    within a range of dates.

    Parameters:
    suffix (str): The suffix to append to the end of each song title and artist name.
    dates (list of str): A list of date strings in the format YYYY-MM-DD.

    Returns:
    A list of strings representing the song titles and artist names with the given suffix.
    """

    # Create empty lists to store the chart data
    list2 = []
    list1 = []

    for custom_date in dates:
        chart = billboard.ChartData('hot-100', date=custom_date)

        # Iterate over the chart data and append each item to the list2
        for song in chart:
            list2.append(song.title + " - " + song.artist)

    # Append suffix to each item in list2
    for i in range(len(list2)):
        list2[i] = str(list2[i]) + suffix

    # Find duplicates in list1
    for item in list2:
        if item not in list1:
            list1.append(item)
        else:
            print(f"{item} is duplicating an item in list1")

    return list1
