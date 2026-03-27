import random

# Step 1: Ask for User Input
user_string = input("Enter a string (exactly 10 characters): ")

# Step 2: Check the Length of the String
string_length = len(user_string)

if string_length < 10:
    print("String not long enough.")
elif string_length > 10:
    print("String too long.")
else:
    # String is exactly 10 characters
    print("Perfect string")
    
    # Step 3: Print the First and Last Characters
    print(f"First character: {user_string[0]}")
    print(f"Last character: {user_string[-1]}")
    
    # Step 4: Build the String Character by Character
    print("\nBuilding the string:")
    built_string = ""
    for i in range(len(user_string)):
        built_string += user_string[i]
        print(built_string)
    
    # Step 5: Bonus - Jumble the String
    print("\nBonus - Jumbled version:")
    char_list = list(user_string)
    random.shuffle(char_list)
    jumbled = "".join(char_list)
    print(jumbled)