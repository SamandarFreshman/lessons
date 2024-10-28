a,b,c=map(int,input("Enter 3 numbers her(a b c):").split())
if a<b:
    if c<b:
        print("The largest number is",b)
    else:
        print("The largest number is",c)
    if a<c:
        print("The smallest number is",a)
    else:
        print("The smallest number is",c)
else:
    if c<a:
        print("The largest number is",a)
    else:
        print("The largest number is",c)
    if b<c:
        print("The smallest number is",b)
    else:
        print("The smallest number is",c)