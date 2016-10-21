---
layout: page
title: Windows command line
permalink: /windows_command/
---

I populate this as I come across things I find useful - I work with Powershell (just type in powershell in the windows start menu and it'll pop up). A good place to visit for a proper "how to course" for working with the command line can be found [here](http://learnpythonthehardway.org/book/appendixa.html).

##Make new files/directories:

`New-Item c:\scripts\Windows PowerShell -type directory`

`New-Item c:\scripts\new_file.txt -type file`

If the item you are trying to create already exists you’ll get back an error message similar to this:

`New-Item : The file 'C:\scripts\new_file.txt' already exists.`

However, you can override the default behavior by including the -force parameter:

`New-Item c:\scripts\new_file.txt -type file -force`

`New-Item c:\scripts\new_file.txt -type file -force -value "This is text added to the file"`

##Remove file/folder:

`rm folder (will call up options if files are within)`

`rm file`

##Directory management:

See all files in all folders and subfolders in dir:

`Get-ChildItem -Path .\ -recurse `

See all folders and subfolders in dir:

`Get-ChildItem -Path .\ -recurse | where psiscontainer`

See all folders in dir:

`Get-ChildItem -Path .\ -Directory`

Search for file in dir recursively:

`ls *.sh -recurse`