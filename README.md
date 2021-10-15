# YouTube Channels Tracker

This fun project is created to fetch most recent videos for all the youtube channels that I follow. Instead of going to each channel and look for latest videos, we can run the main.py file and it returns the text file with most recent videos from all the channels. The text file will be stored in the "out" folder.

## High Level Design

1. Prepare a list of channels and store them in a Constant as per the above format
2. For each channel category in the constant variable, get the list of channels &nbsp
    1. For each channel, fetch the Uploads playlist Id using YouTube API
    2. Use the Uploads playlist Id from above step to fetch the most recent videos using YouTube API
3. Generate the text content and write to a text file in "out" folder

## Configuration Required

1. Get an YouTube API key and set it in the constants.py file (variable = API_KEY)
2. Set all the channels in the constants.py file (variable = CHANNEL_CATEGORIES)
3. Set the number of most recent videos to be returned in constants.py file (variable = VIDEOS_PER_CHANNEL)

Sample format for "CHANNEL_CATEGORIES" variable:

![a relative link](images/channel_obj_structure.jpg?raw=true)

## Sample Output Text File

![a relative link](images/out_file_structure.jpg?raw=true)

## Pending Enhancements

1. Exception Handling
2. Add the uploaded video date in the output text file
3. Have an option to input a date and only return the videos that were uploaded after that date
4. Write the output to an HTML file instead of a text file
