import requests
import helper_functions
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

# Get all playlist Ids for a given channel category
def get_all_playlist_ids(channel_list, playlist_id_map):
    playlist_keys = playlist_id_map.keys()
    for channel in channel_list:
        channel_id = channel_list[channel]
        if channel_id not in playlist_keys:
            uploads_playlist_id = get_playlist_id(channel_id, 'uploads')
            if uploads_playlist_id:
                playlist_id_map[channel_id] = uploads_playlist_id
    return playlist_id_map

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

# Get most recent videos for a given playlist Id with date-time delta
def get_recent_published_videos(playlist_id):
    local_date_delta = helper_functions.get_local_datetime_delta()
    response = fetch_videos(playlist_id, constants.VIDEOS_PER_CHANNEL)
    videos_list = []
    if 'items' in response:
        for item in response['items']:
            video_published_date = item['snippet']['publishedAt']
            local_video_published_date = helper_functions.convert_to_local_datetime(video_published_date)
            if local_video_published_date > local_date_delta:
                video_title = item['snippet']['title']
                video_id = item['snippet']['resourceId']['videoId']
                video_url = constants.YOUTUBE_URL + 'watch?v=' + video_id
                videos_list.append(video_title + ": " + video_url + " | Published: " \
                    + helper_functions.convert_to_local_datetime_string(local_video_published_date))    
    return videos_list

# Get latest videos per channel in a given channel category
# Example: Programming Channel Category => Programming Channel1, Programming Channel2
# This function will return videos for both Programming Channel1 & Programming Channel2
def get_channel_category_videos(channel_list, uploads_playlist_map):
    channel_category_videos = {}
    for channel in channel_list:
        channel_id = channel_list[channel]
        #uploads_playlist_id = get_playlist_id(channel_id, 'uploads')
        uploads_playlist_id = uploads_playlist_map[channel_id]
        # print("Uploads Playlist Id: ", uploads_playlist_id)
        if uploads_playlist_id:
            videos_list = get_recent_published_videos(uploads_playlist_id)
            # print(videos_list)
            channel_category_videos[channel] = videos_list
    return channel_category_videos