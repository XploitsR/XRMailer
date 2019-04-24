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
# Github: https://github.com/XploitsR/XRMailer                       #
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
CMDS=`type -P figlet &>/dev/null && echo 1 || echo 0`
xrsh="$path/xrmailer"
xrbn="$path/banner"
xrpy="$path/xrmailer.py"
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
if [ "$pyDir" -eq 0 ] && [ "$CMDS" -eq 0 ]
then	
echo "[!] Some Commands Are Missing!"
sleep 1
echo "[+] Installing...."
sleep 1

#Install needed files
apt-get install python3 python3-pyfiglet && clear
start=true

else
start=true
fi

sleep 2

#Rechecking 
if [ "$pyDir" -eq 0 ] && [ "$CMDS" -eq 0 ] && [ ! $start ]
then

sleep 1
echo "[!] Something went wrong!..."
sleep 1
echo "[!] Please Run The Setup Again..."
sleep 1

else

echo "[*] Installations Done!!!"

#verifying for necessary files
if [ ! -f "$xrsh" ] && [ ! -f "$xrpy" ] && [ ! -f "$xrbn" ] && [ ! -f "$xrtp" ] && [ ! -f "$xrhtml" ] && [ ! -f "$xrtxt" ] && [ ! -f "$xrem" ] && [ ! -f "$xrpng" ]
then

echo "[!] Some (files) are missing..."
echo "[!] Please re-clone XRMailer..."
sleep 1
exit 1

else

chmod 755 $xrsh
chmod 755 $xrpy
chmod 755 $xrbn
sleep 1

#Checking for directories
if [ ! -d "Emails" ] && [ ! -d "Files" ] && [ ! -d "Templates" ]
then 

sleep 1

#Create Needed Directories
mkdir Emails
mkdir Files
mkdir Templates
mkdir .xrlog
touch xrlog
echo "Setup Done" > xrlog

# (mv) files to needed directories
mv templates.py Templates/
mv sample.html Templates/
mv sample.txt Templates/
mv sample.csv Emails/
mv sample.png Files/
mv xrlog .xrlog/

proceed=true

fi

if [ "$proceed" ]
then

sleep 1
echo "[*] Setup Done (^_^) ";
echo "[*] Type ./xrmailer to get started (^_^) ";
echo " "
sleep 1
fi
fi
fi

else
echo " "
echo "[*] Setup Already Done"
echo "[*] Type ./xrmailer to get started (^_^) ";
echo " "
fi
