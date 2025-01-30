#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)
# A          B      (A AND B)   (NOT B)    (A AND B) OR (NOT B)
# -----------------------------------------------
# True      True      True       False           True
# True      False     False      True            True
# False     True      False      False           False
# False     False     False      True            True
#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
anws= int(input("How bright is it on a scale of 0-10? (0 being dark, 10 being bright.)"))
if anws <= 8:
    print("Headlights on!")
else:
    print("Headlights off.")
#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.
balance= int(input("Hello, what is your bank balance?"))
if balance < 100:
    print ("true")
else:
    print ("false")
#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age= int(input("Hello, how old are you?"))
if age < 13:
    print("You may see G-rated movies")
elif 13 <= age <= 17:
    print("You may see G-rated or PG-13-rated movies")
else:
    print("You may see G-rated, PG-13-rated, or R-rated movies")
#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.
order= int(input("Hello, what was the amount of your order?"))
if order >= 50:
    print("You spent $50 or more so your shipping is free!")
    print("The total is: $",order)
else:
    print("You spent under $50 so your total (including shipping) is:")
    print("$", order+5)
