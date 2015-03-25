#!/usr/bin/python

import eyeD3
import os
import sys
import getopt

#### Function to generate the name of the mp3 as per the name Format
def generateMp3Name(trackArtist, trackTitle, trackAlbum, nameFormat, duplicateNo):
  newFileName = ""
  newFileFullName = ""

  # check the right format and generate the file name  
  if(nameFormat == "aTA"):
    newFileName = trackAlbum + "-" + trackTitle + "-" + trackArtist
  elif(nameFormat == "aAT"):
    newFileName = trackAlbum + "-" + trackArtist + "-" + trackTitle
  elif(nameFormat == "ATa"):
    newFileName = trackArtist + "-" + trackTitle + "-" + trackAlbum
  elif(nameFormat == "AaT"):
    newFileName = trackArtist + "-" + trackAlbum + "-" + trackTitle
  elif(nameFormat == "TaA"):
    newFileName = trackTitle + "-" + trackAlbum + "-" + trackArtist
  elif(nameFormat == "TAa"):
    newFileName = trackTitle + "-" + trackArtist + "-" + trackAlbum
  elif(nameFormat == "TA"):
    newFileName = trackTitle + "-" + trackArtist
  elif(nameFormat == "AT"):
    newFileName = trackArtist + "-" + trackTitle
  elif(nameFormat == "Aa"):
    newFileName = trackArtist + "-" + trackAlbum
  elif(nameFormat == "aA"):
    newFileName = trackAlbum + "-" + trackArtist
  elif(nameFormat == "Ta"):
    newFileName = trackTitle + "-" + trackAlbum
  elif(nameFormat == "aT"):
    newFileName = trackAlbum + "-" + trackTitle
  else:
    print "Invalid Name Format is detected !"
    print_help()
    sys.exit(2)

  # check if duplicate No need to be associated 
  if(duplicateNo == 0):
    newFileFullName = newFileName + ".mp3"
  else :
    newFileFullName = newFileName + "_" + str(duplicateNo) + ".mp3"

  return newFileFullName


#### Function to rip the mp3
def ripTheMp3(inputPath, outputPath, allowDuplicate, nameFormat, allowRecursive):
  count = 0
  directory = inputPath
  outDirectory = ""
  # Lets have a Walk in subdirectory of Current dir
  for root, dirs, files in os.walk(directory):
    print "Drilling directory: " + directory
    fileExist = False
    if outputPath == "":
      outDirectory = root
    else:
      outDirectory = outputPath
    for fileFullName in files:
      fileName, fileExtension = os.path.splitext(fileFullName)
      # Check if its a directory came here to trouble us
      if fileExtension == "":
        print "Ignoring Invalid File, No extension: " + fileFullName
        continue;
      # check if the file type is Mp3
      if(fileExtension == ".mp3"):
        # create a new instance of Tag
        tag = eyeD3.Tag()
        # Create a proper path for the file (to find the proper location of the file path)
        old_file_path = root + "/" + fileFullName
        # Link the mp3 file in the current directory for tag
        tag.link(old_file_path)
        # get Artist
        trackArtist = tag.getArtist()
        # get Title
        trackTitle = tag.getTitle()
        # get Album
        trackAlbum = tag.getAlbum()
        # generate file Name
        newFileFullName = generateMp3Name(trackArtist, trackTitle, trackAlbum, nameFormat, 0)
        # check if file generated name is the same as file name
        if(fileFullName == newFileFullName):
          print "Bingo ! File Generated name is same as filename for : " + fileFullName
          continue
        # check if file already exist in the outDirectory
        new_file_path = outDirectory + "/" + newFileFullName
        # check if file already exist
        isDuplicate = os.path.isfile(new_file_path)
        if (isDuplicate and allowDuplicate == False):
          print "Duplicate in not allowed, leaving file : " + new_file_path
          continue
        # duplicate count for generating the duplicate name
        duplicateNo = 1
        while(isDuplicate):
          print "File already exist, Duplicate File :" + newFileFullName
          # Try to assign new name with Duplicate No
          newFileFullName = generateMp3Name(trackArtist, trackTitle, trackAlbum, nameFormat, duplicateNo)
          # check if File name is same as generated duplicate name   
          if(newFileFullName == fileFullName):
            print "Bingo !! File Generated name is same as filename for : " + fileFullName
            fileExist = True
            break
          # Generate the new file path as per the current working directory
          new_file_path = outDirectory + "/" + newFileFullName
          # check if still duplicate
          isDuplicate = os.path.isfile(new_file_path)
          # increase the duplicate generate no
          duplicateNo = duplicateNo + 1
        # check if file exist flag is set
        if fileExist:
          continue
        # increment the song count (just for feeling good :D)
        count = count + 1
        print str(count) + "> Renaming File : " + fileFullName + " to : " + newFileFullName
        # generate the file path on file folder for rename
        new_file_path = outDirectory + "/" + newFileFullName
        # rename the file
        os.rename(old_file_path, new_file_path)
      # END of mp3 check

    # END of For Each File loop 

    # check if recursive is enabled
    if (allowRecursive == False):
      break 
  # END of For Each directory loop

  print "All mp3 files has checked successfully"


#### Function to print help, it all here :D
def print_help():
  print ""
  print "iRat.py Help: (iRat.py -h):"
  print ""
  print "iRat.py -I <input_folder> -O <output_folder> -N <name_format>"
  print ""
  print "-I < > : Input folder to check mp3's from. If not Specified takes current path."
  print "-O < > : Output folder to place converted mp3's. If not Specified use original path."
  print "-F < > : Name Format. Name format should be within pre-defined formats."
  print "         a : Album name"
  print "         A : Artist name"
  print "         T : Title name"
  print "         Formats: aAT, AaT, ATa, TAa, aTA, TaA, TA, AT, aA, Aa, Ta, aT. Default is : TA"
  print ""
  print "-h     : Help"
  print "-d     : Allow Duplicate. It allows the duplicate file with same name album and artist"
  print "         same named file will generate as: yellow.mp3, yellow_1.mp3 .."
  print "-r     : Allow recursive search. Search recursively from the input folder"
  print ""


#### Starting Point, It all begins here :O
# try to get opts
try:
  opts, args  = getopt.getopt(sys.argv[1:],"I:O:F:dhr", ["input=", "output=", "format=", "help"])
# If invalid options
except getopt.GetoptError:
  print "Invalid Input !"
  print_help() 
  sys.exit(2)

# Options values with default
inputPath = "."   # Default Input location is current folder
outputPath = ""   # Default location is the original
nameFormat = "TA" # Default Name Format Title-Artist
needHelp = False  
allowDuplicate = False
allowRecursive = False

# Get all options
for opt, arg in opts:
  if opt in ("-I", "--input"):
    inputPath = arg
  elif opt in ("-O", "--output"):
    outputPath = arg
  elif opt in ("-F", "--format"):
    nameFormat = arg
  elif opt in ("-d"):
    allowDuplicate = True
  elif opt in ("-h", "--help"):
    needHelp = True
  elif opt in ("-r"):
    allowRecursive = True
  else:
    print "Invalid Input : " + str(opt)
    print_help()
    sys.exit(2)

# Check if user need help first
if (needHelp == True):
  print_help()
  sys.exit(0)

# Rip the mp3s as per the config
ripTheMp3(inputPath, outputPath, allowDuplicate, nameFormat, allowRecursive)
