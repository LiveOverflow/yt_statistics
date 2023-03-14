import yt, json
from datetime import datetime

channels = {
    "codingo": "codingo",
    "LiveOverflow": "UClcE-kVhqyiHCcjYwcpfj9w",
    "PwnFunction": "UCW6MNdOsqv2E9AjQkv9we7A",
    "JohnHammond": "_JohnHammond",
    "IppSec": "UCa6eh7gCkpPo5XXUDfygQQA",
    "NahamSec": "UCCZDt7MuC3Hzs6IH4xODLBw",
    "STÖK": "UCQN2DsjnYH60SFBIA6IkNwg",
    "InsiderPhD": "RapidBug",
    "The Cyber Mentor": "TCMSecurityAcademy",
    "HackerSploit": "HackerSploit",
    "Bug Bounty Reports Explained": "BugBountyReportsExplained",
    "GynvaelEN": "GynvaelEN",
    "Alex Chaveriat": "AlexChaveriat",
    "c0nd4": "c0nd4",
    "247CTF": "247CTF",
    "Farah Hawa": "FarahHawa",
    "PinkDraconian": "PinkDraconian",
    "0xdf": "0xdf",
    "zSecurity": "zSecurity",
    "DerekRook": "DerekRook",
    "CryptoCat": "_CryptoCat",
    "Lupin": "0xlupin",
    "Stefan Rows": "StefanRows",
    "Hacksplained": "Hacksplained",
    "Reconless": "reconless1983",
    "hakluke": "hakluke",
    "stacksmashing": "stacksmashing",
    "Low Level Learning": "LowLevelLearning",
    "David Bombal": "davidbombal",
}

with open("all_videos.jsonl", "w") as f:

    for channel in channels:

        videos = yt.list_videos(channels[channel])
        for video in videos:
            title = video['snippet']['title']
            video_id = video['contentDetails']['videoId']
            thumbnail = video['snippet']['thumbnails']['high']['url']
            published = datetime.strptime(video['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").date()
            print(f"{title} - {video_id} - {thumbnail} - {published}")
            channel_id = video['snippet']['channelId']

            details = yt.video_details(video_id)
            print(details)
            if 'tags' in details['snippet']:
                tags = details['snippet']['tags']
            else:
                tags = []
            print(tags)
            title = title.replace(",", " ")
            date = video['snippet']['publishedAt']
            views = details['statistics']['viewCount']
            likes = details['statistics']['likeCount']
            if 'commentCount' in details['statistics']:
                comments = details['statistics']['commentCount']
            else:
                comments = 0
            f.write(json.dumps({
                "channel": channel,
                "channel_id": channel_id,
                "video_id": video_id,
                "title": title,
                "thumbnail": thumbnail,
                "published": video['snippet']['publishedAt'],
                "tags": tags,
                "views": int(views),
                "likes": int(likes),
                "comments": int(comments)
            })+"\n")

