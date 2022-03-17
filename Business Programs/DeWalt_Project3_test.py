#Overview: This program calculates the amount of money a customer owes for a billing period and creates a bill (by writing and saving a file) for the customer
#Team members: James DeWalt

#This section stores import functions:
import shutil, os, datetime, time, sys

#This section stores the welcome function, which greets the user
def welcome():
	print("Welcome to the 180 Energies Customer Billing System.")
	print()
	dash = '-' * 50
	print (dash)
	print()
	
#This section stores the goodbye function, which thanks the user and exits the program OR allows them to perform another search
def goodbye():
	while True:
		print("Customer bills can be located under the following file path: C:\\Customer\\Bills\\")
		print()
		choice2= input("Would you like to prepare another customer bill or quit? Press 1 to prepare another bill or press N to exit: ")
		if choice2 in ['1', '2']:
			break
		else:
			print()
			print("Invalid entry. Press 1 to prepare another bill or press 2 to exit")
			print()
	if choice2 == "1":
		print()
		infomenu()
	elif choice2 == "2":
		print()
		print("Thank you for using this program.")
		sys.exit()	

#This section lets the user proceed to type the customer information in or sends the user to a menu that reminds them to do it later		
def reminder():
	while True:
		print("It is almost the end of the month. Billing statements must be prepared by the 29th of each month.")
		choice= input("Would you like to prepare customer billing statements now? Press 1 for yes, or press 2 to be reminded later: ")
		if choice in ['1', '2']:
			break
		else:
			print()
			print("Invalid entry. Please press 1 for yes, or press 2 to be reminded later")
			print()
	if choice in ["1"]:
		print()
		infomenu()
	elif choice in ["2"]:
		print()
		timemenu()		

#This section sets the program to sleep for the chosen time before returning to the reminder function
def timemenu():
	dash = '-' * 50
	print (dash)
	print()
	print("Remind me in:")
	print()
	print ("1. Ten minutes")
	print ("2. One hour")
	print ("3. 24 hours")	
	while True:
		choice = input("Would you like to be reminded? Enter the number of your choice: ")
		if choice in ['1','2','3']:
			break
		else:
			print()
			print ("Invalid option. Please enter 1,2 or 3")
	print()
	if choice== "1":
		time.sleep(600)
		reminder()
	elif choice== "2":
		time.sleep(3600)
		reminder()
	elif choice== "3":	
		time.sleep(86400)
		reminder()
	
#This section has the user input what the customer code is and what the account number is. It also lets them re-enter info if needed.
def infomenu():
	print("180 Energies Customer Billing System")
	print("Enter customer information:")
	print()
	dash = '-' * 50
	print(dash)
	print()
	print("Customer codes are - (r)esidential, (c)ommercial, or (i)ndustrial")
	print()
	while True:
		global code
		code = input("Enter the customer code: ")
		if code in ['r','c','i']:
			break
		else:
			print("Invalid entry. Please enter r, c, or i")
	global account
	account = input("Enter the customer account number: ")
	print()
	print("You have entered the following information:")
	print()
	print("Customer code: " + str(code))
	print("Customer account: " + str(account))
	print()
	while True:
		choice2 = input("Is the information above correct? Press 1 for yes, or press 2 to re-enter the customer information: ")
		if choice2 in ['1', '2']:
			break
		else:
			print()
			print("Invalid entry. Press 1 for yes, or press 2 to re-enter the customer information")
			print()
	if choice2 == "1":
		print()
		metermenu()
	elif choice2 == "2":
		print()
		infomenu()
	
#This section has the user input what the current meter and previous meter is at. It then calculates the total cost based on their customer code. It also lets them re-enter info if needed.		
def metermenu():	
	print("180 Energies Customer Billing System")
	print("Enter meter information:")
	print()
	dash = '-' * 50
	print(dash)
	print()
	while True:
		global previous_meter
		previous_meter = input("Enter the customer's previous meter reading: ")	
		print()
		if previous_meter.isdigit():
			previous_meter = int(previous_meter)
			break
		else:
			print()
			print("Please retry and enter a number.")
		print()
	while True:
		global current_meter
		current_meter = input("Enter the customer's current meter reading: ")
		print()
		if current_meter.isdigit():
			current_meter = int(current_meter)
			break
		else:
			print()
			print("Please retry and enter a number.")
	global total_therms_used
	total_therms_used = (current_meter - previous_meter) * 1.00 * 1.023
	total_therms_used = float(total_therms_used)
	total_therms_used = round(total_therms_used,2)
	if code == 'r':
		therm_cost = .1453
		day_cost = .80
	elif code == 'c':
		therm_cost = .1053
		day_cost = 3.72	
	elif code == 'i':
		therm_cost = .0694
		day_cost = 23.30	
	global ammount
	ammount = (therm_cost * total_therms_used) + (day_cost * 30)
	ammount = float(ammount)
	ammount = round(ammount, 2)
	print()
	print("You have entered the following information:")
	print()
	print("Customer code: " + str(code))
	print("Customer account: " + str(account))
	print("Previous meter reading: " + str(previous_meter))
	print("Current meter reading: " + str(current_meter))
	print("Number of therms used: " + str(total_therms_used))
	print("Current amount due: $" + str(ammount))
	print()
	while True:
		choice2 = input("Is the meter information above correct? Press 1 for yes, or press 2 to re-enter the meter information: ")
		if choice2 in ['1', '2']:
			break
		else:
			print()
			print("Invalid entry. Press 1 for yes, or press 2 to re-enter the customer information")
			print()
	if choice2 == "1":
		get_filename_datetime()
	
	elif choice2 == "2":
		print()
		metermenu()
	
#This section takes all the accumulated data and stores it within an output file under a path named	'C:\\Customer\\Bills' It also opens the file if prompted and lets the user type in another customer bill	
def get_filename_datetime():
	currentDT = datetime.datetime.now()
	start_date = datetime.datetime.now() + datetime.timedelta(30)
	t = time.localtime()
	timestamp = time.strftime('%b-%d-%Y', t)
	newname = str(account)+ "_" + timestamp + '.txt'
	
	if code == 'r':
		code2 = "Residential"
	elif code == 'c':
		code2 = "Commercial"
	elif code == 'i':
		code2 = "Industrial"
	
	if not os.path.exists('C:\\Customer\\Bills'):
		os.makedirs('C:\\Customer\\Bills')

	with open(os.path.join('C:\\Customer\\Bills', newname),'w')as outputfile:
		print()
		outputfile.write("180 Wisconsin Energies\n")
		outputfile.write("UW-Whitewater\n")
		outputfile.write("Whitewater, Wisconsin\n")
		outputfile.write(""'\n')
		outputfile.write(""'\n')
		outputfile.write("------------------------------------------------------------------------"'\n')
		outputfile.write(""'\n')
		outputfile.write(""'\n')
		outputfile.write("Customer Type:"+ '\t \t \t'+str(code2)+ '\n')
		outputfile.write("Account Number:"+ '\t \t \t'+ str(account)+ '\n')
		outputfile.write(""'\n')
		outputfile.write("Billing Date:" + '\t \t \t'+ currentDT.strftime("%a, %d %B %Y") + '\n')
		outputfile.write("Due Date:" + '\t \t \t' + start_date.strftime("%a, %d %B %Y") + '\n')
		outputfile.write(""'\n')
		outputfile.write(""'\n')
		outputfile.write("------------------------------------------------------------------------"'\n')
		outputfile.write(""'\n')
		outputfile.write(""'\n')
		outputfile.write("Previous meter reading:"+ '\t \t' + str(previous_meter)+ '\n')
		outputfile.write("Current meter reading:"+ '\t \t' + str(current_meter)+ '\n')
		outputfile.write("Number of therms used:"+ '\t \t' + str(total_therms_used)+ '\n')
		outputfile.write("Amount due: "+ '\t \t \t' + "$"+ str(ammount)+ '\n')
		outputfile.write(""'\n')
		outputfile.write(""'\n')
		outputfile.write("------------------------------------------------------------------------"'\n')
		outputfile.write(""'\n')
		outputfile.write(""'\n')
		outputfile.write("Message Center:\n")
		outputfile.write("Thank you for using 180 Wisconsin Energies. We appreciate having you as a customer and we are available to you 24 hours a day, 7 days a week. Happy Holidays!\n")
		
	outputfile.close()	
	while True:
		choice2 = input("Would you like to view the bill now? Press 1 for yes, or press 2 to continue: ")
		if choice2 in ['1', '2']:
			break
		else:
			print()
			print("Invalid entry. Press 1 for yes, or press 2 to continue.")
			print()
	if choice2 == "1":
		print()
		os.startfile("C:\\Customer\\Bills\\" + newname)
		goodbye()
	elif choice2 == "2":
		print()
		goodbye()
			
#This is where the program begins:	
welcome()
reminder()

