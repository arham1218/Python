a = [0] * 6 
for i in range(6):
    a[i] = input("Enter the inputs: ")
    a[i] = int(a[i])

for i in range(6):
    if(a[i] % 2 == 0):
        a[i] = a[i]

    else:
        a[i] = a[i] * 2


a.sort(reverse = True )
a.pop(-1)

print(a)

