#This program uses a reverse cipher to encrypt and decrypt a message

# This asks for their message
msg =input("Please enter a message: ")

#reverses message using index navigation
reverse_msg = msg[::-1]

#reverses using a while loop
i = len(msg)-1
reverse_msg2=""
while i >=0:
	reverse_msg2 = reverse_msg2+ msg[i]
	i = i-1
 
print()
print("This is your original message: " + msg)
print("This is your reverse encrypted message using [::-1]: " + reverse_msg)
print("This is your reverse encrypted message using a while loop: " + reverse_msg2)
