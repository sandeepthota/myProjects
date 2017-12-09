for n in range(99,-1,-1):
    if n == 1:
        print("{} bottle of beer on the wall, {} bottle of beer.".format(n, n))
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    elif n == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        print ("{} bottles of beer on the wall, {} bottles of beer.".format(n,n))
        print ("Take one down and pass it around, {} bottles of beer on the wall.".format(n-1))
    print ()