#This program uses a reverse cipher to encrypt and decrypt a message

# This asks for their message
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

msg =input("Please enter a phrase: ")

while True:
	key = input("Please enter a whole number between 1 and 25 for your key: ")
	if key in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']:
		break
	else:
		print("Must be between 0 and 25")
#if checking for letters, use a try statement

#reverses message using index navigation
msg = msg.upper()
key = int(key)
secretmsg = ""

for letter in msg:
	if letter in alpha:
		letter_index = alpha.find(letter) - key
		if letter_index>25:
			letter_index=letter_index-26
		secretmsg = secretmsg + alpha[letter_index]
	else:
		secretmsg = secretmsg + letter

print()
print("Your original message was: " + msg)
print("You secret messagae is: " + secretmsg)

