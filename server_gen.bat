@echo off

IF NOT EXIST steam_appid.txt (
    @echo 228380 > steam_appid.txt
)

copy server_config.cfg active_config.cfg

:: py .\eventloops\events.py ARG_1 ARG_2 ARG_3 ARG_4
:: ARG_1 MAX LAP COUNT
:: ARG_2 AVERAGE RACE LENGTH
:: ARG_3... track sets to include
py .\eventloops\events.py 8 360 racing

start /B Wreckfest_x64.exe -s server_config=active_config.cfg