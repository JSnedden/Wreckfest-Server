# Customise the following attributes to your liking
# -------------------------------------------------
# Max number of laps in a race
MAX_LAPS = 8
# Average time a race should take (in seconds)
AVG_TIME = 360



import random
import csv

TRACK = dict[str,int,str]
TRACK_SET = list[TRACK]

def addTracks(type:str) -> TRACK_SET:
    filename = 'maps_'+type
    fields = []
    tracks = []
    
    with open(filename, 'r') as maps:

        reader = csv.reader(maps)

        fields = next(reader)

        for row in reader:
            track = { 'id':row[0], 'lap':row[1], 'gamemode':row[2] }
            tracks.append(track)
    
    return tracks

def setTracks(tracks:list) -> None:
    random.shuffle(tracks)
    for track in tracks:
        print('el_add='+track['id'])
        if track['lap'] != 0:
            print('el_laps='+min( round(AVG_TIME / track['lap']) , MAX_LAPS ))
        print('el_gamemode='+track['gamemode'])
        print('')