---
---

# Nano basics

## Installation

[Nano](http://www.nano-editor.org/) is used as the text editor throughout the courses on this site. If you are using Linux or OSX, it should be preinstalled - windows users can download it [here](http://www.nano-editor.org/download.php). To be able to access it from the command line by simply typing `nano`, you will have to insert the path to the nano.exe file (inside the folder you downloaded) to your `PATH`.

## Basic use

Nano is an excellent program for quick and simple text editing - however, if you are new to the command line, it may seem a bit alien. 

To open up a new file called *foo.txt*, simply type:

```
nano foo.txt

```

This will open up the nano editor. You can just type as normal now, moving up and down using the cursors or the enter key. 

NB/ You will see at the bottom of the editor a number of options e.g. *^X Exit*. The *^* symbol represents the Ctrl key.

Once you have typed in some text and are ready to leave nano, use the Ctrl + x keys. This will bring up an option at the bottom saying *Save modified buffer?*. Now press the Y key - you will now have an option of modifying what to call the saved output. Change or keep this and just press enter. To cancel and go back to editing the file, just press Ctrl + C.

## Some useful commands (by no means exhaustive!)

To get a full list of commands, press Ctrl + G (and then Ctrl + X to exit the menu). Anywhere you see a *^* that means Ctrl. 
You'll also see use of *M* - this is the META key. If you don't have a *META* key, this may be mapped to the Esc key. So for example, *Meta + S* will be Esc then S. Another example - *Meta + ^* might for you be Esc followed by Shift + 6 (where 6 has a function of ^). Stick with it - it makes sense eventually!

To *cut a line in a document*, move the cursor to the beginning of the line and press Ctrl + K. 

To copy a block of text, first move the cursor to the beginning of the section and type Ctrl + ^ (this may be Ctrl + shift + 6 for you). Now, move the cursor to the end of the section to copy - you'll see the text get highlighted. You can *cut* all of the highlighted text using Ctrl + K as before, but to *copy* it, set another mark, *META + ^* (see above about META keys - also look [here](https://en.wikipedia.org/wiki/GNU_nano)).

To *paste* (called *uncut* in nano) what you just cut, press Ctrl + U and the line will paste wherever the cursor is at that moment.

## More info

[Beginners Guide](http://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/)

[Useful commands](http://staffwww.fullcoll.edu/sedwards/Nano/UsefulNanoKeyCommands.html)

[Nano made easy](http://www.tuxradar.com/content/text-editing-nano-made-easy)