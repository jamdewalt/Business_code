#This program searches for files of a certain size and writes the result to an outputfile
import shutil, os

os.chdir("C:\\Users\\james\\Desktop\\Test")
os.getcwd()


fhandle = open("casefiles.txt")
file_contents = fhandle.read()
print (file_contents)

if "and" in file_contents:
	print("Term was found.")
else:
	print("Term not found.")



