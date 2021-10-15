import requests
import constants

# Get all Playlists from YouTube API for a given Channel Id 
def fetch_playlists(channel_id):
    api_url = constants.CHANNELS_URL + "?part=contentDetails&id=" + channel_id + "&key=" + constants.API_KEY
    resp = requests.get(api_url)
    #print("Get Playlist Response:", resp)
    #print("Get Playlist Response:", resp.json())
    return resp.json()

# Get Videos from YouTube API for a given Channel Playlist Id 
def fetch_videos(playlist_id, max_results):
    api_url = constants.PLAYLIST_URL + "?part=snippet&maxResults=" + str(max_results) + "&playlistId=" + playlist_id
    api_url += "&key=" + constants.API_KEY
    resp = requests.get(api_url)
    #print("Get Videos Response:", resp)
    #print("Get Videos Response:", resp.json())
    return resp.json()

# Get the playlist Id for a Given channel Id and playlist name
def get_playlist_id(channel_id, playlist_name):
    response = fetch_playlists(channel_id)
    playlist_id = ''
    if 'items' in response:
       playlist_id = response['items'][0]['contentDetails']['relatedPlaylists'][playlist_name]
    return playlist_id

# Get most recent videos for a given playlist Id
def get_recent_videos(playlist_id):
    response = fetch_videos(playlist_id, constants.VIDEOS_PER_CHANNEL)
    videos_list = []
    if 'items' in response:
        for item in response['items']:
            video_title = item['snippet']['title']
            video_id = item['snippet']['resourceId']['videoId']
            video_url = constants.YOUTUBE_URL + 'watch?v=' + video_id
            videos_list.append(video_title + ": " + video_url)    
    return videos_list

# Get latest videos per channel in a given channel category
# Example: Programming Channel Category => Programming Channel1, Programming Channel2
# This function will return videos for both Programming Channel1 & Programming Channel2
def get_channel_category_videos(channel_category):
    channel_category_videos = {}
    for channel in channel_category:
        channel_id = channel_category[channel]
        uploads_playlist_id = get_playlist_id(channel_id, 'uploads')
        # print("Uploads Playlist Id: ", uploads_playlist_id)
        if uploads_playlist_id:
            videos_list = get_recent_videos(uploads_playlist_id)
            # print(videos_list)
            channel_category_videos[channel] = videos_list
    return channel_category_videos