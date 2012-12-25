#! /usr/bin/python
import sys
import urllib
import os

def saveToFile(url, filename):
    if os.path.exists(filename):
        return 
    d_file = urllib.urlopen(url)
    output = open(filename, "wb")
    output.write(d_file.read())
    output.close()
    return


baseurl = "http://www.99comic.com"
serverurl = "http://61.164.109.162:5458/dm01"
f = open("url_level1", "r")
for line in f:
    line_str = str(line)
    website = baseurl + line_str[line_str.find("=")+1:line_str.find("target")-1]
    web = urllib.urlopen(website)
    picList = str()
    episode = str()
    for content in web:
        #find episode
        if (str(content).find("<title>") != -1):
            episode = str(content)[str(content).find("<title>")+7:str(content).rfind("-")-1]
            episode = episode.decode('gb2312') #handle Chinese characters
            #create direcotry for this episode
            if not os.path.exists("OnePiece/" + episode): os.makedirs("OnePiece/" + episode)
            
        #find picture list        
        pos = str(content).find("PicListUrls")
        if (pos != -1):
            picList = str(content)[pos+15:str(content).find(";")-1]
            picArray = picList.split('|')
            filename_prefix = 1
            for pic in picArray:
                download = serverurl + pic
                print "Downloading " + download
                filename = "OnePiece/" + episode + "/" + episode + " - " + str(filename_prefix) + ".jpg"
                filename_prefix = filename_prefix + 1
                print "Saving " + filename
                saveToFile(download, filename)
            break
            
    
    
