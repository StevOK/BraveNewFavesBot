# BraveNewFavesBot
A chat bot designed to accompany the Brave New Faves pirate radio show at twitch.tv/kathleen_lrr.

This bot is designed to look for YouTube links in Twitch chat, put those messages in a list,
then create a text file with that list of posts.
New features added recently also let the user keep track of which songs are played on stream and
prints the full playlist to a text file.

# Initial Setup

To use this bot, you need to have the latest version of Anaconda for Python 3.7 installed.
Download here: https://www.anaconda.com/download/

Once you have this installed, you will also need to install irc, which is what you need to interact
with Twitch. 
Open Anaconda Prompt from the Anaconda3 folder in the Start Menu, then type the following command:
	apt-get install irc
	
# Setup for Starting the Bot

Open Anaconda Promt from the Anaconda3 folder in the Start Menu.

Change your current directory to the folder where these code files are located. If you put this folder
in your default directory, all you will need to do is type the following command:
	cd BraveNewFavesBot
	
To start the bot so that it can look for music recommendations, type the following command:
	python Run.py 
	
BraveNewFavesBot will post a message in your chat saying that it has connected successfully.	
From this point on, chat messages with YouTube links in them will be put into a list! Those messages
will be echoed in the bot's chat window, at twitch.tv/BraveNewFavesBot, for easy live reading.

# To Print the List of Messages to a File

Go to your chat and type the following command:
	!printlist
	
This creates a .txt file with all of the collected messages, including the usernames who made the suggestions, 
in the same folder as this file. The file name will be time-stamped so that this won't write over previous lists
created when running this program.

# New Features Added!

Starting with run2.py, there are is a new feature allowing you to keep track of which requests were played on stream!

# To Add a Song to the Now Playing List

Each viewer request is now marked with a number to easily tell when the song was requested. When you choose a song
to play, look at the request number before the username and description. Go to your chat and type the following
command:
	!nowplaying X
	
Where X is the request's number. The chat bot will print the request message into your chat for the benefit of 
your audience. This will also add the song to the night's playlist.

# To Print the Playlist of Requests Played

Go to your chat and type the following command:
	!printplaylist
	
This creates a .txt file with all of the songs that have been entered using the nowplaying command in the same folder
these source files. The file name will be time-stamped so that this won't write over previous lists created when
running this program.
