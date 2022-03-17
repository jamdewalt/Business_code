#Overview: This program grants the user the option to search for files of different types and creates an output file listing the results of the search
#Team members: James DeWalt

#This section stores import functions:
import shutil, os, sys

#This section stores the goodbye function, which thanks the user and exits the program OR sends the user back to the main menu:
def goodbye():
	while True:
		choice2= input("Are you sure you want to quit? Press Y to exit or press N to return to the main menu: ")
		if choice2 in ['Y','y','N','n']:
			break
		else:
			print()
			print("Invalid entry. Please enter Y to exit or N to return to the main menu.")
			print()
	if choice2 in ["N","n"]:
		print()
		mainmenu()
	elif choice2 in ["Y","y"]:
		print()
		print("Thank you for using this program.")
		sys.exit()	 
 
#This section stores a function that searches for file types and prints the results in a list
def filesearch(file_type):
	filepath = input("Please enter the absolute file path you wish to check: ")
	os.chdir = filepath
	
	with open('type_result.txt','w')as outputfile:
		print()
		print("Search completed. Please check for a file named type_results.txt on your desktop.")
		outputfile.write("Results of file search for files with " + str(file_type)+":\n\n")
		outputfile.write("Your folder path is: " + filepath)
		outputfile.write(""'\n\n')
		for file in os.listdir(filepath):
			if file.endswith(file_type):
				outputfile.write(file + '\n\n')
	outputfile.close()
	print()
	goodbye()

#This section stores the file menu as a function and searches for specific types of files:		
def filemenu():
	print("This option searches for files of a specific type and stores the results of the search in a file:")
	dash = '-' * 30
	print (dash)
	print ("1 – PDF (typically ending in .pdf)")
	print()
	print ("2 – Text (typically ending in .txt)")
	print()
	print ("3 – Word (typically ending in .docx)")
	print()
	print ("4 – Excel (typically ending in .xls)")
	print()
	print ("5 – Python (typically ending in .py)")
	print()
	print ("6 – exit this option and return to the main menu")
	print()
	while True:
		choice = input("Please enter a number to select a file to search for(1,2,3,4,5,6): ")
		if choice in ['1','2','3','4','5','6']:
			break
		else:
			print()
			print ("Invalid option. Please enter 1,2,3,4,5, or 6.")
	print()
	if choice== "1":
		file_type = ".pdf"
		filesearch(file_type)
	elif choice== "2":
		file_type = ".txt"
		filesearch(file_type)
	elif choice== "3":
		file_type = ".docx"
		filesearch(file_type)
	elif choice== "4":
		file_type = ".xls"
		filesearch(file_type)
	elif choice== "5":
		file_type = ".py"
		filesearch(file_type)
	elif choice== "6":
		mainmenu()


#This section stores the main menu as a function:		
def mainmenu():
	print("Main Menu:")
	dash = '-' * 30
	print (dash)
	print ("1 – Search files by type")
	print()
	print ("2 – Quit program")
	print()
	while True:
		choice = input("Please enter a number to select one of the above options: ")
		if choice in ['1','2']:
			break
		else:
			print()
			print ("Invalid option. Please enter 1 or 2.")
	print()
	if choice== "1":
		filemenu()
	elif choice== "2":
		goodbye()

#This is where the program begins:	
print("Welcome! This program searches for file content.")
print()
mainmenu()





