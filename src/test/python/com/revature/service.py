#Add New User To Database
def addUser(Username,Password):
	boolean = False
	with open(Username+'.txt','w') as doc:
		doc.write(Username+'\n')
		doc.write(Password+'\n')
		boolean = True
		print('####Test User Added Successful####')
	if boolean == False:
		print('####Test User Add Failed####')	
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
