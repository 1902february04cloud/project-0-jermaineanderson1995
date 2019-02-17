#!/usr/bin/env python3

#Modules
from pathlib import Path
import sys
import re

#Find Path To Module
sys.path.append('io')
import inputoutput as IO

#Modules
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
	#txt = Path('database/'+username+'.txt')
	try:
		open_file = True
		with open('database/'+username+'.txt','r') as doc:
			for line in doc:
				line = line.strip()
				if line == word:
					boolean = True
		if boolean == False and open_file == True:
			logger.warning('Could Not Find '+word+' In '+username+'\'s Database')		
	except:
		logger.error('Could Not Find '+username+' In The Database')	
	return boolean

#Check Is Passwords Match
def matchPassword(username,password1, password2):
	if password1 == password2:
		if IO.addUser(username,password1):
			return True
		else:
			return False
	else:	
		logger.warning('Passwords Do Not Match')
		return False

#View Balance
def getBal(username):
	if IO.checkForData(username):
		IO.viewBal(username)
	else:
		logger.error('Could Not Find '+username+' In The Database')	

#Validate Amount
def valiAmount(amount):
	pattern = re.compile('^[0-9]*\.[0-9][0-9]$')
	if pattern.match(amount):
		return True
	else:
		logger.warning('Invalid Deposit Amount')
		return False

#Validate And Deposit
def deposit(username,password,amount):
	if IO.deposit(username,password,amount):
		return True
	else:
		logger.error('Could Not Deposit')
		return False

#Validate And withdraw
def withdraw(username,password,amount):
	if IO.withdraw(username,password,amount):
		return True
	else:
		logger.error('Could Not Withdraw')
		return False

#View Transactions
def getTrans(username):
	if IO.checkForData(username):
		if IO.viewTrans(username):
			return True
		else:
			return False
	else: 
		logger.error('Could Not Find '+username+' In The Database')	
		return False

#View Transactions
def checkForData(username):
	return IO.checkForData(username)
