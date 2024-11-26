cd ~/git/pub-aph
source venv/bin/activate
clear

clear; echorun aphrodite run /home/ubuntu/hff/8b-base --enforce-eager --uvloop -tp 2 -pp 1

clear; python LUKE/querytest.py
