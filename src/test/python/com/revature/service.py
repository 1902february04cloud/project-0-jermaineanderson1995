#Login
def login(Username,Password):
	boolean = False
	with open(Username+'.txt','r') as doc:
		for line in doc:
			line = line.strip()
			if line == Password:
				boolean = True
				print('####Login Successful####')
	if boolean == False:
		print('####Login Failed####')

#Deposit
def deposit(Username,Password,Amount):
	boolean = False
	count = 0
	if Amount.isnumeric():
		with open(Username+'.txt','w') as doc:
			doc.write(Username+'\n')
			doc.write(Password+'\n')
			doc.write(Amount+'\n')
			boolean = True
			print('#####Deposit Successful#####')
		if boolean == False:
			print('#####Deposit Failed#####')
	else:
		print('#####Invalid Deposit#####')
	
