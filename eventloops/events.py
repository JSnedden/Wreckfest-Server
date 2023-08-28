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
        print('# Retrieved maps from '+filename)
    except:
        print('# Error getting tracks in '+filename)
    
    return tracks

def setTracks(track_list:TRACK_SET) -> None:
    random.shuffle(track_list)
    file = open('active_config.cfg', 'a')

    for track in track_list:
        file.write('el_add='+track['id']+'\n')
        if track['lap'] != 0:
            file.write('el_laps='+str(min( round(AVG_TIME / track['lap']) , MAX_LAPS ))+'\n')
        file.write('el_gamemode='+track['gamemode']+'\n')
        file.write('\n')
    
    file.close()

maps = sys.argv[1:]
tracks:TRACK_SET = []

for map in maps:
    tracks += addTracks(map)

setTracks(tracks)
