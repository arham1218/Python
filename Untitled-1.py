
mark =  input("Please enter your mark:")
mark = int(mark)
if(mark >= 0 and mark <= 100):
    if(mark >= 90 and mark <= 100):
        print("You get an A")
    elif (mark >= 80 and mark <= 89):
        print("You get a B")
    elif (mark >= 70 and mark <= 79):
        print("You get a C")
    elif (mark >= 60 and mark <= 69):
        print("You get a D")
    else:
        print("You get a F")
else:
    print("Invalid input")    



     


