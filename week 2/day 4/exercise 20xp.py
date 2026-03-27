import json
import random
import os

# ============================================
# 🌟 Exercise 1: Random Sentence Generator
# ============================================

def get_words_from_file(file_path):
    """
    Read words from a file and return as a list.
    
    Args:
        file_path: Path to the word list file
    
    Returns:
        List of words
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()
            # Split by whitespace and filter empty strings
            words = [word.strip().lower() for word in content.split() if word.strip()]
            return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def get_random_sentence(length, words_list):
    """
    Generate a random sentence of specified length.
    
    Args:
        length: Number of words in the sentence
        words_list: List of words to choose from
    
    Returns:
        Random sentence as string
    """
    if not words_list:
        return "No words available to generate sentence."
    
    # Select random words
    selected_words = [random.choice(words_list) for _ in range(length)]
    
    # Create sentence (first word capitalized, add period at end)
    sentence = " ".join(selected_words).lower()
    sentence = sentence[0].upper() + sentence[1:] + "."
    
    return sentence


def create_sample_word_file(file_path):
    """Create a sample word list file if it doesn't exist."""
    sample_words = """apple banana cherry date elderberry fig grape honeydew 
    kiwi lemon mango nectarine orange papaya quince raspberry strawberry 
    tomato ugli fruit vanilla watermelon xigua yam zucchini
    house car tree dog cat book computer phone table chair window door
    happy sad fast slow big small bright dark loud quiet hot cold"""
    
    try:
        with open(file_path, "w") as file:
            file.write(sample_words)
        print(f"Created sample word file: {file_path}")
    except Exception as e:
        print(f"Error creating file: {e}")


def exercise1_main():
    """Main function for Exercise 1."""
    print("=" * 60)
    print("Exercise 1: Random Sentence Generator")
    print("=" * 60)
    
    word_file = "words_list.txt"
    
    # Create sample file if it doesn't exist
    if not os.path.exists(word_file):
        create_sample_word_file(word_file)
    
    # Get words from file
    words = get_words_from_file(word_file)
    
    if not words:
        print("Could not load words. Exiting.")
        return
    
    print(f"\nLoaded {len(words)} words from file.")
    print("\nThis program generates a random sentence from a word list.")
    print("Enter a number between 2 and 20 for sentence length.")
    
    # Get user input
    try:
        length_input = input("\nHow many words should the sentence have? ")
        length = int(length_input)
        
        # Validate input
        if length < 2 or length > 20:
            print(f"Error: {length} is out of range. Please enter a number between 2 and 20.")
            return
        
        # Generate and display sentence
        sentence = get_random_sentence(length, words)
        print(f"\nGenerated sentence ({length} words):")
        print(sentence)
        
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")


# ============================================
# 🌟 Exercise 2: Working with JSON
# ============================================

def exercise2_main():
    """Main function for Exercise 2."""
    print("\n" + "=" * 60)
    print("Exercise 2: Working with JSON")
    print("=" * 60)
    
    # Sample JSON string
    sampleJson = """{ 
       "company":{ 
          "employee":{ 
             "name":"emma",
             "payable":{ 
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""
    
    # Step 1: Parse JSON string
    print("\nStep 1: Loading JSON...")
    try:
        data = json.loads(sampleJson)
        print("JSON loaded successfully.")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return
    
    # Step 2: Access nested salary key
    print("\nStep 2: Accessing nested 'salary' key...")
    try:
        salary = data["company"]["employee"]["payable"]["salary"]
        print(f"Employee salary: ${salary}")
    except KeyError as e:
        print(f"Key not found: {e}")
        return
    
    # Step 3: Add birth_date key
    print("\nStep 3: Adding 'birth_date' key...")
    data["company"]["employee"]["birth_date"] = "1990-05-15"
    print("Added birth_date: 1990-05-15")
    
    # Display modified data
    print("\nModified employee data:")
    print(f"  Name: {data['company']['employee']['name']}")
    print(f"  Salary: ${data['company']['employee']['payable']['salary']}")
    print(f"  Bonus: ${data['company']['employee']['payable']['bonus']}")
    print(f"  Birth Date: {data['company']['employee']['birth_date']}")
    
    # Step 4: Save to file
    print("\nStep 4: Saving to file...")
    output_file = "employee_data.json"
    
    try:
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Successfully saved to '{output_file}'")
        
        # Display the saved JSON
        print(f"\nContent of '{output_file}':")
        print(json.dumps(data, indent=4))
        
    except Exception as e:
        print(f"Error saving file: {e}")


# ============================================
# Main Execution
# ============================================

if __name__ == "__main__":
    # Run Exercise 1
    exercise1_main()
    
    # Run Exercise 2
    exercise2_main()
    
    print("\n" + "=" * 60)
    print("All exercises completed!")
    print("=" * 60)