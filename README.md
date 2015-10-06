# IRAT
 
iRat is python aplication to generate mp3 file as per the id3 tag values.  People like me often gets irritated by gambled mp3 name while it is copied from Iphone or Ipod. iRat is really usefull to change the gambled Mp3 name as required. 
 
iRat provides multiple nameing Format to name the mp3 file as you want it. So no more worries, iRat will do it for you. 

### Version:
1.0.0
 
### iRat Help:
 
#####Use: 

```
./iRat.py -I <'input_folder'> -O <'output_folder'> -N <'name_format'>
```

#####Option:
 
```
**-I < >** : Input folder to check mp3's from. If not Specified takes current path.
 
**-O < >** : Output folder to place converted mp3's. If not Specified use original path.
 
**-F < >** : Name Format. Name format should be within pre-defined formats.

         **a :** Album name
         
         **A :** Artist name
         
         **T :** Title name
         
         Formats: aAT, AaT, ATa, TAa, aTA, TaA, TA, AT, aA, Aa, Ta, aT. Default is : TA
         
 
**-h**     : Help
 
**-d**     : Allow Duplicate. It allows the duplicate file with same name album and artist
 
         same named file will generate as: yellow.mp3, yellow_1.mp3 ..
         
**-r**     : Allow recursive search. Search recursively from the input folder
``` 
### More Info:
This is an early release. I’ve been using it for a while and I like this one pretty well, but no guarantees
that it won’t change a bit.

