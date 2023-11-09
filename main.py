# My Second Project

print("Welcome to my tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 15. 20? "))
people = int(input("How many people to split the bill with? "))
tip_percentage = tip / 100 * bill
total_bill = tip_percentage + bill
bill_per_person = total_bill / people
round_bill = (round(bill_per_person, 2))
Final_amount = "{:.2f}".format(round_bill)
print(f"Each person bill is: ${Final_amount}")


