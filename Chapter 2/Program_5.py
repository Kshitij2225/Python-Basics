a = int(input("Enter First Number :- "))
b = int(input("Enter Second Number :-"))
c = int(input("Enter Third Number :-"))
d= int(input("Enter Fourth Number :-"))

if(a>b and a>c and a>d):
    print("A is Greatest")
elif(b>a and b>c and b>d):
    print("B is Greatest")
elif(c>a and c>b and b>d):
    print("C is Greatest")
elif(d>a and d>b and d>c):
    print("D is Greatest")
else:
    print("Get Lost!")
