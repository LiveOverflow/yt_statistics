# yt_statistics

This repository contains various data from the LiveOverflow YouTube channel (`liveoverflow_videos.jsonl`) and other security creators (`all_videos.jsonl`).
Data was last pulled on 15.03.2023.

```json
{
    "channel_id": "UClcE-kVhqyiHCcjYwcpfj9w",
    "video_id": "MS7WRuzNYDc",
    "thumbnail": "https://i.ytimg.com/vi/MS7WRuzNYDc/hqdefault.jpg",
    "date": "2022-10-21T15:55:18Z",
    "views": "260530",
    "tags": ["ip address", "leak", "..."],
    "title": "I Leaked My IP Address!",
    "description": "How bad is it to leak your IP address? VPN providers..."
}
```

Each `video_id` in the `liveoverflow_videos.jsonl` has a corresponding `liveoverflow_transcripts/<video_id>.txt` file:

```
Is leaking your IP address really dangerous? It 
seems like many people think so, because because
when I released my minecraft hacking video 
series, I kept leaking my personal IP,
as well as the IP of other players (oops sorry?). 
After that I got tons of worrying messages telling
...
```

Feel free to use the data to create some statistics, or train a LiveOverflow script writing AI (but pls let me use it too :P)