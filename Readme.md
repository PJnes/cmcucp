# CMCUCP: The Complete Marvel Cinematic Universe Chronological Playlist

This is a simple script that generates a Plex playlist with everything in your library from the MCU, in chronological order (according to [this page](https://www.digitalspy.com/movies/a825774/marvel-cinematic-universe-in-chronological-order/)).

Fun fact: This is about 17 days of continuous video.

I've created a web based version of this, that provides chonological playlists for the MCU, as well as Star Wars, Doctor Who, Star Trek and others.

You should check out [Chronoplex](https://chronoplex.app), it does a [prettier MCU chronological playlist](https://chronoplex.app/mcu)

## The new fancy docker way

- `docker run --rm ghcr.io/pjnes/cmcucp PLEX_USER PLEX_PASS PLEX_SERVER [PLEX_PLAYLIST]`

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
