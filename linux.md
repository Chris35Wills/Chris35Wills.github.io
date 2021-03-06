---
layout: page
title: Linux terminal
permalink: /linuxbits/
---

Notes I made from reading and searching when I got started with linux. A good place to visit for a proper "how to course" in terminal can be found [here](http://learnpythonthehardway.org/book/appendixa.html).

##General

Access to bashrc:

`nedit ~/.bashrc`  

- this is where the bash prompt is defined and it also holds path details

Use alias as defined in ~/.bashrc:

`source ~/.bashrc`

`alias_name`
		
Ctrl + v then Ctrl + i creates a tab character equivalent

Say you run a programme from a given console and you want to run something else
at the same time - you can do the following in order:

Ctrl + z			

- Pauses what is running

`bg`				

- Starts the process again but puts it in the background

...you can now use the command line again to start something else (which can
also be put in the background

`jobs`				

- To see what is running

`fg 1`				

- To bring job one back to the foreground

Ctrl + c			

- Closes the foreground task

`csh name_of_script.csh`		

- Runs a c shell script

`nedit name_of_script.csh`		

- Opens a specified file using a given programme (int this case, nedit)

`top`							

- Shows you what is running (can be sorted by processes and memory usage using capitals P and M respectively)			

`history 10`					

- Echo the last 10 commands 

`man gawk`						

- Access a manual (of gawk in this example) - to move through the manual use "n", quit using a "q" and search for a word or character

`ls`							

- List files in a directory

`ls -l`							

- List files in a directory + directories

NB/ If you have a directory problem e.g. " /tmp/temp_coords: Permission denied. " just type:

`ls -h /tmp/temp_coords`

... and this will give you details with regard to permissions of the file (maybe you can't 
access it because you don;t have the permission!) 

`ls -lh`	

- List files in a directory + directories + size (in a readable format)

`ls -la`						

- List files in a directory + hidden files

`rm -rf <filename>`	

- Delete specified file

`rm -Ri <folderpath>`			

- Delete folder at specified path

`ls rm -f $dataset/h*`` 		

- lists what is to be removed without removing it

`ls rm -f  $dataset/m*` 		

- lists what is to be removed without removing it

`rm -f $dataset/h*`				

- remove all files in directory $database that begin with "h"

`rm -f  $dataset/m*` 			

- remove all files in directory $database that begin with "m"

`cp -c blah1/ blah2/blah3`				

- copy blah1 to within blah3 - use flags (e.g. -c) when dealing with folders

`rsync -av /source/data/ target/`		

- a better way to copy (everything) - have a look at the flags (-av is copy everything and verbose)

'...'		

- Quotes eactly what is written betwen the '..'

"..."		

- Quotes what is written betwen the ".." but if variables, these will still be used as such
							
`df -h`			

- States how much memory is in use (total system usage)

`du -sk name`		

- Size of file/folder

`ps`

- Gives a list of processes and associated IDs

`pgrep firefox`				

- Gets the process ID of firefox (you could type any programme)

`kill 22349`				

- Kills process of number 22349

`ps aux | grep firefox`		

- Gets the process ID of firefox (you could type any programme) that is being run on any login that you may have (main or one of your tightVNC connections). This is worth using if firefox tells you it is aleady open and needs closing)

`cut -c5-10 file.txt`	

- cuts the 5th-10th characters from a text file and prints to stdout

`cut -d"	" -f3  file.txt`	

- provides the 3rd field as designated following a tab delimiter see [here](www.thegeekstuff.com/2013/06/cut-command-examples/) for more.

`mkdir foobar`				

- Makes new direcory 'foobar'

`mv nz* foobar`				

- Moves all files in a directory with prefix of nz (regardless of what follows) to the directory of foobar
- Make sure you are in the directory of the *nz files!
							
`man chmod`					

- Manual for the chmod tool used for setting PERMISSIONS (read/write/execute)

`chmod -w` 					

- Set current directory as writable

`chmod -w test_folder`		

- Set "test_folder" as writable
							
`echo grd2xyz variable variable variable` 	

- Rather than run the command grd2xyz, prefixing echo will print out exactly what is being passed into it

`pwd`							

- Gives you the current directory path	

`which programmeName`			

- Gives you the path directoy

`ls *d *.geo > list_geo`

- Create list of all things with suffix .geo

`ls *d *.dem_par > list_dem_par`

- Create list of all things with suffix .dem_par

`paste list_geo list_dem_par > list_multi_mosaic`		

- Combine lists ino 1 list called list_multi_mosaic

`man -k pdf`				

- Find programmes that deal with pdf files 

`xdg-open foo.pdf`			

- Display pdf (better than evince)

`evince file2open.pdf`		

- Allows pdf file reading from terminal

`display file2open.png`		

- Uses ImageMagick to view a png file		

`man -k grd`				

- Finds any programme with "grd" in the title (useful for finding newe tools etc...) <- doesn't find everything though (only those with "manuals" -- i.e. can't use for finding gamma tools for example)"

Search for file (name):

`find . -name \*png`			

- Find files | in this directory (the ".") | with anything preceding "png" (wildcard * can be used but must be escaped with "\") 

`find -name "query"`			

- Find files in your current directroy of "name" - case sensitive

`find -iname "query"`			

- Find files in your current directroy of "name" - not case sensitive

Search for file (containing string):

`grep -rnw 'directory' -e "pattern"`	

e.g. `grep -rnw ./ -e "about"`		Find files in current dir containing string 'about' 

See also [here](http://stackoverflow.com/questions/16956810/finding-all-files-containing-a-text-string-on-linux)  for more info on string searching in files and [here](http://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/) for more info on file and folder searching.

##When in a network

Logging into other machines from the Konsole:

`ssh nameofcomputer`		

- Will get you access to a computer in the network 
- Say yes to security question and then enter your password