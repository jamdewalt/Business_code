#Overview: This program grants the user the option to search for files of different types, and create an output file listing the results of the search

#This section stores import functions:
import shutil, os, sys

#This section stores a function that restarts the program:
def restart_program():
    print ()
    python = sys.executable
    os.execl(python, python, * sys.argv)
    print()
#This section stores a function that searches for file types and prints the results in a list
def filesearch(file_type):
	filepath = input("Please enter the absolute file path you wish to check: ")
	os.chdir = filepath
	
	with open('search_results.txt','w')as outputfile:
		print()
		print("Search completed. Please check for a file named search_results.txt on your desktop.")
		outputfile.write("Results of file search for files with " + str(file_type)+":\n\n")
		outputfile.write("Your folder path is: " + filepath)
		outputfile.write(""'\n\n')
		for file in os.listdir(filepath):
			if file.endswith(file_type):
				outputfile.write(file + '\n\n')
	outputfile.close()


#This section gives the option to exit or restart the program:
def tryagain():
	while True:
		choice2= input("Thank you for using this program. Press 1 to exit. Press 2 to return to the main menu: ")
		if choice2 in ['1','2']:
			break
		else:
			print()
			print("Invalid entry. Please try again: ")
			print()

	if choice2=='1':
		sys.exit()
	elif choice2=='2':
		menu()

#This section stores the goodbye function, which thanks the user and exits the program:
def goodbye():
	print ("Thank you for utilizing this program.")
	sys.exit()

#This section stores the main menu as a function:		
def menu():
	print("Main Menu:")
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
	print ("6 – Quit the program")
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
		goodbye()		

#This is where the program begins:	
print("Welcome! This program searches for files of a specific type and stores the results of the search in a file.")
print()
menu()

#This gives the option to exit or restart the program:
while True:
	choice2= input("Thank you for using this program. Press 1 to exit. Press 2 to return to the main menu.")
	if choice2 in ['1','2']:
		break
	else:
		print()
		print("Invalid entry.")
		print()

if choice2=='1':
	sys.exit()
elif choice2=='2':
	restart_program()



