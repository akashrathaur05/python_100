print("WELCOME TO ROLLERCOASTER! THERE ARE SOME RULES TO ENJOY RIDE")
age = int(input("Enter your age : "))
height = int(input("Enter your height : "))
if height <= 120:
    print("Your height is not elegible for ride!")
else:
    print("You are elegible ride")
    if age <= 18:
        print("please pay 7$")
    else:
        print("please pay 8$")