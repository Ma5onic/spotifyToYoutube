Relevant scripts:

1. spotifyJson.py
2. spotifyToYoutube.py


You begin in 1. where you first use the link commented out to get JSON of a spotify playlist's tracks
and put it in this same directory with line 8's filename, 'playlist.json'.

Script 1 will parse that json file and create a list of track name + artist names.
The output will be another json file, 'youtubePlaylist.json'.

Script 2 will use youtubePlaylist.json in order to search all of those songs and add to a youtube playlist
which the user will need to first manually create, then provide the script with that playlist's unique id in line 135.



TLDR:
visit
https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlists-tracks/
fill form: enter your spotify playlist id
get auth code
copy curl onto terminal, append, -o playlist.json
change max Size in spotifyJson.py to your playlist's # of songs
then run python spotifyJson.py

2. Then go to youtube.com and create an empty playlist, copy the playlist id
put it in line 135 of spotifyToYoutube.py

run python spotifyToYoutube.py

3. cd one directory up
copy the whole youtube playlist url, and a name of the folder where the videos will be downloaded

run python playlist.py youtube_playlist_url folder_name

Disclaimer: This is a project purely to improve python skills and making api calls. Since we are dealing with apis, we'll need to register as developer and use certain credentials, such as client_id.json, for the second script. Please proceed responsibly. 

