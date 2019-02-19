#!/usr/bin/env python3
import service as s
'''
This is your main testing script, this should call several other testing scripts on its own
'''
def main():
	Username = 'TestUser'
	Password = 'TestPassword'
	print('\n\n')
	input('Press "Enter" To Run Application Test')
	s.addUser(Username,Password)
	s.login(Username,Password)
	print('\n\n')

if __name__ == '__main__':
	main()
