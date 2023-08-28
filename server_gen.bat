@echo off

IF NOT EXIST steam_appid.txt (
    @echo 228380 > steam_appid.txt
)

copy server_config.cfg active_config.cfg

py .\eventloops\events.py racing

start /B Wreckfest_x64.exe -s server_config=active_config.cfg