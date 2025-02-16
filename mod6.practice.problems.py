#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
list1= input("Give a list of numbers separated with commas: ")
nums= [int(num) for num in list1.split(',')]
even_sum = 0
for num in nums:
    if num % 2 == 0:
        even_sum += num
print("The sum of the even numbers:", even_sum, end="\n\n")
#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
list2= input("Please give a few sentences with the word 'Olympic' in them seperated by commas:")
strings = [s.strip() for s in list2.split(',')]
olympic_count = 0
for string in strings:
    olympic_count += string.lower().count("olympic")
print("The word 'Olympic' appears", olympic_count, "times.", end="\n\n")
#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
list3= input("Please give a few items in a list seperated by commas:")
string= [s.strip() for s in list3.split(',')]
filtered_strings= [s for s in strings if len(s) > 3]
print("Theses strings/items are longer than three characters: ", filtered_strings, end="\n\n")
#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
nums= [6, 4, -3, -7, 2, -8, 0, 10]
pos_count = 0
neg_count = 0
for num in nums:
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
print("The positive numbers:", pos_count)
print("The negative numbers:", neg_count, end="\n\n")
#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
nums= [1, 2, 3, 4, 5]
square_nums = []
for num in nums:
    square_nums.append(num ** 2)
print("Squared numbers:", square_nums)
