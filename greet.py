from constant import TIME
def get_time_of_day():
    if TIME < 12:
        return "Morning"
    elif TIME < 16:
        return "Afternoon"
    else:
        return "Evening"
    
def get_time_for_bye():
    if TIME > 12:
        return "Good Night"
    else:
        return "Have a nice day"
    
