import random
import string
from datetime import datetime, timedelta
import sys

# ============================================
# 🌟 Exercise 1: Currencies
# ============================================
print("=" * 50)
print("Exercise 1: Currencies")
print("=" * 50)

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        # Handle plural form
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"
    
    def __repr__(self):
        return self.__str__()
    
    def __int__(self):
        return self.amount
    
    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError("Unsupported type for addition")
    
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self
        else:
            raise TypeError("Unsupported type for addition")

# Test Currency class
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(f"str(c1): {str(c1)}")           # '5 dollars'
print(f"int(c1): {int(c1)}")           # 5
print(f"repr(c1): {repr(c1)}")         # '5 dollars'
print(f"c1 + 5: {c1 + 5}")             # 10 dollars
print(f"c1 + c2: {c1 + c2}")           # 15 dollars
print(f"c1: {c1}")                     # 5 dollars

c1 += 5
print(f"c1 += 5: {c1}")                # 10 dollars

c1 += c2
print(f"c1 += c2: {c1}")               # 20 dollars

# This will raise TypeError - uncomment to test
# print(c1 + c3)


# ============================================
# 🌟 Exercise 2: Import (Simulated in single file)
# ============================================
print("\n" + "=" * 50)
print("Exercise 2: Import")
print("=" * 50)

# This would normally be in func.py
def sum_two_numbers(a, b):
    """Sum two numbers and print the result."""
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")
    return result

# This simulates importing and using from exercise_one.py
print("Calling sum_two_numbers(10, 20):")
sum_two_numbers(10, 20)


# ============================================
# 🌟 Exercise 3: String module
# ============================================
print("\n" + "=" * 50)
print("Exercise 3: String module")
print("=" * 50)

def generate_random_string(length=5):
    """Generate a random string of specified length using uppercase and lowercase letters."""
    # Get all letters (uppercase + lowercase)
    all_letters = string.ascii_letters
    
    # Generate random string
    random_string = ''.join(random.choice(all_letters) for _ in range(length))
    return random_string

random_str = generate_random_string(5)
print(f"Random string of length 5: {random_str}")


# ============================================
# 🌟 Exercise 4: Current Date
# ============================================
print("\n" + "=" * 50)
print("Exercise 4: Current Date")
print("=" * 50)

def display_current_date():
    """Display the current date."""
    current_date = datetime.now()
    print(f"Current date: {current_date.strftime('%Y-%m-%d')}")
    return current_date

display_current_date()


# ============================================
# 🌟 Exercise 5: Amount of time left until January 1st
# ============================================
print("\n" + "=" * 50)
print("Exercise 5: Time until January 1st")
print("=" * 50)

def time_until_january_first():
    """Calculate and display time left until January 1st of next year."""
    now = datetime.now()
    
    # Determine target year (next year if we're past Jan 1, else this year)
    if now.month == 1 and now.day == 1:
        # If today is Jan 1, target is next year
        target_year = now.year + 1
    else:
        target_year = now.year + 1
    
    # Create datetime for January 1st of target year
    january_first = datetime(target_year, 1, 1)
    
    # Calculate difference
    time_left = january_first - now
    
    # Display results
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"Current date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target: January 1st, {target_year}")
    print(f"Time left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    
    return time_left

time_until_january_first()


# ============================================
# 🌟 Exercise 6: Birthday and minutes
# ============================================
print("\n" + "=" * 50)
print("Exercise 6: Birthday and minutes lived")
print("=" * 50)

def calculate_minutes_lived(birthdate_str, date_format="%d/%m/%Y"):
    """
    Calculate how many minutes a person has lived.
    
    Args:
        birthdate_str: Birthdate as string
        date_format: Format of the birthdate string (default: DD/MM/YYYY)
    """
    # Parse the birthdate
    birthdate = datetime.strptime(birthdate_str, date_format)
    
    # Get current datetime
    now = datetime.now()
    
    # Calculate time difference
    time_lived = now - birthdate
    
    # Convert to minutes
    total_seconds = time_lived.total_seconds()
    total_minutes = int(total_seconds / 60)
    
    print(f"Birthdate: {birthdate.strftime('%d %B %Y')}")
    print(f"You have lived approximately {total_minutes:,} minutes!")
    print(f"That's about {total_minutes // 525600:,} years in minutes!")
    
    return total_minutes

# Test with a sample birthdate
calculate_minutes_lived("15/05/1990")


# ============================================
# 🌟 Exercise 7: Faker Module
# ============================================
print("\n" + "=" * 50)
print("Exercise 7: Faker Module")
print("=" * 50)

# Check if faker is installed, if not show message
try:
    from faker import Faker
    
    def generate_fake_users(num_users):
        """Generate a list of fake users."""
        fake = Faker()
        users = []
        
        for _ in range(num_users):
            user = {
                'name': fake.name(),
                'address': fake.address().replace('\n', ', '),
                'language_code': fake.language_code()
            }
            users.append(user)
        
        return users
    
    # Generate and display users
    users_list = generate_fake_users(5)
    print("Generated 5 fake users:")
    for i, user in enumerate(users_list, 1):
        print(f"\nUser {i}:")
        for key, value in user.items():
            print(f"  {key}: {value}")

except ImportError:
    print("Faker module not installed.")
    print("To install, run: pip install faker")
    print("\nSimulating with fake data:")
    
    # Simulate what faker would produce
    simulated_users = [
        {'name': 'John Smith', 'address': '123 Main St, Springfield, IL', 'language_code': 'en'},
        {'name': 'Maria Garcia', 'address': '456 Oak Ave, Miami, FL', 'language_code': 'es'},
        {'name': 'Pierre Dubois', 'address': '789 Rue de Paris, Paris', 'language_code': 'fr'}
    ]
    
    for i, user in enumerate(simulated_users, 1):
        print(f"\nUser {i}:")
        for key, value in user.items():
            print(f"  {key}: {value}")


print("\n" + "=" * 50)
print("All exercises completed!")
print("=" * 50)