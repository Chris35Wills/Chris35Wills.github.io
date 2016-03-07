---
---

# Setting up your machine

Before attending the DTP Python training course, there are a few preliminary steps that you must first take. These will result in:

* local installation of a bash prompt terminal
* local Python installation (using the Anaconda distribution)
* initiation of a Github user account
* installation of an appropriate text editor 

## Program installation

---

### Bash shell

#### Windows

Download the Git for Windows [installer](https://git-for-windows.github.io/). Run the installer. 

**Important:** on the 6th page of the installation wizard (the page titled `Configuring the terminal emulator...`) select `Use Windows' default console window`. 

If you forget to do this, programs that you need for the workshops on this site will not work properly. If this happens rerun the installer and select the appropriate option.

This will provide you with both Git and Bash in the Git Bash program.

#### Mac OS X

The default shell in all versions of Mac OS X is bash, so no need to install anything. You access bash from the Terminal (found in /Applications/Utilities). You may want to keep Terminal in your dock for this workshop.

#### Linux

The default shell is usually Bash, but if your machine is set up differently you can run it by opening a terminal and typing bash. There is no need to install anything.

### Git

Git is a version control system that lets you track who made changes to what when and has options for easily updating a shared or public version of your code on [github.com](https://github.com/). You will need a [supported web browser](https://help.github.com/articles/supported-browsers/) (current versions of Chrome, Firefox or Safari, or Internet Explorer version 9 or above).

#### Windows

Git should be installed on your computer as part of your Bash install (described above).

#### Mac OS X

For OS X 10.9 and higher, install Git for Mac by downloading and running the most recent "mavericks" installer from [this list](http://sourceforge.net/projects/git-osx-installer/files/). After installing Git, there will not be anything in your /Applications folder, as Git is a command line program. **For older versions of OS X (10.5-10.8)** use the most recent available installer labelled "snow-leopard" [available here](http://sourceforge.net/projects/git-osx-installer/files/).

#### Linux

If Git is not already available on your machine you can try to install it via your distro's package manager. For Debian/Ubuntu run sudo apt-get install git and for Fedora run sudo yum install git.

---

### Text editor

When you're writing code, it's nice to have a text editor that is optimized for writing code, with features like automatic color-coding of key words. The default text editor on Mac OS X and Linux is usually set to Vim, which is not famous for being intuitive. if you accidentally find yourself stuck in it, try typing the escape key, followed by :q! (colon, lower-case 'q', exclamation mark), then hitting Return to return to the shell.

#### Windows

*notepad* is your go to editor and is accessed by simply typying ```notepad``` in your terminal - to keep things simple, you can just use this. 

Syntax highlighting (which can make coding a bit easier on the eye) can be achieved by using [*Notepad++*](http://notepad-plus-plus.org/) or [*Sublime Text*](http://www.sublimetext.com/). Be aware that you must add its installation directory to your system path. **Please ask your instructor to help you do this.**

*nano* is a basic editor that can also be used. This can be installed by following the instructions detailed [here](http://gosukiwi-blog.tumblr.com/post/44781816410/using-nano-from-git-on-windows) - **if you have any trouble with this, please just ask one of the instructors on the course**.

#### Mac OS X

If you already have an editor you like to use to work on text files, then please use that for the course. Others editors that you can use are [*Text Wrangler*](http://www.barebones.com/products/textwrangler/) or [*Sublime Text*](http://www.sublimetext.com/).

*nano* is another basic editor that can be used. It should be pre-installed.

#### Linux

If you already have an editor you like to use to edit text files, then please use that for the course - your choice between Emacs and Vim is a decision for you alone!

Others editors that you can use are [Gedit](https://wiki.gnome.org/Apps/Gedit), [Kate](http://kate-editor.org/) or [Sublime Text](http://www.sublimetext.com/).

*nano* is a basic editor that you can also use. It should be pre-installed.

---

### Python

[Python](http://python.org/) is a popular language for scientific computing, and great for general-purpose programming as well. Installing all of its scientific packages individually can be a bit difficult, so we will be using [Anaconda](https://store.continuum.io/cshop/anaconda/), an all-in-one installer.

Python version 3.X is the most up to date version of python to date, however many people are still working with v2.7. We promote the installation of v3.X on this course - older versions  will work but may result in you hitting some errors, especially when you get used to the language and start using different packages.

#### Windows

If you already have python, take a look [here](../already_have_python). If not, then follow the instructions below:

1. Open [http://continuum.io/downloads](http://continuum.io/downloads) with your web browser.
2. Click on **Python 3.X** link.
3. Download this Python 3 installer.
4. Install Python 3 using all of the defaults for installation except make sure to check **Register Anaconda as my default Python 3.x**.

#### Mac OS X

If you already have python, take a look [here](../already_have_python). If not, then follow the instructions below:

1. Open [http://continuum.io/downloads](http://continuum.io/downloads) with your web browser.
2. Click on **Python 3.X** link.
3. Download this Python 3 installer.
4. Install Python 3 using all of the defaults for installation.

#### Linux

If you already have python, take a look [here](../already_have_python). If not, then follow the instructions below:

1. Open [http://continuum.io/downloads](http://continuum.io/downloads) with your web browser.
2. Click on the **Python 3.X** link.
3. Download this Python 3 installer, save it in your home folder.
4. Install Python 3 using all of the defaults for installation. (Installation requires using the shell. If you aren't comfortable doing the installation yourself stop here and request help at the workshop.)
5. Open a terminal window.
6. Type `bash Anaconda-` and then press tab. The name of the file you just downloaded should appear.
7. Press enter. You will follow the text-only prompts. When there is a colon at the bottom of the screen press the down arrow to move down through the text. Type `yes` and press enter to approve the license. Press enter to approve the default location for the files. Type `yes` and press enter to prepend Anaconda to your `PATH` (this makes the Anaconda distribution the default Python).

---

### Now, test everything works!

Once you are done installing the software listed above, please go to [this page](../../Setup_check/setup_check), which has instructions on how to test that everything has been installed correctly.

---

## Additional things to set up

### Get a github account

Register [here](https://github.com/) and don't forget your password. Your account will be vital to the course on version control.

## Help

### Getting started with the terminal

If you are new to using the terminal, please have a run through [this excellent crash course](http://learnpythonthehardway.org/book/appendixa.html) to get familiar with things - this if from the [Learn Python The Hard Way](http://learnpythonthehardway.org/) site which is also worth a look through.

### Getting out of a terminal...

If you are new to the terminal, you may occasionally ask yourself where you have ended up and in some cases, how to leave a certain location. [This page](http://hpcarcher.github.io/2015-04-16-imperial/novice/ref/05-prompts-exits.html) offers some useful tips and advice - **please have a look through this before attending the course**.

