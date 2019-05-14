#!/bin/bash

######################################################################
# Copyright (c). All rights reserved                                 #
# GNU GENERAL PUBLIC LICENSE                                         #
# Version 3, 29 June 2007                                            #
#                                                                    #
# Coded by Solomon Narh (::XploitsR Author::)                        #
# Github: https://github.com/XploitsR/XRMailer                       #
# Facebook: https://facebook.com/RXploits                            #
# Twitter: https://twitter.com/RXploits                              #
# Telegram: https://t.me/RXploits                                    #
# Website: https://xploitsr.tk                                       #
#                                                                    #
#             ::PERSONAL ME::                                        #
# Github: https://github.com/XploitsR/Solomon97062                   #
# Facebook: https://facebook.com/solomon.narh.311                    #
# Twitter: https://twitter.com/solomon97062                          #
# Instagram: @_xploitsr_author_1                                     #
# Email: solomonnarh97062@gmail.com                                  #
######################################################################

path=`pwd`
xrlog="$path/.xrlog/xrlog"
if [ ! -f "$xrlog" ]
then
path=`pwd`
pyDir=`type -P python3 &>/dev/null && echo 1 || echo 0`
pyfig=`type -P figlet &>/dev/null && echo 1 || echo 0`
xtm=`type -P xterm &>/dev/null && echo 1 || echo 0`
xrsh="$path/xrmailer"
xrbn="$path/banner"
xrpy="$path/xrmailer.py"
xrsmtp="$path/xrsmtp.py"
xrtp="$path/templates.py"
xrhtml="$path/sample.html"
xrtxt="$path/sample.txt"
xrem="$path/sample.csv"
xrpng="$path/sample.png"
start=" "
sleep 2
echo " "
echo "[*] Setting Up...Please Wait! "
sleep 5
#verify commands exist
if [ "$pyDir" -eq 0 ] || [ "$pyfig" -eq 0 ] || [ "$xtm" -eq 0 ]
then	
echo "[!] Some Commands Are Missing!"
sleep 1
echo "[+] Installing...."
sleep 1
#Install needed files
sudo apt-get update && apt-get install xterm -y && clear
if [ "$xtm" -eq 1 ]; then
xterm -T "* Installing python3 and python3-pyfiglet *" -geometry 100x30 -e "sudo apt-get install python3 python3-pyfiglet"
start=true
fi
else
start=true
fi
sleep 2
#Rechecking 
if [ "$pyDir" -eq 0 ] || [ "$pyfig" -eq 0 ] || [ "$xtm" -eq 0 ] || [ ! $start ]
then
sleep 1
echo "[!] Something went wrong!..."
sleep 1
echo "[!] Please Run The Setup Again..."
sleep 1
exit 1
else
echo "[*] Installations Done!!!"
#verifying for necessary files
if [ ! -f "$xrsh" ] && [ ! -f "$xrpy" ] && [ ! -f "$xrsmtp" ] && [ ! -f "$xrbn" ] && [ ! -f "$xrtp" ] && [ ! -f "$xrhtml" ] && [ ! -f "$xrtxt" ] && [ ! -f "$xrem" ] && [ ! -f "$xrpng" ]
then
echo "[!] Some (files) are missing..."
echo "[!] Please re-clone XRMailer..."
sleep 1
exit 1
else
chmod +x $xrsh >/dev/null 2>&1
chmod +x $xrpy >/dev/null 2>&1
chmod +x $xrbn >/dev/null 2>&1
sleep 1
#Checking for directories
if [ ! -d "emails" ] && [ ! -d "files" ] && [ ! -d "templates" ]
then 
sleep 1
#Create Needed Directories
mkdir emails >/dev/null 2>&1
mkdir files >/dev/null 2>&1
mkdir templates >/dev/null 2>&1
mkdir modules >/dev/null 2>&1
mkdir .xrlog >/dev/null 2>&1
touch xrlog >/dev/null 2>&1
echo "Setup Done" > xrlog
# (mv) files to needed directories
mv templates.py templates/ >/dev/null 2>&1
mv sample.html templates/ >/dev/null 2>&1
mv sample.txt templates/ >/dev/null 2>&1
mv sample.csv emails/ >/dev/null 2>&1
mv sample.png files/ >/dev/null 2>&1
mv xrsmtp.py modules/ >/dev/null 2>&1
mv xrlog .xrlog/ >/dev/null 2>&1
proceed=true
fi
if [ "$proceed" ]
then
sleep 1
echo "[*] Setup Done (^_^) ";
echo "[*] Type ./xrmailer to get started (^_^) "
echo " "
sleep 1
exit 1
fi
fi
fi
else
echo " "
echo "[*] Setup Already Done"
echo "[*] Type ./xrmailer to get started (^_^) "
echo " "
exit 1
fi
