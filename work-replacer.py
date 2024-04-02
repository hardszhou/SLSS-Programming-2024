# Text/Emoji Replacer
# Author: Hardy
# 26 February 2024

# Create a function called translate
#    Accepts a string as parameter
#    From the parameter replace all 100 with 💯
#    Also replace all noodles with 🍜
#    Return the result
def translate(user_input):
    # Your block of code goes in here
    # Delete the pass and put in your own code
    text = user_input
    text = text.replace("noodle", "🍜").replace("100", "💯")
    return text


def main():
    # Get the user's input
    # Use the translate function on the
    #    user's input
    # Print the results
    user_input = input()
    print(translate(user_input.strip("s").lower().capitalize()))

main()