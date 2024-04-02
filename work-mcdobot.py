# Exercise - McDoBot
# Author: Hardy
# 21 February 2024

print()
user_reply = input("Would you like fries with your meal? Yes or No?\n\n")

print()
if user_reply.strip(" !.?,").lower() == "yes":
    print("Here is your meal with fries!\n")
elif user_reply.strip(" !.?,").lower() == "no":
    print("Here is your meal without fries!\n")
else:
    print(f"Sorry, I didn't understand {user_reply}...\n")