# ============================================
# 🌟 Exercise 1: Converting Lists into Dictionaries
# ============================================
print("=" * 50)
print("Exercise 1: Converting Lists into Dictionaries")
print("=" * 50)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Method 1: Using zip() and dict()
result_dict = dict(zip(keys, values))
print(f"Using zip(): {result_dict}")

# Method 2: Using dictionary comprehension (alternative)
result_dict2 = {keys[i]: values[i] for i in range(len(keys))}
print(f"Using comprehension: {result_dict2}")


# ============================================
# 🌟 Exercise 2: Cinemax #2
# ============================================
print("\n" + "=" * 50)
print("Exercise 2: Cinemax #2")
print("=" * 50)

# Original family data
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

print("Ticket prices:")
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    total_cost += price
    print(f"{name.capitalize()}: ${price}")

print(f"\nTotal cost: ${total_cost}")

# Bonus: User input version
print("\n--- BONUS: User Input Version ---")
family_input = {}
while True:
    member = input("Enter family member name (or 'done' to finish): ")
    if member.lower() == 'done':
        break
    age = int(input(f"Enter {member}'s age: "))
    family_input[member] = age

total_cost_input = 0
print("\nTicket prices:")
for name, age in family_input.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    total_cost_input += price
    print(f"{name.capitalize()}: ${price}")

print(f"\nTotal cost: ${total_cost_input}")


# ============================================
# 🌟 Exercise 3: Zara
# ============================================
print("\n" + "=" * 50)
print("Exercise 3: Zara")
print("=" * 50)

# Create the brand dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

print(f"Original brand: {brand}")

# Change number_stores to 2
brand["number_stores"] = 2
print(f"\nAfter changing number_stores to 2: {brand['number_stores']}")

# Print sentence about Zara's clients
clothes_types = ", ".join(brand["type_of_clothes"])
print(f"\nZara serves clients looking for: {clothes_types} clothing.")

# Add country_creation key
brand["country_creation"] = "Spain"
print(f"\nAdded country_creation: {brand['country_creation']}")

# Check if international_competitors exists and add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    print(f"\nAdded Desigual to competitors: {brand['international_competitors']}")

# Delete creation_date
del brand["creation_date"]
print(f"\nDeleted creation_date. Keys now: {list(brand.keys())}")

# Print last international competitor
last_competitor = brand["international_competitors"][-1]
print(f"\nLast competitor: {last_competitor}")

# Print major colors in US
us_colors = brand["major_color"]["US"]
print(f"Major colors in US: {us_colors}")

# Print number of keys
num_keys = len(brand)
print(f"\nNumber of keys: {num_keys}")

# Print all keys
print(f"All keys: {list(brand.keys())}")

# Bonus: Merge with more_on_zara
print("\n--- BONUS: Merging Dictionaries ---")
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# Update brand with more_on_zara (overwrites number_stores)
brand.update(more_on_zara)
print(f"After merging: {brand}")


# ============================================
# 🌟 Exercise 4: Disney Characters
# ============================================
print("\n" + "=" * 50)
print("Exercise 4: Disney Characters")
print("=" * 50)

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Characters to indices
char_to_index = {}
for i, char in enumerate(users):
    char_to_index[char] = i
print(f"Characters to indices: {char_to_index}")

# 2. Indices to characters
index_to_char = {}
for i, char in enumerate(users):
    index_to_char[i] = char
print(f"Indices to characters: {index_to_char}")

# 3. Sorted alphabetically to indices
sorted_chars = sorted(users)
sorted_char_to_index = {}
for i, char in enumerate(sorted_chars):
    sorted_char_to_index[char] = i
print(f"Sorted alphabetically: {sorted_char_to_index}")


print("\n" + "=" * 50)
print("All exercises completed!")
print("=" * 50)