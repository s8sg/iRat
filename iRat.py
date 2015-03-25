#!/usr/bin/python

import eyeD3
import os

count = 0
directory = "."
# Lets have a Walk in subdirectory of Current dir
for root, dirs, files in os.walk(directory):
  print "Drilling directory: " + directory
  fileExist = False
  for fileFullName in files:
    fileName, fileExtension = os.path.splitext(fileFullName)
    # Check if its a directory came here to trouble us
    if fileExtension == "":
      print "Ignoring Invalid File, No extension: " + fileFullName
      continue;
    if(fileExtension == ".mp3"):
      tag = eyeD3.Tag()
      old_file_path = root + "/" + fileFullName
      tag.link(old_file_path)
      trackArtist = tag.getArtist()
      trackTitle = tag.getTitle()
      trackAlbum = tag.getAlbum()
      newFileFullName = trackTitle + "-" + trackArtist + ".mp3"
      # check if file generated name is the same as file name
      if(fileFullName == newFileFullName):
        print "Bingo !! File Generated name is same as filename for : " + fileFullName
        continue;
      # check if file already exist
      new_file_path = root + "/" + newFileFullName
      isDuplicate = os.path.isfile(new_file_path)
      duplicateNo = 1
      while(isDuplicate):
        print "File already exist, Duplicate File :" + newFileFullName
        # Try to assign new name with Duplicate No
        newFileFullName = trackTitle + "-" + trackArtist + "_" + str(duplicateNo) + ".mp3"
        if(newFileFullName == fileFullName):
          print "Bingo !! File Generated name is same as filename for : " + fileFullName
          fileExist = True
          break;
        new_file_path = root + "/" + newFileFullName
        isDuplicate = os.path.isfile(new_file_path)
        duplicateNo = duplicateNo + 1
      if fileExist:
        continue;
      count = count + 1
      print str(count) + "> Renaming File : " + fileFullName + " to : " + newFileFullName
      new_file_path = root + "/" + newFileFullName
      os.rename(old_file_path, new_file_path) 
