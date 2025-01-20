#1
print ("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
#I love the last air bender so much!!

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
import math
num1 = int(input("Give me a number please. (I will be adding, subtracting, multipling, and dividing them with each other.)"))
num2 = int(input("And another number."))
print (num1+num2, num1-num2, num1*num2, num1/num2)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
num3 = int(input("We're going to find the area of a Triangle, please give a side length."))
num4 = int(input("Okay, now another side."))
num5 = int(input("And the final side."))
semi = ((num3+num4+num5)*.5)
A= int, input(math.sqrt(semi*(semi-num3)*(semi-num4)*(semi-num5)))

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import statistics
num6 = int(input("Please give five numbers one at a time."))
num7 = int(input("Another one."))
num8 = int(input("another one."))
num9 = int(input("another one."))
numa = int(input("another."))
#please tell me there is an easier way of what is above :(
total = (num6+num7+num8+num9+numa)
print (("This is the total of the numbers given:"), total)
averag3 = ((num6+num7+num8+num9+numa)/5)
print (("This is the average of the numbers given:"),averag3)
min_value = min(num6, num7, num8, num9, numa)
print(("The minimum value of this list is:"), min_value)
max_value = max(num6, num7, num8, num9, numa)
print(("The maxiam vaule of this list is:"), max_value)
range = max_value - min_value
print ("This is the range of theses numbers:",range)
#I got everything else to function I just couldn't figure out standard deviation, please help me out.
#def calculate_std_dev(num6, num7, num8, num9, numa):
#deviations = [(x - averag3)**2 for stan in (num6, num7, num8, num9, numa_)]
#variance = sum(deviations) / (5 - 1)
#return variance ** 0.5
