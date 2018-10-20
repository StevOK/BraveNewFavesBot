#BraveNewFavesBot chat bot code
#Most of this code is from a tutorial, so I hope there isn't anything dumb in here
import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
import datetime

#This will open up a socket and print a nice message to the chat saying the bot is working
s = openSocket()
joinRoom(s)

readbuffer = "" #buffer for incoming chat messages
lst = [] #start a list for user submissions

#Here I come up with a unique name for a text file to be created by the bot
# so that it doesn't write over older lists
fname = datetime.datetime.now().strftime("%m-%d-%H-%M")+'-list.txt'

while True:
		#Get a message from chat, then clean it up for our purposes
		readbuffer = readbuffer + s.recv(1024).decode("utf-8")
		temp = str.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			#Gotta PONG when twitch PINGs you, or you'll lose your socket
			#This is probably a pretty bad way of writing this but it works
			if "PING :tmi.twitch.tv" in line:
				s.send("{}\r\n".format("PONG :tmi.twitch.tv").encode("utf-8"))
				break
			user = getUser(line)
			message = getMessage(line)
			#Prints a cleaned-up version of every message typed in chat to the prompt screen,
			# even though all that information already gets displayed
			print (user + " :" + message) 
			
			#This will check each message in chat to see if it has a youtube link in it,
			# then add the post to the list and the bot's chat if it does.
			# I bet I could clean this up but it picks up all the messages in the format
			# with which viewers have been submitting videos in the past.
			if ("youtube.com" in message or "youtu.be" in message):
				#Add the post to the list
				lst.append(user + ": " + message)
				#Add the post to the bot's chat. Might make this its own function at some point,
				# especially since it should print to whatever the bot's name is rather than this
				# bot specifically.
				messageTemp = "PRIVMSG #" + "bravenewfavesbot" + " :" + user + ": " + message
				s.send("{}\r\n".format(messageTemp).encode("utf-8"))
				break
			
			#If you type in the command !printlist, the bot will literally print
			# the list to an output file every time. It writes over older versions of the file,
			# but since the list keeps older posts between printings, it's like adding to the file. 
			#For now I have my username in here too since I'm the one who is running the code,
			# but I will remove it once Kathleen takes over.
			#I used this format for the command to mirror commands in other popular chat bots.
			if ("kathleen_lrr" in user or "freshprinceofbeleren" in user) and "!printlist" in message:
				f=open(fname, 'w')
				for line in lst:
					f.write("%s\n\n" % line)
				f.close()
				break
