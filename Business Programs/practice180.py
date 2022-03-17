#This program searches for files of a certain size and writes the result to an outputfile
import os

filepath = input("Please enter the absolute file path you wish to check: ")
os.chdir = filepath

with open('foundfiles.txt','w')as outputfile:
	outputfile.write("Results of search: files greater than 300 bytes\n\n")
	for file in os.listdir(filepath):
		fsize = os.path.getsize(file)
		if fsize >3000:
			print (file)
			outputfile.write(file + '\n')
	
outputfile.close()




	
	
