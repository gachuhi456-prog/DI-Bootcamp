import random

# 1. Ask for User Input
user_input = input("Please enter a string that is exactly 10 characters long: ")

# 2. Check the Length of the String
if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string")
    
    # 3. Print the First and Last Characters
    # Using index 0 for the first and -1 for the last character
    print(f"First character: {user_input[0]}")
    print(f"Last character: {user_input[-1]}")

    # 4. Build the String Character by Character
    print("\nConstructing string progressively:")
    accumulator = ""
    for char in user_input:
        accumulator += char
        print(accumulator)

    # 5. Bonus: Jumble the String
    # Strings are immutable, so we convert to a list to shuffle
    char_list = list(user_input)
    random.shuffle(char_list)
    jumbled_string = "".join(char_list)
    
    print(f"\nJumbled version: {jumbled_string}")