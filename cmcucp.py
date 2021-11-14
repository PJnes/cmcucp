import math, sys
from plexapi.myplex import MyPlexAccount
from plexapi.playlist import Playlist
from plexapi.exceptions import NotFound

# Parse Arguments
if len(sys.argv) < 4:
    print("Arguments: PLEX_USER PLEX_PASS PLEX_SERVER [PLEX_PLAYLIST]")
    exit(1)

plex_user = sys.argv[1]
plex_pass = sys.argv[2]
plex_server = sys.argv[3]
plex_playlist = "Complete MCU Chronological Playlist"

if len(sys.argv) == 5:
    plex_playlist = sys.argv[4]


# Add a movie from plex to the playlist.
def addmovie(title):
    results = plex.library.search(title=title, libtype="movie")
    if results:
        # Just use the first result, this could be smarter.
        items.append(results[0])
        print("Added %(title)s" % {'title': title})
    else:
        errors.append(title)
        print("Failed to add %(title)s" % {'title': title})


# Add a TV show episode or range of episodes from plex to the playlist.
def addtv(show, season, episode, end=False):
    # Default to single episode if no end value.
    if not end:
        end = episode
    end = end + 1

    results = plex.library.search(title=show, libtype="show")
    for number in range(episode, end):
        values = {'show': show, 'season': season, 'number': number}
        try:
            item = results[0].episode(season=season, episode=number)
        except (NotFound, IndexError):
            errors.append("%(show)s Season %(season)d Episode %(number)d" % values)
            print("Failed to add %(show)s Season %(season)s Episode %(number)s" % values)
        else:
            items.append(item)
            print("Added %(show)s Season %(season)s Episode %(number)s" % values)


# Login
try:
    account = MyPlexAccount(plex_user, plex_pass)
    plex = account.resource(plex_server).connect()
    print("Logged in to %(server)s as %(user)s" % {'server': plex_server, 'user': plex_user})
except:
    print("Failed to login to %(server)s as %(user)s" % {'server': plex_server, 'user': plex_user})
    exit()

# Delete existing playlist
try:
    plex.playlist(plex_playlist).delete()
    print("Removing existing playlist called '%(playlist)s" % {'playlist': plex_playlist})
except:
    print("No existing playlist called '%(playlist)s" % {'playlist': plex_playlist})


items = []
errors = []


# Order Source: https://www.digitalspy.com/movies/a825774/marvel-cinematic-universe-in-chronological-order/
addmovie("Captain America: The First Avenger")
addtv("Marvel's Agent Carter", 1, 1, 8)
addtv("Marvel's Agent Carter", 2, 1, 10)
# Agent Carter (one-shot on Iron Man 3 DVD)
addmovie("Captain Marvel")
addmovie("Iron Man")
addmovie("Iron Man 2")
addmovie("The Incredible Hulk")
# The Consultant (one-shot on the Thor DVD)
# A Funny Thing Happened on the Way to Thor's Hammer (one-shot on the Captain America: The First Avenger DVD)
addmovie("Thor")
addmovie("The Avengers")
# Item 47 (one-shot on the Avengers Assemble DVD)
addmovie("Iron Man 3")
# All Hail the King (one-shot on the Thor: The Dark World DVD)
addtv("Marvel's Agents of S.H.I.E.L.D.", 1, 1, 7)
addmovie("Thor: The Dark World")
addtv("Marvel's Agents of S.H.I.E.L.D.", 1, 8, 16)
addmovie("Captain America: The Winter Soldier")
addtv("Marvel's Agents of S.H.I.E.L.D.", 1, 17, 22)
addmovie("Guardians of the Galaxy")
addmovie("Guardians of the Galaxy Vol. 2")
addtv("Marvel's Daredevil", 1, 1, 13)
addtv("Marvel's Agents of S.H.I.E.L.D.", 2, 1, 10)
addtv("Marvel's Jessica Jones", 1, 1, 13)
addtv("Marvel's Agents of S.H.I.E.L.D.", 2, 11, 19)
addmovie("Avengers: Age of Ultron")
addtv("Marvel's Agents of S.H.I.E.L.D.", 2, 20, 22)
addtv("Marvel's Daredevil", 2, 1, 4)
addtv("Marvel's Luke Cage", 1, 1, 4)
addtv("Marvel's Daredevil", 2, 5, 11)
addtv("Marvel's Luke Cage", 1, 5, 8)
addtv("Marvel's Daredevil", 2, 12, 13)
addtv("Marvel's Luke Cage", 1, 9, 13)
addmovie("Ant-Man")
addtv("Marvel's Agents of S.H.I.E.L.D.", 3, 1, 10)
addtv("Marvel's Agents of S.H.I.E.L.D.", 3, 11, 19)
addtv("Marvel's Iron Fist", 1, 1, 13)
addmovie("Captain America: Civil War")
addtv("Marvel's Agents of S.H.I.E.L.D.", 3, 20, 22)
addtv("Marvel's The Defenders", 1, 1, 8)
addtv("Marvel's Agents of S.H.I.E.L.D.", 4, 1, 6)
addmovie("Doctor Strange")
addmovie("Black Panther")
addtv("Marvel's Agents of S.H.I.E.L.D.", 4, 7, 8)
# Marvel's Agents of S.H.I.E.L.D.: Slingshot (season 1, eps 1-6)
addtv("Marvel's Agents of S.H.I.E.L.D.", 4, 9, 22)
addmovie("Spider-Man: Homecoming")
addmovie("Thor: Ragnarok")
addtv("Marvel's Inhumans", 1, 1, 8)
addtv("Marvel's The Punisher", 1, 1, 13)
addtv("Marvel's Runaways", 1, 1, 10)
addtv("Marvel's Agents of S.H.I.E.L.D.", 5, 1, 10) # allowing for time travel craziness
addtv("Marvel's Jessica Jones", 2, 1, 13)
addtv("Marvel's Agents of S.H.I.E.L.D.", 5, 11, 18)
addtv("Marvel's Cloak & Dagger", 1, 1, 10)
addtv("Marvel's Cloak & Dagger", 2, 1, 10)
addtv("Marvel's Luke Cage", 2, 1, 13)
addtv("Marvel's Iron Fist", 2, 1, 10)
addtv("Marvel's Daredevil", 3, 1, 13)
addtv("Marvel's Runaways", 2, 1, 13)
addtv("Marvel's The Punisher", 2, 1, 13)
addtv("Marvel's Jessica Jones", 3, 1, 13)
addmovie("Ant-Man and the Wasp")
addmovie("Avengers: Infinity War")
addtv("Marvel's Agents of S.H.I.E.L.D.", 5, 19, 22) # Concurrent with Infinity War
addtv("Marvel's Agents of S.H.I.E.L.D.", 6, 1, 13) # takes place in Endgame's five-year time jump
addtv("Marvel's Agents of S.H.I.E.L.D.", 7, 1, 13) # takes place in Endgame's five-year time jump
addtv("Marvel's Runaways", 3, 1, 10)
addmovie("Avengers: Endgame")
addtv("Loki", 1, 1, 6)
addtv("WandaVision", 1, 1, 9)
addtv("The Falcon and the Winter Soldier", 1, 1, 6)
addmovie("Spider-Man: Far From Home")

print("----------------------------------------------------")

# Create playlist
if len(items) > 0:
    playlist = Playlist.create(plex, plex_playlist, items = items)
else:
    print("Script couldn't find any items to add to your MCU playlist")
    exit()

# Get playlist duration
hours = math.floor(playlist.duration / 1000 / 60 / 60)
time = "%(days)d days and %(hours)d hours" % { 'days': math.floor(hours / 24), 'hours': hours % 24}

if len(errors) > 0:
    print("The following files could not be found to add to the playlist.")
    for item in errors:
        print("- %(item)s" % {'item': item})
    print("Run the script again once these items are in Plex.")

print("----------------------------------------------------")
print("Enjoy %(time)s of the MCU!" % {'time': time})
