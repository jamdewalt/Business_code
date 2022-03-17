#Created a string and calculated the length of the string 
word = "misunderstand" 
print(len(word)) 


#Added 'ing' at the end of a string and stored it as a new variable
word = (word) + "ing"
print (word)
print ()


#Created a list containing three items of different data types and printed the contents of the list 
listof = ['Red', True ,3]
print ("The list displays:")
for x in listof:
  print(x)
print()
 
#Created a list of seven integers, then found and printed the sum
numbers = [1,2,3,4,5,6,7]
number_sum = sum(numbers)
print (number_sum)

#Got the smallest number from the list and printed it 
smallest_number = min(numbers)
print(smallest_number)
print()

#Created a tuple with four items of different data types and printed it for my own viewing
data = ("black", False, 3.2, 1)
print (data)


#Created a tuple containing five numbers and printed one item from the tuple with a label saying: "The item in position (whatever index position you choose) is: (the item). 
numbers2=(1,2,3,4,5)
print ("The item in position", numbers2[1], "is",data[0])
