N1=int(input("enter the first number:"))
N2=int(input("enter the second number:"))
N3=int(input("enter the third number:"))
if(N1>N2 and N2>N3):
    print("the first no is greatest among all three")
elif(N2>N1 and N1>N3 and N2>N3):
    print("the second no is greatest among all three")
else:
    print("the third no is greatest among all three")


