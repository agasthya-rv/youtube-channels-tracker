import helper_functions
import constants

# Make a list of channels -> Programming, PF, Trading, Economics & Misc
# Have a date to compare and return recent videos
# For each channel, get Uploads playlist Id, pass it and get the videos
# Compare with the date and return latest videos
# Videos Format: Channel Category, Channel Name, Title - Link

def main():
    channel_list = constants.TEST_CHNL
    channel_videos = {}
    for key in channel_list:
        channel_id = channel_list[key]
        uploads_playlist_id = helper_functions.get_playlist_id(channel_id)
        # print("Uploads Playlist Id: ",uploads_playlist_id)
        if uploads_playlist_id:
            videos_list = helper_functions.get_top_videos(uploads_playlist_id)
            # print(videos_list)
            channel_videos[key] = videos_list
    return channel_videos


if __name__ == "__main__":
    channel_videos = main()
    print(channel_videos)