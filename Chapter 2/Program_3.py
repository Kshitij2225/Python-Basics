num = int(input("How Much U got :- "))
if (num>=90):
    print("Yeah! You Got Grade:- A")
elif(num>=80 and num<=90):
    print("Keep It Up!")    # Here AND is an Logical Operator.
elif(num>=70 and num<=80): 
    print("Good! But work smart \n Grade:- C")
elif(num>=40 and num<=70):
    print("You Have to Work Hard + Smart.\n Grade:- D")
else:
    print("Oops! \n Better Luck Next Time!")