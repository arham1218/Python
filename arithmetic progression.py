num1 = input("Please enter the first term: ")
num1 = int(num1)
num2 = input("Please enter the last term: ")
num2 = int(num2)
num3 = input("Please enter the common difference: ")
num3 = int(num3)
sum = 0
for i in range(num1,num2 + 1 ,num3):
    sum = sum + i
    
print(sum)
