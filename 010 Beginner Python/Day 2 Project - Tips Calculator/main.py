#If the bill was $150.00, split between 5 people, with 12% tip. Each person should pay (150.00 / 5) * 1.12 = 33.6 ;Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculatior.")
total=input("What was the total bill?")
total=float(total)
tip = input("What percentage tip would you like to give? 10, 12 or 15?")
tip=int(tip)
total= total*(1+tip/100)
people= int(input("How many people to split the bill?"))
#{:0.2f} .format(number) 
bill= round(float(total/people),2)
mess="{:0.2f}".format(bill)
print(f"Each person should pay: ${mess}.")