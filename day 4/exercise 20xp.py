import random

# ============================================
# 🌟 Exercise 1: What Are You Learning?
# ============================================
print("=" * 50)
print("Exercise 1: What Are You Learning?")
print("=" * 50)

def display_message():
    print("I am learning about functions in Python.")

display_message()


# ============================================
# 🌟 Exercise 2: What's Your Favorite Book?
# ============================================
print("\n" + "=" * 50)
print("Exercise 2: What's Your Favorite Book?")
print("=" * 50)

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")


# ============================================
# 🌟 Exercise 3: Some Geography
# ============================================
print("\n" + "=" * 50)
print("Exercise 3: Some Geography")
print("=" * 50)

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")


# ============================================
# Exercise 4: Random
# ============================================
print("\n" + "=" * 50)
print("Exercise 4: Random")
print("=" * 50)

def check_number(user_number):
    random_number = random.randint(1, 100)
    
    if user_number == random_number:
        print("Success! The numbers match!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

check_number(50)


# ============================================
# 🌟 Exercise 5: Let's Create Some Personalized Shirts!
# ============================================
print("\n" + "=" * 50)
print("Exercise 5: Let's Create Some Personalized Shirts!")
print("=" * 50)

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")

# Call with default values
make_shirt()
# Call with medium size (default text)
make_shirt("medium")
# Call with custom size and text
make_shirt("small", "Custom message")
# Call with keyword arguments
make_shirt(size="extra large", text="Hello World!")


# ============================================
# 🌟 Exercise 6: Magicians…
# ============================================
print("\n" + "=" * 50)
print("Exercise 6: Magicians…")
print("=" * 50)

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

make_great(magician_names)
show_magicians(magician_names)


# ============================================
# 🌟 Exercise 7: Temperature Advice
# ============================================
print("\n" + "=" * 50)
print("Exercise 7: Temperature Advice")
print("=" * 50)

def get_random_temp(season=None):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring":
        return random.randint(16, 23)
    elif season == "summer":
        return random.randint(24, 40)
    elif season == "autumn":
        return random.randint(10, 24)
    else:
        return random.randint(-10, 40)

def main():
    # Bonus: Ask for month to determine season
    month = int(input("Enter a month (1-12) or 0 for random: "))
    
    if month == 0:
        season = None
    elif month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    else:
        season = "autumn"
    
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    # Provide advice based on temperature
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()


print("\n" + "=" * 50)
print("All exercises completed!")
print("=" * 50)