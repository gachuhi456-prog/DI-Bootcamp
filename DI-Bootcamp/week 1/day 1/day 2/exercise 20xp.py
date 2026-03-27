import random

# ============================================
# 🌟 Exercise 1: Favorite Numbers
# ============================================
print("=" * 50)
print("Exercise 1: Favorite Numbers")
print("=" * 50)

my_fav_numbers = {7, 13, 42}
print(f"My favorite numbers: {my_fav_numbers}")

my_fav_numbers.add(99)
my_fav_numbers.add(100)
print(f"After adding two numbers: {my_fav_numbers}")

my_fav_numbers.remove(100)
print(f"After removing last added: {my_fav_numbers}")

friend_fav_numbers = {3, 7, 21, 42}
print(f"Friend's favorite numbers: {friend_fav_numbers}")

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(f"Our favorite numbers (concatenated): {our_fav_numbers}")


# ============================================
# 🌟 Exercise 2: Tuple (Immutability Demo)
# ============================================
print("\n" + "=" * 50)
print("Exercise 2: Tuple")
print("=" * 50)

my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")
print("Tuples are immutable - cannot add items directly!")
print("To 'add' items, you must create a new tuple:")

new_tuple = my_tuple + (4, 5)
print(f"New tuple after concatenation: {new_tuple}")


# ============================================
# 🌟 Exercise 3: List Manipulation
# ============================================
print("\n" + "=" * 50)
print("Exercise 3: List Manipulation")
print("=" * 50)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(f"Original basket: {basket}")

basket.remove("Banana")
print(f"After removing 'Banana': {basket}")

basket.remove("Blueberries")
print(f"After removing 'Blueberries': {basket}")

basket.append("Kiwi")
print(f"After adding 'Kiwi' to end: {basket}")

basket.insert(0, "Apples")
print(f"After adding 'Apples' to beginning: {basket}")

apples_count = basket.count("Apples")
print(f"'Apples' appears {apples_count} times")

basket.clear()
print(f"After emptying the list: {basket}")


# ============================================
# 🌟 Exercise 4: Floats
# ============================================
print("\n" + "=" * 50)
print("Exercise 4: Floats")
print("=" * 50)

print("Float: decimal number (e.g., 1.5, 3.14)")
print("Integer: whole number (e.g., 1, 2, 100)")
print("Difference: floats have decimal points, integers don't")

sequence = []
for i in range(1, 5):
    sequence.append(i + 0.5)
    sequence.append(i + 1)

print(f"Generated sequence: {sequence}")


# ============================================
# 🌟 Exercise 5: For Loop
# ============================================
print("\n" + "=" * 50)
print("Exercise 5: For Loop")
print("=" * 50)

print("Numbers 1 to 20:")
for num in range(1, 21):
    print(num, end=" ")
print()

print("Numbers at even indices (0, 2, 4...) from 1 to 20:")
numbers = list(range(1, 21))
for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i], end=" ")
print()


# ============================================
# 🌟 Exercise 6: While Loop
# ============================================
print("\n" + "=" * 50)
print("Exercise 6: While Loop")
print("=" * 50)

while True:
    name = input("Enter your name (at least 3 letters, no digits): ")
    
    if name.isdigit():
        print("Invalid! Name cannot be only digits. Try again.")
    elif len(name) < 3:
        print("Invalid! Name must be at least 3 letters. Try again.")
    else:
        print("Thank you!")
        break


# ============================================
# 🌟 Exercise 7: Favorite Fruits
# ============================================
print("\n" + "=" * 50)
print("Exercise 7: Favorite Fruits")
print("=" * 50)

fav_fruits_input = input("Enter your favorite fruits (separated by spaces): ")
fav_fruits = fav_fruits_input.split()
print(f"Your favorite fruits: {fav_fruits}")

chosen_fruit = input("Enter the name of any fruit: ")

if chosen_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# ============================================
# 🌟 Exercise 8: Pizza Toppings
# ============================================
print("\n" + "=" * 50)
print("Exercise 8: Pizza Toppings")
print("=" * 50)

toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print(f"\nYour toppings: {toppings}")
total_cost = base_price + (len(toppings) * topping_price)
print(f"Base price: ${base_price}")
print(f"Toppings cost: ${len(toppings) * topping_price}")
print(f"Total cost: ${total_cost}")


# ============================================
# 🌟 Exercise 9: Cinemax Tickets
# ============================================
print("\n" + "=" * 50)
print("Exercise 9: Cinemax Tickets")
print("=" * 50)

family_ages_input = input("Enter ages of family members (separated by spaces): ")
family_ages = [int(age) for age in family_ages_input.split()]

total_cost = 0
for age in family_ages:
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost
    print(f"Age {age}: ${cost}")

print(f"\nTotal ticket cost: ${total_cost}")

# Bonus: Restricted movie (ages 16-21 only)
print("\n--- BONUS: Restricted Movie (Ages 16-21) ---")
group_ages_input = input("Enter ages of teenagers (separated by spaces): ")
group_ages = [int(age) for age in group_ages_input.split()]

allowed_attendees = []
for age in group_ages:
    if 16 <= age <= 21:
        allowed_attendees.append(age)

print(f"Original group ages: {group_ages}")
print(f"Allowed attendees (ages 16-21): {allowed_attendees}")
print(f"Number of people who can watch: {len(allowed_attendees)}")


print("\n" + "=" * 50)
print("All exercises completed!")
print("=" * 50)