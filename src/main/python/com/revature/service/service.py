#!/usr/bin/env python3

#Modules
from pathlib import Path
import sys
import re
sys.path.append('io')
import inputoutput as IO
sys.path.append('error')
from error import *
import logging

#Create A Logger For This Script Only
logger = logging.getLogger(__name__)
logging_format = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
logging_handler = logging.FileHandler('logs/Service_Errors.log')
logging_handler.setFormatter(logging_format)
logger.addHandler(logging_handler)

#Check If A Word Exist In Users Database
def checkIfTrue(username,word):
	boolean = False
	open_file = False
	try:
		open_file = True
		with open('database/'+username+'.txt','r') as doc:
			for line in doc:
				line = line.strip()
				if line == word:
					boolean = True
		if boolean == False and open_file == True:
			#raise WarningError
			print('')
	except:
		logger.warning('Could Not Log Into '+username)		
	return boolean

#Check Is Passwords Match
def matchPassword(username,password1, password2):
	try:
		if password1 == password2:
			if IO.addUser(username,password1):
				return True
			else:
				raise Error
		else:
			raise WarningError	
	except WarningError:
		logger.warning('Register Passwords Do Not Match')
		return False
	except Error:
		logger.error('Could Not Add User')
		return False
	
#View Balance
def getBal(username):
	try:
		if IO.checkForData(username):
			IO.viewBal(username)
		else:
			raise WarningError
	except WarningError:
		logger.warning('Could Not Find '+username+' In The Database')	

#Validate Amount
def valiAmount(amount):
	pattern = re.compile('^[0-9]*\.[0-9][0-9]$')
	try:
		if pattern.match(amount):
			return True
		else:
			raise WarningError
	except WarningError:	
		logger.warning('Invalid Deposit Amount')
		return False

#Validate Username
def valiUser(username):
	'''
	Username Must:
	
	1. First Character Can Not Be A Number
	1. Has To Be Atleast 5 Characters Long
	2. Can Not Contain Symbols
	''' 
	pattern = re.compile('^[A-za-z][0-9A-Za-z]{4,}$')
	try:
		if pattern.match(username):
			return True
		else:
			raise WarningError
	except WarningError:
		logger.warning(username+' Was Not Valid')
		return False

#Validate And Deposit
def deposit(username,password,amount):
	try:
		if IO.deposit(username,password,amount):
			return True
		else:
			raise WarningError
	except WarningError:
		logger.warning('Could Not Deposit '+amount+' For '+username)
		return False

#Validate And withdraw
def withdraw(username,password,amount):
	try:
		if IO.withdraw(username,password,amount):
			return True
		else:
			raise WarningError
	except WarningError:
		logger.warning('Could Not Withdraw '+amount+' For '+username)
		return False

#View Transactions
def getTrans(username):
	try:
		if IO.checkForData(username):
			if IO.viewTrans(username):
				return True
			else:
				raise Error
		else: 
			raise WarningError
	except WarningError:
		logger.warning(username+' Does Not Exist In The Database')	
		return False
	except Error:
		logger.error('Could Not Print Transactions For '+username)
		return False

#View Transactions
def checkForData(username):
	return IO.checkForData(username)

