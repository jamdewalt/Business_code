import os

filepath = input("Please enter the absolute file path you wish to check: ")
os.chdir = filepath

with open('foundfiles.txt','w')as outputfile:
	print("Results of search")
	for filename in os.listdir(filepath) :
		file_size= os.path.getsize(filename)
		if file_size>30:
			print (filename)
			outputfile.write(filename + "\n")
outputfile.close()
