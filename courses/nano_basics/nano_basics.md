---
---

# Nano basics

## Installation

[Nano](http://www.nano-editor.org/) is used as the text editor throughout the courses on this site. If you are using Linux or OSX, it should be preinstalled - windows users can download it [here](http://www.nano-editor.org/download.php). To be able to access it from the command line by simply typing `nano`, you will have to insert the path to the nano.exe file (inside the folder you downloaded) to your `PATH`.

## Basic use

Nano is an excellent program for quick and simple text editing - however, if you are new to the command line, it may seem a bit alien. 
To open up a new file called *foo.txt*, simply type:

  nano foo.txt

This will open up the nano editor. You can just type as normal now, moving up and down using the cursors or the enter key. 

NB/ You will see at the bottom of the editor a number of options e.g. *^X Exit*. The *^* symbol represents the <kbd>Ctrl</kbd> key.

Once you have typed in some text and are ready to leave nano, use the <kbd>Ctrl</kbd> + <kbd>x</kbd> keys. This will bring up an option at the bottom saying *Save modified buffer?*. Now press the <kbd>Y</kbd> key - you will now have an option of modifying what to call the saved output. Change or keep this and just press <kbd>enter</kbd>. To cancel and go back to editing the file, just press <kbd>Ctrl</kbd> + <kbd>C</kbd>.

## Some useful commands (by no means exhaustive!)

**Full list of commands**: <kbd>Ctrl</kbd> + <kbd>G</kbd> (and then <kbd>Ctrl</kbd> + <kbd>X</kbd> to exit the menu). 

Anywhere you see a *^* before another letter, that means <kbd>Ctrl</kbd>. You'll also see use of *M* - this is the <kbd>META</kbd> key. If you don't have a *META* key, this may be mapped to the <kbd>Esc</kbd> key. So for example, *Meta + S* will be <kbd>Esc</kbd> then <kbd>S</kbd>. Another example - *Meta + ^* (note that ^ in this case does not preceed a letter so if used in its own right) might for you be <kbd>Esc</kbd> followed by <kbd>Shift</kbd> + <kbd>6</kbd> (where <kbd>6</kbd> has a function of <kbd>^</kbd>). Stick with it - it makes sense eventually!

**Cut a line in a document**: move the cursor to the beginning of the line and press <kbd>Ctrl</kbd> + <kbd>K</kbd>. 

**Copy a block of text**: move the cursor to the beginning of the section and type <kbd>Ctrl</kbd> + <kbd>^</kbd> (this may be <kbd>Ctrl</kbd> + <kbd>shift</kbd> + <kbd>6</kbd> for you). Now, move the cursor to the end of the section to copy - you'll see the text get highlighted. To *copy* it, set another mark using *META + ^* (see above about META keys - also look [here](https://en.wikipedia.org/wiki/GNU_nano)) - this may be <kbd>Esc</kbd> followed by <kbd>Shift</kbd> + <kbd>6</kbd> for you.

**Paste** (*uncut* in nano): press <kbd>Ctrl</kbd> + <kbd>U</kbd> and the line will paste wherever the cursor is at that moment.

## More info

[Beginners Guide](http://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/)

[Useful commands](http://staffwww.fullcoll.edu/sedwards/Nano/UsefulNanoKeyCommands.html)

[Nano made easy](http://www.tuxradar.com/content/text-editing-nano-made-easy)
