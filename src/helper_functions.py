import os
from datetime import datetime, timedelta
import pytz
import constants

# Write content to text file and place in a folder
def write_to_text_file(content, folder_name):
    output_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', folder_name))
    file_name = datetime.today().strftime('%Y%m%d_%H%M%S') + '.txt'
    with open(os.path.join(output_directory,file_name), "w", encoding='utf-8') as text_file:
        text_file.write(content)

# Create content for the text file for a given channel category and associated channels
def generate_file_content(channel_category, channel_category_videos):
    file_content = '******** ' + channel_category + ' ********' 
    for channel_name, channel_videos in channel_category_videos.items():
        file_content += '\n' + channel_name + '\n'
        if len(channel_videos) < 1:
            file_content += 'No new videos uploaded \n'
        else:
            for video in channel_videos:
                file_content += video + '\n'
    file_content += '\n'
    return file_content

# Returns datetime in local timezone
def get_local_datetime():
    return datetime.now(tz=pytz.timezone(constants.MY_TIME_ZONE))

# Computes and returns datetime by subtracting delta time
def get_local_datetime_delta():
    return get_local_datetime() - timedelta(hours=constants.VIDEOS_TIME_DELTA)

# Converts and returns UTC datetime string to local datetime
def convert_to_local_datetime(utc_datetime_str):
    utc_dt_obj = datetime.strptime(utc_datetime_str,'%Y-%m-%dT%H:%M:%SZ')
    utc_dt = utc_dt_obj.replace(tzinfo=pytz.utc)
    return utc_dt.astimezone(pytz.timezone(constants.MY_TIME_ZONE))

# Converts and returns local datetime to local datetime string
def convert_to_local_datetime_string(local_datetime):
    return local_datetime.strftime(constants.LOCAL_DATE_TIME_FORMAT)   