#checking alien color to asign points

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
age = input("Please enter an age?")
age = int(age)
print()
if age<2:
	print("That person is a baby.")
if 2<=age<4:
	print("That person is a toddler.")
if 4<=age<13:
	print("That person is a kid.")
if 13<=age<20:
	print("That person is a teenager.")
if 20<=age<65:
	print("That person is an adult.")
if age>65:
	print("That person is an elder.")
