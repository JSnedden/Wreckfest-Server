import sys
import random
import csv

TRACK = dict[str,str]
TRACK_SET = list[TRACK]

def addTracks(type:str) -> TRACK_SET:
    filename = 'eventloops/maps_'+type+'.csv'
    fields = [] # type: ignore
    tracks:TRACK_SET = []
    
    try:
        with open(filename) as file:

            reader = csv.reader(file, delimiter=',')

            fields = next(reader) # type: ignore

            for row in reader:
                track:TRACK = { 'id':row[0], 'lap':row[1], 'gamemode':row[2] }
                tracks.append(track)
        print('# Retrieved maps from '+filename)
    except:
        print('# Error getting tracks in '+filename)
    
    return tracks

def setTracks(track_list:TRACK_SET, avg_time:int, max_laps:int) -> None:
    random.shuffle(track_list)
    file = open('active_config.cfg', 'a')

    for track in track_list:
        file.write('el_add='+track['id']+'\n')
        if int(track['lap']) != 0:
            laps = max(round(avg_time / int(track['lap'])), 1)
            file.write('el_laps='+str(min(laps, max_laps))+'\n')
        file.write('el_gamemode='+track['gamemode']+'\n')
        file.write('\n')
    
    file.close()
    print('# Finished writing tracks to file')

laps_max:int = int(sys.argv[1])
time_avg:int = int(sys.argv[2])
maps:list[str] = sys.argv[3:]
tracks:TRACK_SET = []

if len(maps) == 0:
    print('# No maps were retrieved...')
for map in maps:
    tracks += addTracks(map)

setTracks(tracks, time_avg, laps_max)
