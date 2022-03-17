import shutil, os
#switch to target directory
os.chdir("C:\\Users\\dewaltjm07\\Desktop\\180practicefiles\\180practicefiles")

while True:
	filename = input("Please enter the filename or path to the file you wish to check: ")
	try:
		fhandle = open(filename, 'r')
		break
	except:
		print("\nUnfortunately, this is not a valid file.")
filesize = os.path.getsize(filename)
if filesize >50:
	print("This filesize is greater than 50 bytes")
else:
	print("This filesize is less than 50 bytes")
