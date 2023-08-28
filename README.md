# Wreckfest Server - Event list randomiser
This project allows you (a wreckfest server host) to start a wreckfest server with any map types you choose and define race parameters.
I found out that Wreckfest servers (as of 24/08/2023) do not randomise the event loops, which means that they follow the same order when the voting starts. I was inconvenienced by this and realised that it would best be solved by a small script, so probably in python. I didn't find any public solutions that randomises a list of tracks and makes the average race length a given time of my choosing.

Some inspiration was taken from [TheLysdexicOne](https://github.com/TheLysdexicOne)'s [project](https://github.com/TheLysdexicOne/wreckfest-server) randomising the tracks though I have designed a simplified and somewhat modular approach. Modular being modded maps can be added, but at the expense of the host manually creating the `.csv` file to add it into rotation

## Requirements
To host a Wreckfest server, you need either:
* Wreckfest game installed, or
* Wreckfest Dedicated Server installed (via SteamCMD or otherwise)
The install location of your chosen version will be referenced as 'game installation folder'

To use this project's files and functionality, you need to have [Python](https://www.python.org/downloads/) installed.

This project runs on windows machines, linux machines should start servers by calling the script inside the batch (`.bat`) file.

## Setup / Install

1. [Download](https://github.com/JSnedden/Wreckfest-Server/archive/refs/heads/main.zip) the project repository `.zip`
2. Unzip to your game installation folder
3. Open `server_config.cfg` in whichever environment you wish and amend the server settings
4. If you wish to use any modded maps:
    * Ensure the mods are stored in the /mods folder and named in the server config
    * To add modded maps to your rotation, you should create your own `.csv` in the format `maps_<mod>.csv`
    * Use the required headers "map_id,lap_time,gamemode", "location" and "track" optional
    * "map_id" should correspond to the name of the `.evse` file in /<mod>/data/propert/event
    * "lap_time" should be the average lap time for your participants for that track rounded to nearest 5 seconds
        * Base game sample events were created using B class non-special vehicles
    * "gamemode" should refer to the gamemode type allowed for that map
        * Base game sample events only include racing and derby types
5. If you want to change the average length of the maximum number of laps or average race length, amend the values in `eventloops/events.py`
6. Open `server_gen.bat` and add the name (from `maps_<name>.csv`) following the python script call and before the double angle brackets
    * Example `.\eventloops\events.py racing >> active_config.cfg`
7. When happy with your options, double click `server_gen.bat` to start your server!