import math, sys
import collections
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
playlist_exists = ""
existingitems = ""
existingitems_list = ""
items = []
searchitems = []
errors = []
searcherrors = []

if len(sys.argv) == 5:
    plex_playlist = sys.argv[4]

# read the playlist from file
def readplaylistfromfile():
  with open("./mcuchronologicalplaylist.txt", "r") as f:
    global playlistfile 
    playlistfile = []
    for playlistfileitem in f:
        number = 0
        while number == 0:
          if playlistfileitem.startswith("#"):
#            print(" skipping line" + playlistfileitem)
            number += 1
          else:
            playlistfile.append(playlistfileitem.rstrip('\n'))
            number += 1
#    print (*playlistfile, sep = "\n")

readplaylistfromfile()
# search a movie from plex to the playlist.
def addmovie(title):
    results = plex.library.search(title=title, libtype="movie")
    if results:
        # Just use the first result, this could be smarter.
        items.append(results[0])
        print("Added %(title)s" % {'title': title})
    else:
        errors.append(title)
        print("Failed to add %(title)s" % {'title': title})


# search a TV show episode or range of episodes from plex to the playlist.
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
            
def searchmovie(title):
    results = plex.library.search(title=title, libtype="movie")
    if results:
        # Just use the first result, this could be smarter.
        searchitems.append(results[0])
        print("Found '%(title)s' on Plex." % {'title': title})
    else:
        searcherrors.append(title)
        print("Didn't found '%(title)s' on Plex" % {'title': title})
def searchtv(show, season, episode, end=False):
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
            searcherrors.append("%(show)s Season %(season)d Episode %(number)d" % values)
            print("Didn't found '%(show)s Season %(season)s Episode %(number)s' on Plex." % values)
        else:
            searchitems.append(item)
            print("Found '%(show)s Season %(season)s Episode %(number)s' on Plex." % values)
            
def user_prompt(question: str) -> bool:
    """ Prompt the yes/no-*question* to the user. """
    from distutils.util import strtobool
    while True:
        user_input = input(question + " [y/n]: ")
        try:
            return bool(strtobool(user_input))
        except ValueError:
            print("Please use y/n or yes/no.\n")

def addTrackToPlaylist(playlist, title):
    playlist = plex.playlist(playlist)
    track = plex.fetchItem(title)
    playlist.addItems(track)
    print(f"added {track} to playlist {playlist}")
    
def moveItemafter(playlist, title, after, countcurrent, countall):
    playlist = plex.playlist(playlist)
    track = plex.fetchItem(title)
    trackafter = plex.fetchItem(after)
    playlist.moveItem(track, trackafter)
    print(f"{countcurrent} / {countall} ordered {track} in playlist '{plex_playlist}' after {trackafter}")

def removeTrackfromPlaylist(playlist, title):
    playlist = plex.playlist(playlist)
    track = plex.fetchItem(title)
    playlist.removeItems(track)
    print(f"removed {track} from playlist {playlist}")

# Login
try:
    account = MyPlexAccount(plex_user, plex_pass)
    plex = account.resource(plex_server).connect()
    print ("\n")
    print("Logged in to %(server)s as %(user)s" % {'server': plex_server, 'user': plex_user})
except:
    print ("\n")
    print("Failed to login to %(server)s as %(user)s" % {'server': plex_server, 'user': plex_user})
    exit()

# Delete existing playlist
try:
    for playlist in plex.playlists():
      if playlist.title == plex_playlist:
        print ("Playlist exists called '" + playlist.title +"'")
        playlist_exists = "yes"
        break
except:
    print("No existing playlist called '%(playlist)s'" % {'playlist': plex_playlist})

#when the playlist exist, update it if needed

if playlist_exists == "yes":
  for playlist in plex.playlists():
    if playlist.title == plex_playlist:
      existingitems = playlist.items()
      break
  print ("Searching for Playlist - Items on Plex.")
  print ("Source: https://www.digitalspy.com/movies/a825774/marvel-cinematic-universe-in-chronological-order/")
  d = 0
  while d < len(playlistfile):
          splitplaylistfile = str(playlistfile[d]).split(";")
          d = d + 1
          if splitplaylistfile[0] == "movie":
            searchmovie( splitplaylistfile[1])
          else:
            if splitplaylistfile[0] == "show":
              splitplaylistfileshow = str(splitplaylistfile[1]).split(",")
              searchtv( splitplaylistfileshow[0], int(splitplaylistfileshow[1]), int(splitplaylistfileshow[2]), int(splitplaylistfileshow[3]))
            else:
              print ("This line doesn't contain a categorisation (movie/show) --> " + str(splitplaylistfile)) 
  print("Comparing Playlist-Items")
  unique = [i for i in searchitems if i not in existingitems]
  tomuchinplaylist = ""
  if(collections.Counter(searchitems)!=collections.Counter(existingitems)) and (len(unique)==0):
    unique = [i for i in existingitems if i not in searchitems]
    tomuchinplaylist = "yes"
  if (len(unique) > 0 ) and (tomuchinplaylist == ""):
    print ("The following items have been found in your libraries, but aren't in your playlist '" + plex_playlist +"':")
    print (*unique, sep = "\n")
    if user_prompt("Do you wan't to add and order them now (could take a few minutes)?"):
      i = 0
      while i < len(unique):
        splitunique = str(unique[i]).split(":")
        i = i + 1
        addTrackToPlaylist(plex_playlist, int(splitunique[1]))
      for playlist in plex.playlists():
        if playlist.title == plex_playlist:
          existingitems = playlist.items()
          break
      if existingitems == searchitems:
        print ("They are already in the right order.")
      else:
        j = 1
        k = 0
        while j < len(searchitems):
          splitsearchitems = str(searchitems[j]).split(":")
          k = j -1
          splitsearchitems_minus_one =  str(searchitems[k]).split(":")
          moveItemafter(plex_playlist, int(splitsearchitems[1]), int(splitsearchitems_minus_one[1]), j, len(searchitems))
          j = j +1
    else:
      print ("Then you can just add and order them manually to the playlist.")  
  
  elif (len(unique) > 0 ) and (tomuchinplaylist == "yes"):
    print ("The following items have been found in your playlist '" + plex_playlist +"', but aren't in our list:")
    print (*unique, sep = "\n")
    if user_prompt("Do you wan't to remove and order them now (could take a few minutes)?"):
      i = 0
      while i < len(unique):
        splitunique = str(unique[i]).split(":")
        i = i + 1
        removeTrackfromPlaylist(plex_playlist, int(splitunique[1]))
      print ("Order Playlist")
      if existingitems == searchitems:
        print ("They are already in the right order.")
      else:      
        j = 1
        k = 0
        while j < len(searchitems):
          splitsearchitems = str(searchitems[j]).split(":")
          k = j -1
          splitsearchitems_minus_one =  str(searchitems[k]).split(":")
          moveItemafter(plex_playlist, int(splitsearchitems[1]), int(splitsearchitems_minus_one[1]), j, len(searchitems))
          j = j +1
    else:
      print ("Then you can just add and order them manually to the playlist.")  
  
  else:
    print ("The Playlist is up to date.")
    if user_prompt("Do you wan't check the order right now? (could take a few minutes)"):
      print ("Order Playlist")
      if existingitems == searchitems:
        print ("They are already in the right order.")
        exit();
      else:
        exit();
        j = 1
        k = 0
        while j < len(searchitems):
          splitsearchitems = str(searchitems[j]).split(":")
          k = j -1
          splitsearchitems_minus_one =  str(searchitems[k]).split(":")
          moveItemafter(plex_playlist, int(splitsearchitems[1]), int(splitsearchitems_minus_one[1]), j, len(searchitems))
          j = j +1
    else:
      print("Thanks - Bye")

#### When the playlist doesn't exist, then create new

if playlist_exists == "":
  print("No existing playlist called '%(playlist)s'" % {'playlist': plex_playlist})
  print ("Add Playlist called '"+ plex_playlist)
  print ("Source: https://www.digitalspy.com/movies/a825774/marvel-cinematic-universe-in-chronological-order/")
  print("----------------------------------------------------")
# Create playlist
  d = 0
  while d < len(playlistfile):
          splitplaylistfile = str(playlistfile[d]).split(";")
          d = d + 1
          if splitplaylistfile[0] == "movie":
            searchmovie( splitplaylistfile[1])
          else:
            if splitplaylistfile[0] == "show":
              splitplaylistfileshow = str(splitplaylistfile[1]).split(",")
              searchtv( splitplaylistfileshow[0], int(splitplaylistfileshow[1]), int(splitplaylistfileshow[2]), int(splitplaylistfileshow[3]))
            else:
              print ("This line doesn't contain a categorisation (movie/show) --> " + str(splitplaylistfile))
  if len(searchitems) > 0:
    playlist = Playlist.create(plex, plex_playlist, items = searchitems)
  else:
    print("Script couldn't find any items to add to your MCU playlist")
    exit()
# Get playlist duration
hours = math.floor(playlist.duration / 1000 / 60 / 60)
time = "%(days)d days and %(hours)d hours" % { 'days': math.floor(hours / 24), 'hours': hours % 24}

if len(errors) > 0:
    print("The following files could not be found in your libraries to add to the playlist.")
    for item in errors:
        print("- %(item)s" % {'item': item})
    print("Run the script again once these items are in Plex.")
if len(searcherrors) > 0:
    print ("\n")
    print("The following files could not be found in your libraries to add to the playlist.")
    for item in searcherrors:
        print("- %(item)s" % {'item': item})
    print("Run the script again once these items are in Plex.")

print("----------------------------------------------------")
print("Enjoy %(time)s of the MCU!" % {'time': time})
print ("\n")

