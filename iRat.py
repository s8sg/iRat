#!/usr/bin/python

import eyeD3
import os

count = 0
directory = "."
# Lets have a Walk in subdirectory of Current dir
for root, dirs, files in os.walk(directory):
  print "Drilling directory: " + directory
  for fileFullName in files:
    fileName, fileExtension = os.path.splitext(fileFullName)
    # Check if its a directory came here to trouble us
    if fileExtension == "":
      print "Ignoring Invalid File, No extension: " + fileFullName
      continue;
    if(fileExtension == ".mp3"):
      tag = eyeD3.Tag()
      tag.link(fileFullName)
      trackArtist = tag.getArtist()
      trackTitle = tag.getTitle()
      trackAlbum = tag.getAlbum()
      newFileFullName = trackTitle + "-" + trackArtist + ".mp3"
      # check if file generated name is the same as file name
      if(fileFullName == newFileFullName):
        print "Bingo !! File Generated name is same as filename for : " + fileFullName
        continue;
      # check if file already exist
      isDuplicate = os.path.isfile(newFileFullName)
      duplicateNo = 1
      while(isDuplicate):
        print "File already exist, Duplicate File :" + newFileFullName
        # Try to assign new name with Duplicate No
        duplicateNo = 1
        newFileFullName = trackTitle + "-" + trackArtist + "_" + str(duplicateNo) + ".mp3"
        isDuplicate = os.path.isfile(newFileFullName)
      count = count + 1
      print str(count) + "> Renaming File : " + fileFullName + " to : " + newFileFullName        
      os.rename(fileFullName, newFileFullName) 
