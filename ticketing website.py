name = []
age = []
gender = []
weight = []
for i in range(4):
    name.append(input("Please enter your name: "))
    name[i] = str(name[i])
    age.append(input("Please enter your age: "))
    age[i] = int(age[i])
    gender.append(input("Please enter your gender: "))
    gender[i] = str(gender[i])
    weight.append(input("Please enter your weight: "))
    weight[i] = float(weight[i])
    
    if(age[i] < 12 or age[i] > 70):
        print("Sorry, you are not eligible")
    else:
        ticket_price = age[i] * 1.8 + weight[i] * 1.2
        print("Your ticket price is", ticket_price)


   


print(name)
print(age)
print(gender)
print(weight)


