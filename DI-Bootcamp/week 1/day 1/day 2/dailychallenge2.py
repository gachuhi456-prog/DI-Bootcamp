# ============================================
# Birthday Cake Challenge
# ============================================

# Get user birthdate
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

# Parse the date
day, month, year = birthdate.split("/")
day = int(day)
month = int(month)
year = int(year)

# Calculate age
from datetime import datetime
current_year = datetime.now().year
age = current_year - year

# Get last digit of age for candles
last_digit = age % 10

# Create candle string (i characters)
candles = "i" * last_digit if last_digit > 0 else "i"

# Build the cake
def print_cake():
    print(f"       ___{candles}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

# Check for leap year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(f"\nYou are {age} years old!")
print(f"Candles on cake: {last_digit}")

if is_leap_year:
    print("\n🎉 You were born on a leap year! Here are TWO cakes! 🎉\n")
    print("       CAKE 1:")
    print_cake()
    print("\n       CAKE 2:")
    print_cake()
else:
    print("\nHere is your cake!\n")
    print_cake()