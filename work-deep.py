# Exercise - Conditionals
# Author: Hardy
# 20 February 2024

print()
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n\n")
print()

if answer == "42":
    print("Yes")
elif answer.lower() == "forty-two" or answer.lower() == "forty two":
    print("Yes")
else:
    print("No")
print()