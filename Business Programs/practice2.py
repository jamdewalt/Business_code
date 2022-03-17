#checking alien color to assign points

 

alien_color = "green"

if alien_color == "green":

                print("Your alien was " + alien_color + ". You earned 5 points.")

else:

                print("Your alien was " + alien_color + ". You earned 0 points.")

                               

alien_color = "yellow"

if alien_color == "yellow":

                print("Your alien was " + alien_color + ". You earned 10 points.")

else:

                print("Your alien was " + alien_color + ". You earned 0 points.")

               

alien_color = "red"

if alien_color == "red":

                print("Your alien was " + alien_color + ". You earned 15 points.")

else:

                print("Your alien was " + alien_color + ". You earned 0 points.")

print()

print()

#This program helps determine a person's stage of life
while True:
	age = input("Please enter an age?")
	try:
		age = int(age)
		break
	except:
		print("Please use a number.")
	

print()

if age<2:

                print("That person is a baby.")

elif 2<=age<4:

                print("That person is a toddler.")

elif 4<=age<13:

                print("That person is a kid.")

elif 13<=age<20:

                print("That person is a teenager.")

elif 20<=age<65:

                print("That person is an adult.")

else:

                print("That person is an elder.")
 
