# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word=input("Hello, pick a word and type it in for me.")
repeat=int(input("How many times would you like this word repeated?"))
print (word*repeat)
#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name=input("Hello user, what is your name?")
age=int(input((name)+", how old are turning this year?"))
year= 2025-age
print("You must have been born in the year:", (year))
#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence=input("Please give me a sentence.")
word=input("Please give me a word to search for.")
found= word in sentence
print(found)
#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word2=input("Please give me a word.")
index1=int(input("Please give me a first letter from your word."))
index2=int(input("Please give me a letter from ladder half of your word."))
sliced=word2[index1:index2]
print("Sliced word:", (sliced))
#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
w1= input("Please give me a word.")
w2=input("Please give me another word.")
w3=input("Please give me and another word.")
print((w1), (w2), (w3), sep="|")
