print("welcome to the Rollercoaster!")
height = int(input("what is your height in cm? "))
age = int(input("what is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 10:
        print("you will pay $10")
    elif age <= 18:
        print("you will pay $15")
    elif age > 18:
        print("you are mature enough tp pay $$$$$")

else:
    print("Sorry!you have to grow taller to be able to ride")