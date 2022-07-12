number1 = input("Please enter your number:")
number1 = int(number1)

if(number1 >= 0 and number1 <= 1000):
    if(number1 % 2 == 0):
        print("Divisible by 2")
    if(number1 % 3 == 0):
        print("Divisible by 3")
    if(number1 % 4 == 0):
        print("Divisible by 4")
    if(number1 % 5 == 0):
        print("Divisible by 5")
    if(number1 % 6 == 0):
        print("Divisible by 6")
    if(number1 % 7 == 0):
        print("Divisible by 7")
    if(number1 % 8 == 0):
        print("Divisible by 8")
    if(number1 % 9 == 0):
        print("Divisible by 9")
else:
    print("Invalid input")
    
    
