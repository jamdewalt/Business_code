#this program stores my favorites pizzas and printe them for the user

pizzas = ["cheese", "spinach", "buffalo chicken"]

#printing items from the list
for pizza in pizzas:
	print("I like eating " + pizza + " pizza.")

print("\n Actually, I don't really eat a lot of pizza")	
print()
print()
	
#printing items from the list
for i in range(len(pizzas)):
	print("I like eating " + pizzas[i] + " pizza.")

print("\n Actually, I don't really eat a lot of pizza")	

print()
print()
pops = ["Sprite", "Strawberry Crush", "Pepsi"]
for i in range(len(pizzas)):
	print("When I eat " + pizzas[i] + " pizza, I drink " + pops[i] + ".")

print()
print()
print("Pizza Type\t\tPop")
print()
for i in range(len(pizzas)):
	print(pizzas[i].title() + "\t\t\t" + pops[i].title()) #to get rid of the extra tab at the end, use an if statement
	
	
	
	
