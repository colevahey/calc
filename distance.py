import math

def distance():
    print("You chose Distance Formula")
    point1x = input("What is the X value of your first point? >> ")
    point1y = input("What is the Y value of your first point? >> ")
    point2x = input("What is the X value of your second point? >> ")
    point2y = input("What is the Y value of your second point? >> ")
    a = int(point1x) - int(point2x)
    b = int(point1y) - int(point2y)
    asquared = a*a
    bsquared = b*b
    answer = math.sqrt(asquared + bsquared)
    print("The distance between your two points is " + str(answer) + " units")
