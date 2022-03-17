#This program displays rainfall and snowfall information for LaCrosse, Wisconsin for the month of February 2019.

#These two tuple lists store the day of the month and snowfall data.
feb = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28)
snowfall = (0.2,0,0,0,0,0.5,0.3,3,0,0,1.4,7.6,3.4,0,0.2,0,0.4,4.3,0,2,3.6,0,0.5,2.5,0,0,1.3,0)

#This is for decoration only. Used to put dashes in between lines to make the columns look better.
dash = '-' * 80

#This converts snowfall to rainfall and stores it as a variable.
rainfall_conversion = 10
rainfall = [x / rainfall_conversion for x in snowfall]

#This stores a goodbye message to be used at the end of each option. This is primarily for ease of access.
goodbye = ("Thank you for using this system. Please restart to perform additional actions.")

#This defines what the average snowfall is and stores it as a variable.
average = sum(snowfall) / len(snowfall)

#This displays the main menu
print("Welcome! This program displays rainfall and snowfall information for LaCrosse, Wisconsin in February 2019.")
print()
print("1. Display daily total snowfalls for February, 2019")
print()
print ("2. Display minimum, maximum, monthly cumulative snowfall, and average snowfall for February, 2019")
print()
print("3. Calculate snowfall to rain conversion for February, 2019 and display daily and monthly totals")
print()

#This lets the user decide on an option (1, 2 or 3) or else tells them to try again using the correct format.
choice = input("Please enter a number to select a menu option(1,2 or 3): ")
print()
if  choice == "1":
	print(dash)
	print ("Daily Total Snowfalls for LaCrosse, Wisconsin in February 2019")
	print (dash)
	print ("Day of Month:", '\t', "Daily Total Snowfall Amount(in.):")
	for days,total in zip(feb,snowfall):
		print (days , '\t\t' , total)
	print()
	print (goodbye)
elif choice == "2":
	print(dash)
	print("Snowfall metrics (in.) for LaCrosse, Wisconsin in February 2019")
	print(dash)
	print("The minimum daily snowfall is: ", '\t', min(snowfall))
	print("The maximum daily snowfall is: ", '\t', max(snowfall))
	print("The average daily snowfall is: ", '\t',round(average, 1))
	print("The total cumulative snowfall is:", '\t', sum(snowfall))
	print()
	print(goodbye)
elif choice== "3":
	print(dash)
	print ("Daily Total Snowfalls for LaCrosse, Wisconsin in February 2019")
	print()
	print ("To convert snowfall total to rainfall total, divide the snowfall total by 10.")
	print ("This table shows the daily snow to rain conversion:")
	print (dash)
	print ("Day of Month:", '\t', "Daily Total Snowfall Amount(in.):", '\t', "Daily Total Rainfall Amount(in.):")
	for days,total,rain in zip(feb,snowfall,rainfall):
		print (days , '\t\t' , total, '\t\t\t\t\t' ,round(rain,2))
	print()
	print (goodbye)
#This dipslays an error message if the user doesn't input 1, 2 or 3.
else:
	print ()
	print("Sorry. You entered the following:" +(choice)+ ". Please enter one of the following numbers to select your choice (1,2,or 3)")
	print()	





