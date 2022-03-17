#This program displays a list of students with their test scores. It also shows the highest, lowest, and average scoes.
student_name= ['Marie', 'Andrew', 'Saran', 'Antonio', 'Taylor', 'Cesar', 'Willa', 'Robert']     
test_score= ['89','45','96', '99', '67', '84', '39', '50']

#This displays the students name and accompanying test score
print ("Student names and test scores:")
print()
for name,score in zip(student_name,test_score):
    print (name + '\t' + score)
print()

#This calculates the highest, lowest, and average score by storing each as a variable
scores= [89,45,96,99,67,84,39,50]
best_score= max(scores)
worst_score= min(scores)
average_score = sum(scores)/8

#This displays the highest, lowest, and average score
print ("The highest score is:", best_score)
print ("The lowest score is:", worst_score)
print ("The class average is", round(average_score,))


