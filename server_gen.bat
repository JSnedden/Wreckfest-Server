@echo off

IF NOT EXIST steam_appid.txt (
    @echo 228380 >steam_appid.txt
)

server_config.cfg > active_config.cfg
.\eventloops\events.py >> active_config.cfg

start /B Wreckfest_x64.exe -s server_config=active_config.cfg