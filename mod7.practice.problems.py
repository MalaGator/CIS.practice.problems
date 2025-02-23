#1. Write a function called count_vowels(input) that takes a string
#and returns the number of vowels (a, e, i, o, u) in it.
#test string: Leafeon is the best Eeveelution. (14) make every word uniform. define the vowels & count them from a string. return count & print count
#def count_vowels(t):
#    lower_t = t.lower()
#    vowels = "aeiou"
#    count = 0
#    for char in lower_t:
#        if char in vowels:  # Check if the character is a vowel
#            count += 1
#    return count
#result = count_vowels("Leafeon is the best Eeveelution")
#print(result)
def count_vowels(t):
    lower_t = t.lower()
    vowels = "aeiou"
    count = 0
    for char in lower_t:
        if char in vowels:
            count += 1
    return count
user_input = input("Please give a string: ")
result = count_vowels(user_input)
print("The number of vowels in your string is:", result)
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome (reads the same forward and backward, ignoring case). The function should
#returns either True or False.
#test strings: Racecar, Eevee, leafeon. Make everything uniform (lowercase). define, lowercase, flip, return output, print results T/F
def is_palindrome(s):
    lower_s = s.lower()
    flip_s = lower_s[::-1]
    return lower_s == flip_s
print(is_palindrome("Racecar"))
print(is_palindrome("Eevee"))
print(is_palindrome("leafeon"),'\n')
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types. Write a function called type_advantage(attacker, defender) that takes two, Pokémon types as
#strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on simple type effectiveness rules. Your solution only needs to work for these three sets of input:
#print(type_advantage("Water", "Fire")) # "Super Effective", print(type_advantage("Fire", "Water")) # "Not Very Effective", print(type_advantage("Electric", "Grass")) # "Neutral
#I over thought this one and was writing all of the different pokemon types until I reread this...
#test if water+fire= super effetive, fire+water= not very effetive, electric+grass= neutral,& anything else neutral. make it uniform w/ lowercase so there is no errors.
#repeat so its easier to test, break w/0
def type_advantage(attacker, defender):
    attacker = attacker.lower()
    defender = defender.lower()
    if attacker == "water" and defender == "fire":
        return "Super Effective\n"
    elif attacker == "fire" and defender == "water":
        return "Not Very Effective\n"
    elif attacker == "electric" and defender == "grass":
        return "Neutral\n"
    else:
        return "Neutral\n"
while True:
    attacker_type = input("Enter your attacker's type (or '0' to quit): ")
    if attacker_type == "0":
        break
    defender_type = input("Enter your defender's type (or '0' to quit): ")
    if defender_type == "0":
        break
    result = type_advantage(attacker_type, defender_type)
    print("The effectiveness of the attack is:", result)
print("Exiting, onto the next practice problem.")
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry farebased on age and whether the person has a vehicle. Assume the following rates:
#* Adults (19-64): $10 without a vehicle, $20 with a vehicle. * Seniors (65+): $5 without a vehicle, $15 with a vehicle. * Children (0-18): Free.
#find the age of peoples, that'll determine the whether there is a car or not, then add the fee of person (and vehicle)
def ferry_fare(age, vehicle):
    if age >= 0 and age <= 18:
        return 0
    elif age >= 65:
        if vehicle:
            return 15
        else:
            return 5
    elif age >= 19 and age <= 64:
        if vehicle:
            return 20
        else:
            return 10
age = int(input("Please enter your age: "))
if age > 18:
    vehicle = input("Do you have a vehicle? (yes/no): ").strip().lower()
    vehicle = vehicle == "yes"
else:
    vehicle = False
fare = ferry_fare(age, vehicle)
print("The ferry fare is: $",(fare))
#5. Write a function called level_up(experience) that takes a player's experience points and returns their new level based on these rules:
#* 0-99 XP → Level 1, * 100-199 XP → Level 2, * 200+ XP → Level 3
#ask the user their exp. if its 200+ then lv3, if its 100<=200 then lv2, that should only leave 99=>.
def level_up(experience):
    if experience >= 200:
        return 3
    elif experience >= 100:
        return 2
    else:
        return 1
exp_points = int(input("Enter your experience points: "))
new_level = level_up(exp_points)
print("Your new level is:",(new_level))
