##
# import statements
##

from clint import resources, arguments
from clint.textui import colored, puts, indent, prompt, validators, columns

##
# Main function
##

def learnFlow():
	data = SessionData()
	puts('Welcome to LearnFlow\nType ? and hit enter for a list of available commands')
	while (data.__LF_Running__):
		command = prompt.query('> ').split()
		try:
			command[0] = commandValidator(command[0])
		except Exception as e:
			puts(colored.yellow(e.message))
			command[0] = None
		if (command and command[0]):
			try:
				commandToFunction[command[0]](data,command[1:])
			except NameError:
				pass

##
# Helper functions
##

def printOptions(data,arg):
	width = 10
	for c in commandList:
		puts(columns([colored.green(c),width],[commandOptions[c],None]))
	puts('')

def register(data,arg):
	puts ('Choose a username and password. ' + colored.red('Note that this application is NOT secure.') + " do not use a password you use elsewhere.")
	username = prompt.query('> username: ')
	password = prompt.query('> password: ')
	# run register endpoint
	puts('')

def login(data,arg):
	username = prompt.query('> username: ')
	password = prompt.query('> password: ')
	# run login endpoint
	data.token = 'token'
	puts ('You have been logged in successfully.\n')

def logout(data,arg):
	data.token = ''
	puts ('You have been logged out successfully.\n')

def quitLearnFlow(data,arg):
	data.__LF_Running__ = False

def printStatus(data,arg):
	print data.token
	print data.__LF_Running__

def viewTracks(data,arg):
	# tracks endpoint
	#for track in myTracks:
	#	puts (track.name) 
	puts('')

def browse(data,arg):
	puts('')
	# browse endpoint
	#for track in tracks:
	#	puts(track.name)

def view(data, arg):
	print(arg)
	# 

##
# Program data
##

commandOptions = {
	'register': 'Register for a LearnFlow account',
	'login': 'Log in to LearnFlow',
	'logout': 'Log out of LearnFlow',
	'?': 'See available commands',
	'q': 'Quit LearnFlow',
	'status': 'Check login status',
	'tracks': 'View your saved tracks',
	'browse': 'View all tracks',
	'view': 'View a specific track'
}

commandToFunction = {
	'register': register,
	'login': login,
	'logout': logout,
	'?': printOptions,
	'q': quitLearnFlow,
	'status': printStatus,
	'tracks': viewTracks,
	'browse': browse,
	'view': view,
}

commandList = commandOptions.keys()

commandValidator = validators.OptionValidator(commandList,'Sorry, we did not recognize that command. Type ? and hit enter for a list of available commands')

##
# Session Data
##

class SessionData:
	def __init__(self):
		self.token = ''
		self.__LF_Running__ = True

##
# Run script
##

learnFlow()



