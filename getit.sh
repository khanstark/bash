#!/bin/bash

x=`youtube-dl --version|cut -d\. -f1,2`
y=`date +"%Y.%m"`
if [ $x=$y ]
then
    echo "version ok"
else
    echo "Update needed. Updating Now.."
    sudo youtube-dl -U
fi

echo "1. One Video"
echo "2. Playlist"
read num
if [ $num -eq 1 ]
then
    echo "enter youtube url"
    read url
    notify-send "Started Download"
    youtube-dl $url
else
    echo "enter playlist url"
    read url
    cnt=1
    curl -s "$url"|grep "/watch?"|cut -d\" -f2|grep "list"|cut -d\; -f1| while read video;do notify-send "Downloading Playlist Video#$cnt"; youtube-dl "http://www.youtube.com$video";((++cnt));done

fi

 
