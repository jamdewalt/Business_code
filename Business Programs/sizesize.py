import os

filepath = input("Please enter the absolute file path you wish to check: ")
os.chdir = filepath
	
with open('search_results.txt','w')as outputfile:
	print()
	print("Search completed. Please check for a file named search_results.txt on your desktop.")
	outputfile.write("Results of file search for files with :\n\n")
	outputfile.write("Your folder path is: " + filepath)
	outputfile.write(""'\n\n')
	for file in os.listdir(filepath):
		file = file.strip()
		fsize = os.path.getsize(file)
	if fsize > 4000:
		print(file)
		outputfile.write(file + '\n\n')
outputfile.close()
