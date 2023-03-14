import requests
import os
from youtube_transcript_api import YouTubeTranscriptApi


headers = {
    "x-origin": "https://explorer.apis.google.com",
}

KEY = os.environ.get("KEY")

# return YouTube channel id via handle or False if failed
def scraping_get_channel_id_from_handle(handle:str):
    url_channel = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={handle}&type=channel&key={KEY}"
    response = requests.get(url_channel, headers=headers)
    j = response.json()
    if 'items' not in j:
        return False
    return j['items'][0]['snippet']['channelId']


def get_captions(video_id):
    try:
        YouTubeTranscriptApi.list_transcripts(video_id)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])
        transcript_text = transcript.fetch()
    except:
        return
    
    transcript_filename = f"transcripts/{video_id}.txt"
    with open(transcript_filename, "w", encoding="utf-8") as f:
        for t in transcript_text:
            f.write(t['text'].strip()+"\n")
    print(transcript_filename)

def get_captions_api(video_id):
    url_captions = f"https://content-youtube.googleapis.com/youtube/v3/captions?videoId={video_id}&part=snippet&key={KEY}"
    response = requests.get(url_captions, headers=headers)
    j = response.json()
    if 'items' not in j:
        print(f"cannot get captions: {video_id}")
        return False
    caption_id = None
    for item in j['items']:
        if not caption_id:
            caption_id = item['id']
        if item['snippet']['trackKind'] == 'asr':
            caption_id = item['id']
    if not caption_id:
        print(f"cannot find captions: {video_id}")
        return []
    url_caption = f"https://youtube.googleapis.com/youtube/v3/captions/{caption_id}?key={KEY}"
    response = requests.get(url_caption, headers=headers)
    j = response.json()
    print(j)


def list_videos(channel_id, **kwargs):
    if not channel_id:
        return []
    part = "snippet,contentDetails,statistics"
    url_channel = f"https://www.googleapis.com/youtube/v3/channels?part={part}&id={channel_id}&key={KEY}"
    response = requests.get(url_channel, headers=headers)
    j = response.json()
    if 'items' not in j:
        print(response.text)
        print(f"cannot find channel: {channel_id}")
        return list_videos(scraping_get_channel_id_from_handle(channel_id))
    playlist_id = j['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    pageToken = None
    while True:
        url_playlist = f"https://content-youtube.googleapis.com/youtube/v3/playlistItems?maxResults=50&playlistId={playlist_id}&part=contentDetails%2Csnippet&key={KEY}"
        if pageToken:
            url_playlist = f"https://content-youtube.googleapis.com/youtube/v3/playlistItems?maxResults=50&playlistId={playlist_id}&part=contentDetails%2Csnippet&key={KEY}&pageToken={pageToken}"
        print(url_playlist)
        j = requests.get(url_playlist, headers=headers).json()
        if 'items' not in j:
            print(response.text)
            print(f"cannot load playlist: {channel_id}")
        videos += j['items']
        if 'nextPageToken' in j:
            pageToken = j['nextPageToken']
        else:
            break
    return videos

def video_details(video_id):
    video_url = f"https://content-youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={KEY}"
    response = requests.get(video_url, headers=headers)
    j = response.json()
    if 'items' not in j:
        print(f"cannot find video: {video_id}")
        print(response.text)
        return None
    return j['items'][0]

