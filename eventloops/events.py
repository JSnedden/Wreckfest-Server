# Customise the following attributes to your liking
# -------------------------------------------------
# Max number of laps in a race
MAX_LAPS = 8
# Average time a race should take (in seconds)
AVG_TIME = 360



import sys
import random
import csv

TRACK = dict[str,int,str]
TRACK_SET = list[TRACK]

def addTracks(type:str) -> TRACK_SET:
    filename = 'eventloops/maps_'+type+'.csv'
    fields = []
    tracks:TRACK_SET = []
    
    try:
        with open(filename) as file:

            reader = csv.reader(file, delimiter=',')

            fields = next(reader)

            for row in reader:
                track:TRACK = { 'id':row[0], 'lap':int(row[1]), 'gamemode':row[2] }
                tracks.append(track)
    except:
        print('# Error getting tracks in '+filename)
    
    return tracks

def setTracks(track_list:TRACK_SET) -> None:
    random.shuffle(track_list)
    for track in track_list:
        print('el_add='+track['id'])
        if track['lap'] != 0:
            print('el_laps='+str(min( round(AVG_TIME / track['lap']) , MAX_LAPS )))
        print('el_gamemode='+track['gamemode'])
        print('')

maps = sys.argv[1:]
tracks:TRACK_SET = []

for map in maps:
    tracks += addTracks(map)
print('')
setTracks(tracks)
