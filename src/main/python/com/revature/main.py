#!/usr/bin/env python3

'''
This is your main script, this should call several other scripts within your packages.
'''

#Modules
from controller import controller as Control

def main():
	Control.run()

if __name__ == '__main__':
	main()
