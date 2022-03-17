# Overview: This program enables the user to encrypt and decrypt messages

#This section stores import functions:
import sys

#This section stores the encryption function with Reverse and Caesar Cyphers:	
def encrypt():
	
	#This is the menu in which the user chooses an encryption option:
	while True:
		msg = input("Please enter a message that you want to encrypt: ")
		method = input("Please select a method of encryption. Type 1 for Reverse Cypher or 2 for Caesar Cypher: ")
		if method in ['1','2',]:
			break
		else:
			print()
			print ("Invalid option. Please enter 1 or 2")
			
	#This section reverse encrypts the message and prints the message
	if method == "1":
		reverse_msg = msg[::-1]
		print()
		print("This is your original message: " + msg)
		print("This is your reverse encrypted message: " + reverse_msg)
		print()
		menu()
		
	#This section encrypts with a caesar cypher and prints the results
	elif method == "2":
		while True:
			key = input("Please enter a whole number between 1 and 25 for your key: ")
			if key in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']:
				break
			else:
				print("Must enter a whole number between 0 and 25")
		alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		msg = msg.upper()
		key = int(key)
		secretmsg = ""

		for letter in msg:
			if letter in alpha:
				letter_index = alpha.find(letter) + key
				if letter_index>25:
					letter_index=letter_index-26
				secretmsg = secretmsg + alpha[letter_index]
			else:
				secretmsg = secretmsg + letter
	
		print()
		print("Your original message was: " + msg)
		print("Your selected key was: " , key)
		print("Your encrypted message is: " + secretmsg)
		print()
		menu()
		
#This section stores the function used to decrypt messages with Reverse, Caesar, and Brute Force decryption:
def decrypt():
	
	#This is the menu in which the user chooses an decryption option:
	while True:
		message = input("Please enter a message that you want to decrypt:")
		method2 = input("Please select a method of decryption. Type 1 for Reverse Cypher, 2 for Caesar Cypher, or 3 if you don't know: ")
		if method2 in ['1','2','3']:
			break
		else:
			print()
			print ("Invalid option. Please enter 1,2, or 3")
			
	#This section reverse decrypts the message and prints the results
	if method2 == "1":
		reverse_message = message[::-1]
		print()
		print("This is your original message: " + message)
		print("This is your decrypted message: " + reverse_message)
		print()
		menu()
		
	#This section decrypts a caesar cypher and prints the results	
	elif method2 == "2":
		while True:
			key = input("Please enter a whole number between 1 and 25 for your key: ")
			if key in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']:
				break
			else:
				print("Must be between 0 and 25")
		alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
		key = int(key)
		secretmsg2 = ""

		for letter in message:
			if letter in alpha:
				letter_index = alpha.find(letter) - key
				if letter_index>25:
					letter_index=letter_index-26
				secretmsg2 = secretmsg2 + alpha[letter_index]
			else:
				secretmsg2 = secretmsg2 + letter

		print()
		print("Your original message was: " + message)
		print("Your selected key was: " , key)
		print("Your decrypted message is: " + secretmsg2)
		print()
		menu()	
		
	#This sections decrypts messages with Reverse, Caesar, and Brute Force decryption:		
	elif method2 == "3":
		SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
		reverse_message = message[::-1]
		print()
		print('All possible decrypted messages are listed. Please look for the decrypted message (it will be readable)')
		print("Your original message was: " + message)
		print("This is your message using reverse decryption: " + reverse_message)
		print()
		print("The following is the result utilizing caesar decryption with brute force:")
		

	for key in range(len(SYMBOLS)):
		translated = ''
	
		for symbol in message:
			if symbol in SYMBOLS:
				symbolIndex = SYMBOLS.find(symbol)
				translatedIndex = symbolIndex - key

				if translatedIndex < 0:
					translatedIndex = translatedIndex + len(SYMBOLS)
				translated = translated + SYMBOLS[translatedIndex]
			else:
				translated = translated + symbol

		print('Key #%s: %s' % (key, translated))
	print()
	menu()		
		
#This section stores the goodbye function, which thanks the user and exits the program:
def goodbye():
	print ("Thank you for utilizing this program.")
	sys.exit()
	
#This section gives the option to exit or restart the program:
def tryagain():
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
		menu()
		
#This section stores the main menu as a function:		
def menu():
	print("Main Menu:")
	dash = '-' * 30
	print (dash)
	print ("1. Encrypt message")
	print()
	print ("2. Decrypt message")
	print()
	print ("3. Quit program")
	print()
	while True:
		choice = input("Please enter a number to select a menu option(1,2,or 3): ")
		if choice in ['1','2','3']:
			break
		else:
			print()
			print ("Invalid option. Please enter 1,2,or 3.")
	print()
	if choice== "1":
		encrypt()
	elif choice== "2":
		decrypt()
	elif choice== "3":
		goodbye()

#This is where the program begins:	
print("Welcome! This program encrypts and decrypt messages.")
print()
menu()
