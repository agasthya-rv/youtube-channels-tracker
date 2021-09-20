import requests
import constants

def fetch_playlists(channel_id):
    api_url = constants.CHANNELS_URL + "?part=contentDetails&id=" + channel_id + "&key=" + constants.API_KEY
    resp = requests.get(api_url)
    #print("Get Playlist Response:", resp)
    return resp.json()

def fetch_videos(playlist_id, max_results):
    api_url = constants.PLAYLIST_URL + "?part=snippet&maxResults=" + str(max_results) + "&playlistId=" + playlist_id
    api_url += "&key=" + constants.API_KEY
    resp = requests.get(api_url)
    #print("Get Videos Response:", resp)
    return resp.json()

def get_playlist_id(channel_id):
    response = fetch_playlists(channel_id)
    playlist_id = ''
    if 'items' in response:
       playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    return playlist_id

def get_top_videos(playlist_id):
    response = fetch_videos(playlist_id,5)
    videos_list = []
    if 'items' in response:
        for item in response['items']:
            video_title = item['snippet']['title']
            video_id = item['snippet']['resourceId']['videoId']
            video_url = constants.YOUTUBE_URL + 'watch?v=' + video_id
            videos_list.append(video_title + ": " + video_url)
        
    return videos_list