#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it. Write a Python script that reads a file gardening.tips.txt and prints out each tip one by one.
#I'm not sure why this won't open up any of the text files. I tried moving the text file to several different locations/ folderes along with the mu program and it still wont work.
def gardening_tips():
    open("gardening_tips.txt", "r") as file:   #"r" = read
    content = file.read()   #reads file as string
    print(content)  #print txt
    file.close()    #close file(s))
#2. Write a Python program that allows users to log their hiking trips. The program should: Use a while loop to repeatedly ask for a hike name and distance in miles,
#Save each entry to hiking_log.txt (each hike on a new line), When the user presses 0, exit the loop & print the contents of hiking_log.txt
def log_hiking_trip():
    with open("hiking_log.txt", "a") as file:  # Open file via append
        while True:
            hike_name = input("Enter the name of the hike (or '0' to exit): ")
            if hike_name == "0":
                break  # Exit loop
            try:
                distance = float(input(f"Enter the distance of {hike_name} in miles: "))
                file.write(f"{hike_name}: {distance} miles\n")
            except ValueError:
                print("Please enter a number for the distance.")
        print("\nHiking Log Contents:") # After exiting loop, print the contents of the log file
        with open("hiking_log.txt", "r") as file_read:
            contents = file_read.read()
            print(contents)
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that: Reads the file,
# Requests 5 inputs from the user: 5 words the user would like to count the, frequency of: Counts how many times each word appears, Creates a dictionary of the words and their counts,
#Print the dictionary to the console
def song_lyrics():
    with open("song_lyrics.txt", "r") as file:
        content = file.read().lower()  # Read content & lowercase for easier word-search
    words_to_count = {}
    for _ in range(5):
        word = input("Enter a word to count its frequency: ").lower()  # Lowercase input
        words_to_count[word] = content.split().count(word)  # Count the word(s)
    print("\nWord frequencies:")
    for word, count in words_to_count.items():
        print(f"'{word}': {count} times")
song_lyric()
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas. Write a program that reads the poll.txt file
#Count how many votes "yea" or "nay" received and print the results.
def poll_results():
    with open("poll.txt", "r") as file:
        votes = file.read().strip()
    vote_list = votes.split(",")    # Split the votes by commas
    yea_count = vote_list.count("yea")
    nay_count = vote_list.count("nay")
    print(f"Yea votes: {yea_count}")
    print(f"Nay votes: {nay_count}")
poll_results()
