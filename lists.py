student=["karan",89,"delhi"]
print(student[0])
student[0]="Daksh"#changement is aplicable that a string cant 
print(student[0])
#slicing is also posible as string can
marks=[89,90]
#list.append adds one element at the end
marks.append(45)
print(marks)
marks.sort()#arrange list in ascending order
print(marks)
marks.sort(reverse=True)#arrange in reverse order
print(marks)
marks.reverse()#reverse the given order
print(marks)
marks.insert(2,1)#insert element at any particular index
print(marks)
marks.remove(45)#removes first occurence of element
print(marks)
marks.pop(2)#removes particular index
print(marks)
print(sum(marks))#it gives us the sum  all the elments in  the list 