class Traingle(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def isTraingle(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.c + self.b > self.a)

    def isPythogorean(self):
        sides = [self.a,self.b,self.c]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2

if __name__ == "__main__":
    while True:
        sides = []
        n = 0
        while n<3:
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
        Tri = Traingle(*sides)
        if (Tri.isTraingle()):
            if (Tri.isPythogorean()):
                print ("Yess!! It is a pythogerean Triplet")
            else:
                print ("Not a pythogerean triplet")
        else:
            print("A triangle cannot be formed with the given sides")
            continue
        user_reply = input("Thanks for playing! Do you want to try again?")
        if user_reply == "yes":
            continue
        else:
            break
