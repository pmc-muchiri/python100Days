print("welcome to the tip calculator")
bill = float(input("What was the total bill?: $"))
percentage_tip = float(input("what percentage tip would you like to give? 10, 12 or 15?: "))
people = int(input("How many people to split the bill?: "))

bill_percent = bill * (percentage_tip/100)
total_bill = bill_percent + bill
bill_person = round(total_bill/people, 2)

print(f"Each person to pay: ${bill_person}")
