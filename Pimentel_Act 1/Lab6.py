Name = input("Enter your name:")
print("Are you a member yes or no?")
member = input("Are you a member ")
age = int (input("Enter a age "))

if age < 18:
    if member == "Yes":
        print("Your fee is 450.00")
    else:
        print(" Your fee is 650.00")
elif age >= 18 and age <= 65:
    if member == "Yes":
        print("Your fee is 550.00")
    else:
        print("Your fee is 750.00")
elif age > 65 and age <=120: 
    if member == "Yes":
        print("Your fee is 400.00")
    else:
        print("Your fee is 600.00")