def Triangle():
    sides = []
    n = 0
    while True and n<3:
        try:
            userInput = int(input("Enter side "+str(n+1)+" of traingle: "))
        except ValueError:
            print("Please enter an integer!")
            continue
        else:
            if userInput < 1:
                print ("Please input a non-zero positive integer")
                continue
            sides.append(userInput)
        n = len(sides)

    if (isTraingle(*sides)):
        print (isPythogorean(*sides))
    else:
        print ("The sides you entered don't form a traingle")
        Triangle()
    end()

def isTraingle(*args):
    a,b,c = args
    s = (a+b-c) * (a+c-b) * (b+c-a)
    if s > 0.00001:
        return True
    else:
        return False

def isPythogorean(*args):
    a,b,c = args
    sides = [a,b,c]
    maxSide = a
    sumofSideSquares = 0
    for side in sides[1:]:
        if side > maxSide :
            sumofSideSquares += maxSide**2
            maxSide = side
        else:
            sumofSideSquares += side**2
    if (maxSide**2 == sumofSideSquares):
        return "Yess!! Pythogearean triplet"
    else:
        return "Not a pythogerean triplet"

def end():
    print ("Thanks for playing! Do you want to try again?")
    user_reply = input()
    if user_reply == "yes":
        Triangle()

'''
A classic way of asking the user for input, then playing the game again and again

We need not use any exception handling or anything for the input question as it can be anything
'''


print ("Welcome to the triangle game")
Triangle()