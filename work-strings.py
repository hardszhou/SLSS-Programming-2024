# Strings Assignment
# Author: Hardy Zhou
# Date: 12 February 2024

# 1. Greets the user
print()
print("Hello!")
print()

# 2. Asks the user's name
print("What is your name?")
print()
user_name = input()
print()
print(f"It is very nice to meet you {user_name}!")
print()

# 3. Asks them 3 questions / Responds specifically to those questions
print()
user_input = input("I want to get to know you better. Could I ask you some questions down below, yes or no?\n\n").lower() 
print()
if user_input == "yes":
    print()
    print("Alright.")
else:
    print()
    print("Well too bad...")

print()
print("|")
print("V")
print()
user_input = input("So, was your day good or bad so far?\n\n").lower()
if user_input == "good":
    print()
    print("That is good to hear!")
else:
    print()
    print("Aw, I hope it gets better!")
print()
print()

print("Moving on,")
print()
print("What is your favourite sport?")
print()
sport = input()
print()
print(f"I see, I enjoy {sport} as well!")

print()
print()
print("Lastly,")
print()
print("What is a song you enjoy listening to?")
print()
song = input()
print()
print(f"That is a good choice! I like {song} too!")

# 5. Says goodbye using the user's name
print()
print()
print(f"Well, it was nice talking with you {user_name}. Goodbye!")
print()