# ============================================
# Challenge 1: Sorting
# ============================================
print("=" * 50)
print("Challenge 1: Sorting")
print("=" * 50)

def sort_words():
    # Step 1: Get Input
    user_input = input("Enter words separated by commas: ")
    
    # Step 2: Split the String
    words = user_input.split(",")
    
    # Step 3: Sort the List
    words.sort()
    
    # Step 4: Join the Sorted List
    result = ",".join(words)
    
    # Step 5: Print the Result
    print(f"Sorted: {result}")

# Run Challenge 1
sort_words()


# ============================================
# Challenge 2: Longest Word
# ============================================
print("\n" + "=" * 50)
print("Challenge 2: Longest Word")
print("=" * 50)

def longest_word(sentence):
    # Step 2: Split the Sentence into Words
    words = sentence.split()
    
    # Step 3: Initialize Variables
    longest = ""
    
    # Step 4 & 5: Iterate and Compare Word Lengths
    for word in words:
        # Step 5: Compare Word Lengths
        if len(word) > len(longest):
            longest = word
    
    # Step 6: Return the Longest Word
    return longest

# Test cases
test1 = "Margaret's toy is a pretty doll."
test2 = "A thing of beauty is a joy forever."
test3 = "Forgetfulness is by all means powerless!"

print(f'Input: "{test1}"')
print(f'Longest word: "{longest_word(test1)}"')
print()

print(f'Input: "{test2}"')
print(f'Longest word: "{longest_word(test2)}"')
print()

print(f'Input: "{test3}"')
print(f'Longest word: "{longest_word(test3)}"')

# Interactive version
print("\n--- Interactive Version ---")
user_sentence = input("Enter a sentence: ")
result = longest_word(user_sentence)
print(f'The longest word is: "{result}"')


print("\n" + "=" * 50)
print("Both challenges completed!")
print("=" * 50)