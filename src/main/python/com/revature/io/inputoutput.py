#!/usr/bin/env python3
'''
1. Add returns to all functions
'''
#Modules
from pathlib import Path
import logging
from datetime import datetime

#Create A Logger For This Script Only
logger = logging.getLogger(__name__)
logging_format = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
logging_handler = logging.FileHandler('logs/IO_Errors.log')
logging_handler.setFormatter(logging_format)
logger.addHandler(logging_handler)

#Check If Username Exist In Database
def checkForData(username):
	try:
		with open('database/'+username+'.txt','r') as doc:
			return True
	except:
		return False

#Add New User To Database
def addUser(username, password):
	try:
		with open('database/'+username+'_Transaction.txt','a+') as doc:
			doc.write('')	
		with open('database/'+username+'.txt','a+') as doc:
			doc.write(username+'\n')
			doc.write(password+'\n')
			doc.write('0.00\n')
			return True
	except:
		logger.critical('Could Not Create Database For '+username)
		return False

#View Balance
def viewBal(username):
	#Variable
	boolean = True
	count = 0
	print('\n')
	try:
		with open('database/'+username+'.txt','r') as doc:
			for line in doc:
				count += 1
				if count == 3:
					line = line.strip()
					print('$'+line)
					boolean = False
		if boolean:
			logger.critical(username+'\'s Balance Does Not Exist')
		print('###############Balance###############')
	except:
		logger.critical('Could Not Print Balance For '+username)
	return boolean
#Read Balance:
def readBal(username):
	#Variable
	boolean = True
	count = 0
	try:
		with open('database/'+username+'.txt','r') as doc:
			for line in doc:
				count += 1
				if count == 3:
					line = line.strip()
					boolean = False
					return line
		if boolean:
			logger.critical(username+'\'s Balance Does Not Exist')
	except:
		logger.critical('Could Not Read The Balance For '+username)


#View Transactions
def viewTrans(username):
	#Variables
	boolean = False
	print('\n')
	try:
		with open('database/'+username+'_Transaction.txt','r') as doc:
			for line in doc:
				if line != '':
					line = line.strip()
					print(line)
					boolean = True
	except:
		logger.critical('Could Not Get The Transaction For '+username)
	return boolean

#Deposit Amount
def deposit(username,password,amount):
	try:
		balance = str(float(readBal(username)) + float(amount))
		with open('database/'+username+'.txt','w') as doc:
			doc.write(username+'\n')
			doc.write(password+'\n')
			doc.write(balance+'\n')
			message = str(datetime.now())+' Deposit In The Amount Of '+amount
			record(username,message)
			return True
	except:
		logger.critical(username+' Could Not Deposit')	
		return False

#Withdraw Amount
def withdraw(username,password,amount):
	#Variables
	count = 0
	try:
		with open('database/'+username+'.txt','r') as doc:
			for line in doc:
				count += 1
				if count == 3:
					#Validate
					line = float(line)
					amount = float(amount)
					if line >= amount:
						balance = line - amount
						balance = str(balance)
						amount = str(amount)
						with open('database/'+username+'.txt','w') as doc:
							doc.write(username+'\n')
							doc.write(password+'\n')
							doc.write(balance+'\n')
							message = str(datetime.now())+' Withdrawal In The Amount Of '+amount
							record(username,message)
							return True

	except:
		logger.critical(username+' Could Not Withdraw')	
		return False

#Record Transaction
def record(username,transaction):
	try:
		with open('database/'+username+'_Transaction.txt','a+') as doc:
			doc.write(transaction+'\n')
	except:
		logger.critical('Count Not Record Transaction For '+username)
