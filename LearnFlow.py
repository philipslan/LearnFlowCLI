##
# import statements
##

from clint import resources, arguments
from clint.textui import colored, puts, indent, prompt, validators

##
# Main function
##

commandOptions = {
	'register': 'Register for a LearnFlow account',
	'login': 'Log in to LearnFlow',
	'logout': 'Log out of LearnFlow',
	'?': 'See available commands'
}

commandList = commandOptions.keys()

commandValidator = validators.OptionValidator(commandList,'Sorry, we did not recognize that command. Type ? and hit enter for a list of available commands')

def learnFlow():
	puts('Welcome to LearnFlow\nType ? and hit enter for a list of available commands')
	while (True):
		command = prompt.query(':', validators=[commandValidator])
		if (command):
			puts('run command')

##
# Run script
##
learnFlow()