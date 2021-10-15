import constants
import os
from datetime import datetime

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
        for video in channel_videos:
            file_content += video + '\n'
    file_content += '\n'
    return file_content
