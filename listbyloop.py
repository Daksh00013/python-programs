num=[1,4,9,16,25,36,49,64,81,100]
x=int(input("which item do you want to search"))
i=0
while i<=9:
    if(num[i]==x):
            print("the item is found at inex",i)
    i+=1