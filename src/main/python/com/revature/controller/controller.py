#!/usr/bin/env python3

#Modules
import sys
sys.path.append('service')
import service as Service
from getpass import getpass
import hashlib

#Run Controller
def run():
	#Global Variables
	MAIN = True
	USER = True
	MEMBER = False
	USERNAME = ''
	PASSWORD = ''
	SALT = 'SALT(LOL)'
	
	#Main Loop
	while MAIN:
		#User Options
		while USER:
			HASHER = hashlib.sha1()
			CON_HASHER = hashlib.sha1()
			print('~~~~~~~~~~~~~~~~~~~~{User Options}~~~~~~~~~~~~~~~~~~~~')
			user_input = input('Enter "r" To Register\nEnter "l" To Login\nEnter "e" To Exit Application\n-> ') 
			#Ignore Case
			user_input = user_input.lower()	
	
			#Register A New User
			if user_input == 'r':
				print('~~~~~~~~~~~~~~~~~~~~{Register}~~~~~~~~~~~~~~~~~~~~')
				username = input('Enter New Username\n-> ')
				password = getpass('Enter New Password\n-> ')
				confirm_password = getpass('Enter New Password Again\n-> ')
				#Check Database, Validate and Add 
				if Service.checkForData(username):
					print('###############[User Already Exist]###############')
				else:
					HASHER.update((username + password + SALT).encode('utf-8'))
					hashed_password = HASHER.hexdigest()
					CON_HASHER.update((username + confirm_password + SALT).encode('utf-8'))
					confirm_hashed_password = CON_HASHER.hexdigest()
					#Validate Andd Add Password
					if Service.matchPassword(username,hashed_password,confirm_hashed_password):
						print('###############[New User Created]###############')
					else:
						print('###############[Password Is Not Valid]###############')
			#Login
			elif user_input == 'l':
				print('~~~~~~~~~~~~~~~~~~~~{Login}~~~~~~~~~~~~~~~~~~~~')
				username = input('Enter Username\n-> ')
				password = getpass('Enter Password\n-> ')
				#Hash
				HASHER.update((username + password + SALT).encode('utf-8'))
				hashed_password = HASHER.hexdigest()
				#Check Database
				if Service.checkIfTrue(username,username) and Service.checkIfTrue(username,hashed_password):
					print('###############[Logged In]###############')
					USERNAME = username
					PASSWORD = hashed_password
					USER = False
					MEMBER = True
				else: 	
					print('###############[Not Found In The System]###############')

			#Exit Application
			elif user_input == 'e':
				MAIN = False
				USER = False
			
			#Check Other Inputs
			else:
				print('###############[Invalid Input]###############')

		#Member Options
		while MEMBER:
			print('~~~~~~~~~~~~~~~~~~~~{Member Options}~~~~~~~~~~~~~~~~~~')
			#New Option List
			member_input = input('Enter "v" To View Balance\nEnter "d" To Deposit Money\nEnter "w" To Withdraw Money\nEnter "t" To View Past Transactions\nEnter "l" To Log Out\n-> ')
					
			#Ignore Case
			member_input = member_input.lower()

			#View Balance
			if member_input == 'v':
				Service.getBal(USERNAME)
		
			#Deposit Money	
			elif member_input == 'd':
				print('~~~~~~~~~~~~~{Enter Amount To Deposit}~~~~~~~~~~~~~~~~')
				amount = input('$')
				if Service.valiAmount(amount):
					if Service.deposit(USERNAME,PASSWORD,amount):
						print('###############[Deposit Completed]###############')
					else:
						print('###############[Deposit Could Not Be Completed]###############')
				else:
					print('#####[Invalid Input! (Examples: $5.00 or $0.30 or $95846785.04) ]##########')

			#Withdraw Money
			elif member_input == 'w':
				print('~~~~~~~~~~~~~{Enter Amount To Withdraw}~~~~~~~~~~~~~~~')
				amount = input('$')
				if Service.valiAmount(amount):
					if Service.withdraw(USERNAME,PASSWORD,amount):
						print('###############[Withdraw Completed]###############')
					else:
						print('###############[Withdraw Could Not Be Completed]###############')			
				else :
					print('##########[Invalid Input! (Examples. $5.00 or $0.30 or $95846785.04) ]##########')
		
			#View Transactions
			elif member_input == 't':
				if Service.getTrans(USERNAME):
					print('###############[Past Transactions]###############')
				else: 
					print('###############[No Past Transactions]###############')
			
			#Logout
			elif member_input == 'l':
				print('###############[Logged Out]###############')
				USERNAME = ''
				PASSWORD = ''
				USER = True
				MEMBER = False

			#Check Other Inputs
			else:
				print('###############[Invalid Input]###############')
