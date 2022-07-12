print("Addition for add")
print("subtraction for sub")
print("Multiplication  for mul")
print("Division for div")
print("Modulus for mod")




num1 = input("Please enter the first number:")
num1 = int(num1)
num2 = input("Please enter the second number:")
num2 = int(num2)
opera = input("Enter your operation:")
opera = str(opera)




if(opera == "add"):
    print("The answer is:", num1 + num2)

elif(opera == "sub"):
    print("The answer is:", num1 - num2)

elif(opera == "mul"):
    print("The answer is:", num1 * num2)

elif(opera == "div"):
    print("The answer is:", num1 / num2)

elif(opera == "mod"):
    print("The answer is:", num1 % num2)

else:
    print("Invalid input")