import math

def quadratics():
    print("You chose quadratics")
    a = input("What is your A value? >> ")
    b = input("What is your B value? >> ")
    c = input("What is your C value? >> ")
    aos = 0 - int(b)/(2*int(a))
    this = float(a)*float(aos)*float(aos)
    that = float(b)*float(aos)
    thus = float(c)
    yvertex = (float(a)*float(aos)*float(aos)) + (float(b)*float(aos)) + float(c)
    begin = -1*float(b)
    middle = float(b)*float(b)
    end = 4*float(a)*float(c)
    squareroot = middle - end
    final = 2*float(a)
    print("The y intercept is " + str(c))
    print("The axis of symmetry is " + str(aos))
    print("The vertex is (" + str(aos) + "," + str(yvertex) + ")")
    if int(b)*int(b) > 4*int(a)*int(c):
        root1 = (begin + math.sqrt(squareroot))/final
        root2 = (begin - math.sqrt(squareroot))/final
        message = "The roots are at " + str(root1) + " and " + str(root2)
    elif squareroot < 0:
        root1 = begin/final
        root2 = begin/final
        imaginary = math.sqrt(-1*squareroot)/final
        message = "The two imaginary roots are at " + str(root1) + "+" + str(imaginary) + "i and " + str(root2) + "-" + str(imaginary) + "i"
    else:
        root = begin/final
        message = "There is only one root and it is at " + str(root)
    print(message)
