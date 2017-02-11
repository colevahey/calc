import math

def pythagorean():
    print("You chose pythagorean theorum")
    hyp = input("Do you have your hypotenuse[Y/N]? >> ")
    if hyp.title() == 'Y':
        a = input("What is the hypotenuse? >> ")
        b = input("What is the other side? >> ")
        if int(a) < int(b):
            print("That is impossible")
            input("[Press enter to continue]")
            pythagorean()
        else:
            final = (float(a)*float(a))-(float(b)*float(b))
            finalside = math.sqrt(final)
    elif hyp.title() == 'N':
        a = input("What is your first side? >> ")
        b = input("What is your second side? >> ")
        final = (float(a)*float(a))+(float(b)*float(b))
        finalside = math.sqrt(final)
    else:
        pythagorean()
    print("Your final side is " + str(finalside))
