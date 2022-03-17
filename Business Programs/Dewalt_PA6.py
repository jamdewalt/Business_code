#Overview: This program searches through files in a directory that contain a specific word or words. It also keeps a running log of each search conducted and the date and time of each search.

#This section stores import functions:
import shutil, os, datetime, sys, os.path

#This section stores the welcome function, which welcomes the user and tells them what the program does
def welcome():
	print("Welcome! This program searches the contents of files for specific terms.")
	print("Names of files that contain those terms will be stored in a file and copies of the files will be stored in a separate folder.")
	print()
	

#This section stores the goodbye function, which thanks the user and exits the program OR allows them to perform another search
def goodbye():
	while True:
		choice2= input("Would you like to conduct another search? Press Y to perform another search or press N to exit: ")
		if choice2 in ['Y','y','N','n']:
			break
		else:
			print()
			print("Invalid entry. Please enter Y to exit or N to perform another search.")
			print()
	if choice2 in ["Y","y"]:
		print()
		mainmenu()
	elif choice2 in ["N","n"]:
		print()
		print("Thank you for using this program.")
		sys.exit()	
		
#This section opens the casefiles.txt file or allows the user to exit/perform another search		
def viewfile():
	while True:
		choice= input("Do you want to view the file? Press Y to open the file or press N to exit the program or conduct another search: ")
		if choice in ['Y','y','N','n']:
			break
		else:
			print()
			print("Invalid entry. Please enter Y to open the file or N to exit the program or conduct another search")
			print()
	if choice in ["Y","y"]:
		print()
		print("Thank you for using this program.")
		os.startfile('casefiles.txt')
		sys.exit()	
		
	elif choice in ["N","n"]:
		print()
		goodbye()
		
		
#This section stores the main menu as a function. Its main purpose is to get filepath data, search terms, and conduct the search of terms to the filepath.	
def mainmenu():
	currentDT = datetime.datetime.now()
	while True:
		filepath = input("Please enter the absolute file path you wish to check: ")
		os.chdir(filepath)
		if os.path.exists(filepath):
			break
		else:	
			print ("Path of the file is Invalid")
			
		if not os.path.exists("e-discovery case files"):
			os.mkdir("e-discovery case files")
	print()
	terms = input("Please enter the search terms you are looking for: ")
	
	with open('casefiles.txt','a')as outputfile:
		print()
		print("Search completed. Please check for a file named casefiles.txt in your directory. This action was taken on " + currentDT.strftime("%a, %d %B %Y %H:%M:%S")+".")
		outputfile.write("Results of file search for files with the terms: " + str(terms) +". This action was taken on " + currentDT.strftime("%a, %d %B %Y %H:%M:%S") + ".")
		outputfile.write(""'\n\n')
		for file in os.listdir(filepath):
			if os.path.isfile(file):
				fhandle=open(file,"r",encoding="ISO-8859-1")
				file_contents = fhandle.read()
				if terms in file_contents:
					outputfile.writelines(file + '\n\n')
					shutil.copy(file, "e-discovery case files")
	viewfile()


#This is where the program begins:	
welcome()
mainmenu()
