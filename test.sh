#! /bin/bash

#url=http://61.164.109.162:5458/dm01/ok-comic01/h/hzw/Vol_01/OnePiece_01_002.jpg
server="http://61.164.109.162:5458/dm01/ok-comic01/h/hzw/"
vol="Vol_01"
episode="01"
page1="00"
page2="0"
for (( i=1; i<100; i++ )) 
do
    if [ $i -lt 10 ]; then
	page=$page1$i
    else
	page=$page2$i
    fi
    url="$server$vol/OnePiece_"$episode"_"$page.jpg
    echo $url
    wget -c $url
done
