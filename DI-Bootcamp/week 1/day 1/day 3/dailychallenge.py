# ============================================
# Challenge 1: Letter Index Dictionary
# ============================================
print("=" * 50)
print("Challenge 1: Letter Index Dictionary")
print("=" * 50)

# Get user input
word = input("Enter a word: ")

# Create dictionary with letter indices
letter_indices = {}

for index, char in enumerate(word):
    if char in letter_indices:
        # Letter already exists, append index
        letter_indices[char].append(index)
    else:
        # New letter, create new list with index
        letter_indices[char] = [index]

print(f"Result: {letter_indices}")


# ============================================
# Challenge 2: Affordable Items
# ============================================
print("\n" + "=" * 50)
print("Challenge 2: Affordable Items")
print("=" * 50)

def clean_price(price_str):
    """Remove $ and commas from price string, return as int"""
    # Remove $ and commas
    cleaned = price_str.replace("$", "").replace(",", "")
    return int(cleaned)

def buy_items(items_purchase, wallet):
    """Buy items based on priority and available money"""
    # Clean wallet amount
    available_money = clean_price(wallet)
    
    basket = []
    
    # Iterate through items (dictionary maintains insertion order in Python 3.7+)
    for item_name, price_str in items_purchase.items():
        item_price = clean_price(price_str)
        
        # Check if we can afford this item
        if available_money >= item_price:
            basket.append(item_name)
            available_money -= item_price
    
    # Return result
    if len(basket) == 0:
        return "Nothing"
    else:
        return sorted(basket)

# Example 1
print("\n--- Example 1 ---")
items_purchase1 = {
    "Water": "$1", 
    "Bread": "$3", 
    "TV": "$1,000", 
    "Fertilizer": "$20"
}
wallet1 = "$300"
result1 = buy_items(items_purchase1, wallet1)
print(f"Items: {items_purchase1}")
print(f"Wallet: {wallet1}")
print(f"Can buy: {result1}")

# Example 2
print("\n--- Example 2 ---")
items_purchase2 = {
    "Apple": "$4", 
    "Honey": "$3", 
    "Fan": "$14", 
    "Bananas": "$4", 
    "Pan": "$100", 
    "Spoon": "$2"
}
wallet2 = "$100"
result2 = buy_items(items_purchase2, wallet2)
print(f"Items: {items_purchase2}")
print(f"Wallet: {wallet2}")
print(f"Can buy: {result2}")

# Example 3
print("\n--- Example 3 ---")
items_purchase3 = {
    "Phone": "$999", 
    "Speakers": "$300", 
    "Laptop": "$5,000", 
    "PC": "$1200"
}
wallet3 = "$1"
result3 = buy_items(items_purchase3, wallet3)
print(f"Items: {items_purchase3}")
print(f"Wallet: {wallet3}")
print(f"Can buy: {result3}")

# Interactive version
print("\n--- Interactive Version ---")
items_input = {}
num_items = int(input("How many items to add? "))

for i in range(num_items):
    item_name = input(f"Enter item {i+1} name: ")
    item_price = input(f"Enter price for {item_name} (e.g., $10 or $1,000): ")
    items_input[item_name] = item_price

wallet_input = input("Enter your wallet amount (e.g., $300): ")
result = buy_items(items_input, wallet_input)
print(f"\nYou can buy: {result}")


print("\n" + "=" * 50)
print("Both challenges completed!")
print("=" * 50)
