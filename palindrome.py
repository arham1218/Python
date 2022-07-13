var1 = input("Please enter your string: ")
var1 = str(var1)
var1 = var1.lower()
var2 = var1[::-1]
if(var2 == var1):
    print("It is palindrome")
else:
    print("It is not palindrome")


