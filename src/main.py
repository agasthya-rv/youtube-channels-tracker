import rest_functions
import helper_functions
import constants

def main():
    # Get the top-level channel categories list
    channel_categories = constants.CHANNEL_CATEGORIES
    file_txt = ''
    uploads_playlist_map = {}
    print("Executing YouTube Channels Tracker script ...")

    # Load uploads playlist Id map from json file, if file exists
    json_file_path = helper_functions.get_file_path(constants.JSON_FILE_PATH)
    if helper_functions.is_file_exists(json_file_path):
        print("Reading all Uploads Playlist Ids from channels_playlistIds.json file")
        uploads_playlist_map = helper_functions.read_from_json_file(json_file_path)

    # For a given channel category, get the list of channels
    # For each channel in the channel category, get the uploads playlist Id and latest videos and write to a file
    for channel_category, channel_list in channel_categories.items():
        print("Refreshing Uploads Playlist Ids for all channels in channel category -> ",channel_category)
        uploads_playlist_map = rest_functions.get_all_playlist_ids(channel_list,uploads_playlist_map)    
        print("Fetching videos for all channels in channel category -> ",channel_category)
        channel_category_videos = rest_functions.get_channel_category_videos(channel_list, uploads_playlist_map)
        file_txt += helper_functions.generate_file_content(channel_category, channel_category_videos)

    print("Writing videos list to output file ...")
    helper_functions.write_to_text_file(file_txt, 'out')
    print("Saving all Uploads Playlist Ids to channels_playlistIds.json file")
    helper_functions.write_to_json_file(uploads_playlist_map,json_file_path)


if __name__ == "__main__":
    main()