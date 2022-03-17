# This program calculates the area of a trapezoid or a triangle.

# This tells the user the programs function
print('This program finds the area of a trapezoid or a triangle.\n')

#This lets the user decide which area they wish to find, area or trapezoid, by entering 1 or 2. Anything else will restart the program.
def triortrap():

    question = input('Please enter 1 to find the area of a trapezoid or 2 to find the area of a triangle: ')
    question1 = int(question)
#This lets the user find the area of a trapezoid. They input two base variables and one height varible. These are then converted into floats. Finally the variables are used in a calculation to find the area. A print statement displays the area    
    if question1 == 1:

        print('This program finds the area of a trapezoid.')
        height = input('Please enter the height of the trapezoid: ')
        base = input('Please enter a base length of the trapezoid: ')
        base2 = input('Please enter another base length of the trapezoid: ')
        height = float(height)
        base = float(base)
        base2 = float(base2)
        area = (base + base2)/2 * height
        print('The area of a trapezoid with height', height, 'and the bases', base, 'and', base2, 'is', area,  '.')
       
#This lets the user find the area of a triangle. They input one base variable and one height varible. These are then converted into floats. Finally the variables are used in a calculation to find the area.A print statement displays the area        
    elif question1 == 2:

        print('This program finds the area of a triangle.')
        height = input('Please enter the height of the triangle: ')
        base = input('Please enter the base length of the triangle: ')
        height = float(height)
        base = float(base)
        area = 0.5 * height * base
        print('The area of a triangle with height', height, 'and base', base, 'is', area, '.')
       
#This restarts the program if they enter something besides 1 or 2
    else:

        print('Please try again.')
        triortrap()
triortrap()
