---
layout: post
title: Modify the appearance of your putty terminal
categories: putty, windows
---

[Putty](http://www.putty.org/) is an open source SSH client for windows. Various tutorials on how to make use of it exist (e.g. see [here](http://internal.math.arizona.edu/services/computing/remote-access/shell/putty)). On opening putty, you have a variety of options which you can make use of, including the appearance of the resultant terminal that opens for a given SSH connection. Colours can be important, affecting things from how well you can see your screen (!) to how well or how long you can manage to concentrate.

You can alter the various colour settings yourself, but as you might guess, this is a well trodden path and there exists a variety of information on useful colour combinations. One colour set-up I find particularly pleasant to work with is [Zenburn](http://kippura.org/zenburnpage/), which was put together for [Vim](http://www.vim.org/). Assuming that you have saved some putty sessions (i.e. for connections you frequently have to make - [see here](http://kb.site5.com/shell-access-ssh/putty/putty-how-to-load-save-or-delete-server-connection-settings/)), you can implement custom colour settings by adapting the putty registry file (.reg). 

So what is a registry file, how to find it and how to adapt it? The putty registry file saves all of the information of your saved putty sessions etc. - by getting a hold of this file, you can transfer it between your windows machines, in turn transferring your putty session settings. Assuming you have administrative rights on your machine, to find this file (also see [here](http://humairahmed.com/blog/?p=3562)):

1. Open a command line terminal
2. Type `regedit` and press enter
3. Type `Ctrl + F` and type "SimonTatham"
4. Make sure only `Keys` is ticked and then select `Find Next`
5. On the left hand side (the directory tree) a folder called "SimonTatham" will appear
6. Right click this and save it somewhere - call it what you want (e.g. "putty_settings_at_work.reg")
7. You can now send and open this on other machines - just right click the file icon and click merge, and you will replicate the defined putty settings on your machine

To create a profile with modified colours (for which we'll use the settings as defined [here](http://looselytyped.blogspot.co.uk/2013/02/zenburn-pleasant-color-scheme-for-putty.html) and [here](https://gist.github.com/EdEichman/1e6b08a298bfb6758f65)): 

1. follow steps 1-6 as above
2. Open the .reg file in a text editor
3. Type the following:
	
		[HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\zenburn]
		"Colour0"="255,255,255"
		"Colour1"="255,255,255"
		"Colour2"="51,51,51"
		"Colour3"="85,85,85"
		"Colour4"="0,0,0"
		"Colour5"="0,255,0"
		"Colour6"="77,77,77"
		"Colour7"="85,85,85"
		"Colour8"="187,0,0"
		"Colour9"="255,85,85"
		"Colour10"="152,251,152"
		"Colour11"="85,255,85"
		"Colour12"="240,230,140"
		"Colour13"="255,255,85"
		"Colour14"="150,133,63"
		"Colour15"="135,206,235"
		"Colour16"="255,222,173"
		"Colour17"="255,85,255"
		"Colour18"="255,160,160"
		"Colour19"="255,215,0"
		"Colour20"="245,222,179"
		"Colour21"="255,255,255"
		"LineCodePage"="UTF-8"
		"Font"="Lucida Console"
		"FontHeight"=dword:0000000c

4. Save the file
5. Right click the icon and click `Merge`
6. Open putty - ion your saved sessions, you should now see `zenburn`
7. Load the session, input your host name (and save it to the session if you want)
8. Now click open and log in as usual and you will have a new colour scheme
9. If you want, you can now delete the .reg file you exported (but not the file in the registry!!) as this has been merged into the registry
