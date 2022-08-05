def intro(name, age, gender):

    name = str(name)
    age = int(age)
    gender = str(gender)
    if(age < 18 or age > 60):

        return "sorry you're not eligible"
    
    else:
        if(gender == "male"):

            print("Welcome aboard, Mr. ", name)

        else:

            print("Welcome aboard, Ms. ", name)





        


a = intro("arham", 45, "male")

print(a)