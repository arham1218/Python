print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("5 = Modulus")

num1 = input("Please enter the first number:")
num1 = int(num1)
num2 = input("Please enter the second number:")
num2 = int(num2)
opera = input("Enter your operation number:")
opera = int(opera)




if(opera == 1):
    print("The answer is:", num1 + num2)

elif(opera == 2):
    print("The answer is:", num1 - num2)

elif(opera == 3):
    print("The answer is:", num1 * num2)

elif(opera == 4):
    print("The answer is:", num1 / num2)

elif(opera == 5):
    print("The answer is:", num1 % num2)

else:
    print("Invalid input")