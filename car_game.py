comment=input(">")
comment.upper()
if comment=="HELP":
    print("""start - to start the car
stop - to stop the car
quit - to exit """)
else:
    print("write a valid code to strt the game")
x= input(">")
if(x=="start"):
    print("Car started.... Ready to Go! ")
elif(x=="stop"):
    print("Car stopped!")
elif(x=="quit"):
    print("you exit form the game succesfully.....")
else:
    print("I don't understand")
    
    