import os, subprocess, time, datetime

currentDT = datetime.datetime.now()
print("Hello, today is: " + currentDT.strftime("%m/%d/%Y") + ".")
print() 

while True:
	choice = input("Press 1 to open Calculator or press 2 to open the editor: ")
	if choice in ["1", "2"]:
		break
	else:
		print("Please enter 1 or 2")
if choice == "1":
	subprocess.Popen("C:\\Windows\\System32\\calc.exe")
elif choice == "2":
	subprocess.Popen("C:\\Windows\\System32\\notepad.exe")

#Program keeps running
#Use Converting datetime Objects into Strings section to get the correct date time stamp
