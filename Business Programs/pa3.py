# Overview:This program calculates and/or reports different winter weather conditions for Madison, Wisconsin.

#This section stores import functions
import sys
import os

#This section stores the restart program function:
def restart_program():

    print ()
    python = sys.executable
    os.execl(python, python, * sys.argv)

#This section stores the windchill function:	
def windchill():
	while True:
		temp = input("Please enter a temperature in Fahrenheit(°F): ")
		if temp.isdigit():
			break
		else:
			print()
			print("Please retry and enter a number.")
	print()
	while True:	
		wind_speed = input("Please enter a wind speed (mph): ")
		if wind_speed.isdigit():
			break
		else:
			print()
			print("Please retry and enter a number.")
	wind_chill =+ 35.74 + 0.6215 * float(temp) - 35.75 * float(wind_speed) ** 0.16 + 0.4275 * float(temp) * float(wind_speed) ** 0.16
	print()
	dash = '-' * 30
	print (dash)
	print ("The temperature is:", temp, "degrees")
	print ("The wind speed is:", wind_speed, "mph")
	print ("The wind chill is:", round(wind_chill,),"degrees")
	print()
	
#This section stores the precipitation function:
def precipitation():
	months= ("March 2018","April 2018","May 2018","June 2018","July 2018","August 2018","November 2018","October 2018","November 2018","December 2018", "January 2019", "February 2019")
	snowfall=(3.42,13.53,0,0,0,0,0,0,3.42,2.05,19.68,22.41)
	print("Monthly Precipitation (in.) for March, 2018 through February, 2019")
	dash = '-' * 55
	print(dash)
	print ("Month/Year:", '\t\t', "Monthly Precipitation Amount(in.):")
	print (dash)
	for days in range(len(months)):
		if len(months[days]) < 7 :
			print(months[days] , '\t' , snowfall[days])
		else:
			print(months[days] , '\t\t' , snowfall[days])
	print()
	
#This section stores the temperature function:	
def temperature():
	months= ("March 2018","April 2018","May 2018","June 2018","July 2018","August 2018","November 2018","October 2018","November 2018","December 2018", "January 2019", "February 2019")
	average_temp =(32.8,37.65,64.55,69.2,72.3,71.5,63.65,47.75,31,28.4,15.95,18.85)

	print("Average Monthly Temperatures (°F) for March, 2018 through February, 2019")
	dash = '-' * 45
	print(dash)
	print ("Month/Year:", '\t\t', "Average Monthly Temp(°F):")
	print (dash)
	for days in range(len(months)):
		if len(months[days]) < 7 :
			print(months[days] , '\t' , average_temp[days])
		else:
			print(months[days] , '\t\t' , average_temp[days])
	print()
	
#This section stores the goodbye function, which thanks the user and exits:
def goodbye():
	print ("Thank you for utilizing this program.")
	sys.exit()
	
	

#This is where the program begins:	
print("Welcome! This program displays weather conditions for Madison, Wisconsin.")
print()
print ("1. Calculate wind chill based on air temperature and wind speed measurements")
print()
print ("2. See total monthly precipitation for March, 2018 through February, 2019")
print()
print ("3. See average monthly temperatures for March, 2018 through February, 2019")
print()
print ("4. Quit program")
print()

while True:
	choice = input("Please enter a number to select a menu option(1,2,3, or 4): ")
	if choice in ['1','2','3','4']:
		break
	else:
		print ("Invalid option. Please enter 1,2,3, or 4.")
print()
if choice== "1":
	windchill()
elif choice== "2":
	precipitation()
elif choice== "3":
	temperature()
elif choice== "4":
	goodbye()

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
	restart_program()
	
	
