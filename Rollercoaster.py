print("welcome to the Rollercoaster!")
height = int(input("what is your height in cm? "))
age = int(input("what is your age? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 10:
        bill = 10
        # print("you will pay $10")
    elif age <= 18:
        bill = 15
        # print("you will pay $15")
    elif age > 18:
        bill = 20
        # print("you are mature enough tp pay $20")
    want_picture = input("Do you want a picture Ticket? Y or N. ")
    if want_picture == "Y":
        bill += 3
        print(f"Your final bill ticket is ${bill}")

else:
    print("Sorry!you have to grow taller to be able to ride")