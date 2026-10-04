choosing = False
#Make a program with the functions:

# 1. One function displays the multiplication table of a number

def table():
    number = int(input("Enter number for multiplication table: "))
    column = 0
    for i in range(12):
        column += 1
        answer = number * column
        print(number,"x",column,"=",answer)


# 2. One function displays the sum of all the numbers until the input number.
total = 0
def sumofnubers():
    start = int(input("Start point:"))
    end = int(input("end point:"))

    for i in range(start,end+1):
        total+= i

    print(total)

# 3. Function for area and perimeter of a square
def square():
    side = float(input("Enter the side of the square: "))
    area = side * side
    perimeter = 4 * side
    print("Area of square =", area)
    print("Perimeter of square =", perimeter)


# 4. Function for area and perimeter of a rectangle
def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print("Area of rectangle =", area)
    print("Perimeter of rectangle =", perimeter)


# 5. Function for area and perimeter of a triangle
def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))

    area = 0.5 * base * height
    perimeter = side1 + side2 + side3

    print("Area of triangle =", area)
    print("Perimeter of triangle =", perimeter)


# 6. Function for area and perimeter of a circle
def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius

    print("Area of circle =", area)
    print("Perimeter of circle =", perimeter)


# Depending upon the choice of the user in a while loop, call the appropriate function

while choosing == False:
    func_number = int(input("Which function do you want too use?(1,2,3,4,5,6)"))
    if func_number == 1:
        table()
        choosing = True
    elif func_number == 2:
        table()
        choosing = True
    elif func_number == 3:
        square()
        choosing = True
    elif func_number == 4:
        rectangle()
        choosing = True
    elif func_number == 5:
        triangle()
        choosing = True
    elif func_number == 6:
        circle()
        choosing = True
    else:
        print("Enter a valid number")
        choosing = False