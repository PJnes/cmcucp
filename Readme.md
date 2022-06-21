# CMCUCP: The Complete Marvel Cinematic Universe Chronological Playlist
## This is fork of the repository from [PJnes / cmcucp](https://github.com/PJnes/cmcucp)

I have modified the original one with this mechanics:
- outsourcing of playlist to file (mcuchronologicalplaylist.txt) --> make editing easier
- if there is no playlist with the name you choosed --> it creates the playlist
- if there is already a playlist with the same name --> it looks inside the playlist and gives you the choice
- -> if you have more items in you library you can add them and check the order
- -> if you have the wrong content in your playlist you can remove them and check order
- -> if the playlist is up to date you can check the order

This is a simple script that generates a Plex playlist with everything in your library from the MCU, in chronological order (according to [this page](https://www.digitalspy.com/movies/a825774/marvel-cinematic-universe-in-chronological-order/)).

Fun fact: This is about 17 days of continuous video.

## The new fancy docker way

- `docker run --rm ghcr.io/cm86/cmcucp PLEX_USER PLEX_PASS PLEX_SERVER [PLEX_PLAYLIST]`

## The old manual way

### Requirements

- Python 3.
- PIP.
- A Plex server somewhere.
- An unhealthily large collection of Marvel videos.

### Setup

- Clone this repo somewhere. Anywhere. Use your imagination.
- Install the dependencies with `pip install -r requirements.txt`.

### Usage

- Just run `python cmcucp.py PLEX_USER PLEX_PASS PLEX_SERVER [PLEX_PLAYLIST]`.
- Wait.
- It will create a new playlist in your Plex library and report any items it couldn't find.
