from datetime import datetime
import re
import pytz

def convert_to_datetime(date_time_string, format_ref = 1)->datetime:
    try:
        if format_ref == 1:
            return datetime.strptime(date_time_string,"%d-%m-%Y %I:%M %p")
        return datetime.strptime(date_time_string,"%Y-%m-%d %H:%M:%S")
    except :
        print(date_time_string,'Hi')
        print('Exception')
        return None
    
def calculate_date_time_difference(from_date, to_date):
    difference = to_date - from_date
    difference_days = difference.days
    difference_hours = difference.seconds/3600  # Get hours and remainder seconds
    #difference_minutes = remainder_seconds // 60  # Convert remainder seconds to minutes

    # Adjust difference if end_date time is before start_date time
    if to_date.time() < from_date.time():
        difference_days -= 1  # Adjust days
        difference_hours += 24  # Add 24 hours to hours
    return(difference_days,difference_hours) 

def check_if_matched(regex,val):
    return re.match(regex,val) is not None
