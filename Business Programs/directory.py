#This program creates a directory and searchs files for content
import shutil, os

os.chdir("C:\\Users\\james\\Desktop\\Test")

if not os.path.exists("newdirectory"):
	os.mkdir("newdirectory")
	
terms =input("Enter your terms: ")
for filename in os.listdir("C:\\Users\\james\\Desktop\\Test"):
	if os.path.isfile(filename):
		fhandle=open(filename,"r",encoding="ISO-8859-1")
		file_contents = fhandle.read()
		if terms in file_contents:
			print(filename)
			shutil.copy(filename, "newdirectory")
			
	
