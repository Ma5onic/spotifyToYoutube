import json
import requests



# this is where you get your playlist Json from spotify
# https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlists-tracks/
# run the curl command in same directory and save to file 'playlist.json'


with open('playlist.json') as data:
    data = json.load(data)

trackAndArtist = []
# We need to get max size of playlist
maxSize = 48
for i in range(0, maxSize):
    trackName = data["items"][i]["track"]["name"]
    trackArtist = data["items"][i]["track"]["album"]["artists"][0]["name"]

    trackAndArtist.append(trackName + " - " + trackArtist)

trackAndArtist.sort()
for i in range(len(trackAndArtist)):
    print(trackAndArtist[i])
print(str(len(trackAndArtist)) + " songs total")



# we output a list of strings of tracknames + artists here to be used in search.py
with open('youtubePlaylist.json', 'w') as outfile:
    json.dump(trackAndArtist, outfile)
