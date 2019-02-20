#!/usr/bin/env python3
import service as s
'''
This is your main testing script, this should call several other testing scripts on its own
'''
def main():
	Username = 'TestUser'
	Password = 'TestPassword'
	Amount = '10'
	F_Username = 'Test'
	F_Password = 'Incorrect'
	F_Amount = 'Money'
	print('\n')
	input('Press "Enter" To Run Application Test')
	print('\n')

	print('Username: '+Username+'\nPassword: '+Password)
	s.login(Username,Password)
	print('\n')

	print('Amount: '+Amount)
	s.deposit(Username,Password,Amount)
	print('\n')

	print('Username: '+Username+'\nPassword: '+F_Password)
	s.login(Username,F_Password)
	print('\n')

	print('Amount: '+F_Amount)
	s.deposit(Username,Password,F_Amount)
	print('\n')

if __name__ == '__main__':
	main()
