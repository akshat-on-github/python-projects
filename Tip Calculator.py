print("welcome to tip calculator")
bill = float(input("what was the total bill?"))
tip = float(input("how much tip would you like to give? 10 , 12 or 15?"))
people = int(input("how many people to split the bill?"))
bill_with_tip = bill * (tip/100)
total_bill = bill + bill_with_tip
bill_per_person =  total_bill/people
final_amount = round(bill_per_person , 2)
print(f"each person should pay {final_amount}")