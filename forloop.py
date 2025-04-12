num=[1,4,9,16,25,36,49,64,81,100]
x=int(input("which element do you want to search"))
indx=0
for value in num:
    if(x==value):
        print("the element is found",indx)
        break
    indx+=1
    