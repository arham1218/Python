a = [1, 3, 4, 16, 4, 8, 20, 9, 7]

b = len(a)

for i in range(b):
    a[i] = a[i] * a[i]
    
a.sort()
a.pop(-1)
print(a)

