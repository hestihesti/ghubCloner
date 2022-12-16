import os
import sys
from termcolor import colored


def git():
	i = ''
	while i != 'q':
		print(colored('Press "q" To Quit', 'red'))
		author = input('Who Is The Author Of The Repo:\n> ')
		name = input('What Is The Repositories Name:\n> ')
		format = f'git clone https://github.com/{author}/{name}.git'
		gt = 'gnome-terminal -x ' + format
		os.system(gt)


git()
