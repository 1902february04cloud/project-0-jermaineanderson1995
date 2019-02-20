#!/usr/bin/env python3

#Modules
from pathlib import Path
import logging
import time
import sys
sys.path.append('error')
from error import *

#Create A Logger For This Script Only
logger = logging.getLogger(__name__)
logging_format = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
logging_handler = logging.FileHandler('logs/IO_Errors.log')
logging_handler.setFormatter(logging_format)
logger.addHandler(logging_handler)

#Check If Username Exist In Database
def checkForData(username):
	boolean = False
	try:
		with open('database/'+username+'.txt','r') as doc:
			boolean = True
	except:
		boolean = False
	return boolean

#Add New User To Database
def addUser(username, password):
	boolean = False
	try:
		with open('database/'+username+'_Transaction.txt','a+') as doc:
			doc.write('')
			boolean = True
		if boolean == False:
			raise Error
		boolean == False	
		with open('database/'+username+'.txt','a+') as doc:
			doc.write(username+'\n')
			doc.write(password+'\n')
			doc.write('0.00\n')
			boolean = True
		if boolean == False:
			raise Error
	except Error:
		logger.error('Could Not Create Database For '+username)
	return boolean

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
			raise Error
	except Error:
		logger.error(username+'\'s Balance Does Not Exist')
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
			raise Error
	except Error:
		logger.error('Could Not Read The Balance For '+username)


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
		if boolean == False:
			raise Error
	except Error:
		logger.error(username+' Has No Transactions')
	return boolean

#Deposit Amount
def deposit(username,password,amount):
	boolean = False
	try:
		balance = str(float(readBal(username)) + float(amount))
		with open('database/'+username+'.txt','w') as doc:
			doc.write(username+'\n')
			doc.write(password+'\n')
			doc.write(balance+'\n')
			message = str(time.ctime())+' Deposit In The Amount Of '+amount
			record(username,message)
			boolean = True
		if boolean == False:
			raise Error
	except Error:
		logger.error(username+' Could Not Deposit To Database')	
		boolean =  False
	return boolean

#Withdraw Amount
def withdraw(username,password,amount):
	#Variables
	boolean = False
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
							message = str(time.ctime())+' Withdrawal In The Amount Of '+amount
							record(username,message)
							boolean = True
					else:
						raise WarningError
		if boolean == False:
			raise Error
	except WarningError:
		logger.warning(username+' Has Insufficient Funds To Widthdraw '+amount)	
	except Error:
		logger.error(username+' Could Not Withdraw From The Database')
	return boolean

#Record Transaction
def record(username,transaction):
	boolean = False
	try:
		with open('database/'+username+'_Transaction.txt','a+') as doc:
			doc.write(transaction+'\n')
			boolean = True
		if boolean == False:
			raise Error
	except:
		logger.error('Count Not Record Transaction For '+username)
