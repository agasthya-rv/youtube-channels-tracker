import rest_functions
import helper_functions
import constants

def main():
    # Get the top-level channel categories list
    channel_categories = constants.CHANNEL_CATEGORIES
    file_txt = ''
    # For a given channel category, get the list of channels
    # For each channel in the channel category, get the latest videos and write to a file
    for channel_category, channel_list in channel_categories.items():
        channel_category_videos = rest_functions.get_channel_category_videos(channel_list)
        file_txt += helper_functions.generate_file_content(channel_category, channel_category_videos)

    helper_functions.write_to_text_file(file_txt, 'out') 


if __name__ == "__main__":
    main()