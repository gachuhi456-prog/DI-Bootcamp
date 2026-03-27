# ============================================
# Challenge 1: Multiples of a Number
# ============================================
print("=" * 50)
print("Challenge 1: Multiples of a Number")
print("=" * 50)

# Get user inputs
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Generate list of multiples
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(f"Output: {multiples}")


# ============================================
# Challenge 2: Remove Consecutive Duplicate Letters
# ============================================
print("\n" + "=" * 50)
print("Challenge 2: Remove Consecutive Duplicate Letters")
print("=" * 50)

# Get user input
user_word = input("Enter a word: ")

# Remove consecutive duplicates
if len(user_word) == 0:
    result = ""
else:
    result = user_word[0]  # Start with first character
    
    for i in range(1, len(user_word)):
        # Only add character if it's different from the previous one
        if user_word[i] != user_word[i - 1]:
            result += user_word[i]

print(f"Output: \"{result}\"")


print("\n" + "=" * 50)
print("Both challenges completed!")
print("=" * 50)