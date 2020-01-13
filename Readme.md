# CMCUCP
## The Complete Marvel Cinematic Universe Chronological Playlist

This is a simple script that generates a Plex playlist with everything in your library from the MCU, in chronological order (according to [this page](https://www.digitalspy.com/movies/a825774/marvel-cinematic-universe-in-chronological-order/)).

Fun fact: This is about 14 days of continuous video.

### Requirements
- Python 3.
- PIP.
- A Plex server somewhere.
- An unhealthily large collection of Marvel videos.

### Setup
- Clone this repo somewhere. Anywhere. Use your imagination.
- Install the dependencies with `pip install -r requirements.txt`.
- Create a config file with `cp example.config.ini config.ini`.
- Edit the config file to add your Plex credentials.
  - PLEX_USER is your Plex username/email.
  - PLEX_PASS is your Plex password.
  - PLEX_SERVER is the name of your Plex server.
  - PLEX_PLAYLIST is the name to give your new MCU playlist.

### Usage
- Just run `python cmcucp.py`.
- Wait.
- It will create a new playlist in your Plex library and report any items it couldn't find.

### Issues?
- Runaways season 3 is missing from my source, so isn't included at the moment.