bill_amount = float(input("What is the the total bill?"))
tip_percentage = int(input("How much would you like to tip?"))
number_of_people = int(input("How many people are splitting the bill?"))
tip_amount = bill_amount * tip_percentage / 100
total_bill = bill_amount + tip_amount
bill_pcp = total_bill/number_of_people
round(bill_pcp, 2)
bill_pcp = "{:.2f}".format(bill_pcp)
print(f"Each person should pay ${bill_pcp}")
