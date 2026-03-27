# ============================================
# Coffee Shop Menu Manager
# ============================================

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}


def show_menu(menu_dict):
    """Print all drinks and prices."""
    if len(menu_dict) == 0:
        print("The menu is empty.")
    else:
        print("Current menu:")
        for drink, price in menu_dict.items():
            print(f"{drink} - {price}₪")


def add_item(menu_dict):
    """Add a new drink to the menu."""
    drink_name = input("Enter new drink name: ")
    
    if drink_name in menu_dict:
        print("Item already exists!")
        return
    
    try:
        price = float(input("Enter price: "))
        if price < 0:
            print("Invalid price.")
            return
        menu_dict[drink_name] = price
        print(f'"{drink_name}" added!')
    except ValueError:
        print("Invalid price.")


def update_price(menu_dict):
    """Change the price of an existing drink."""
    drink_name = input("Which drink do you want to update? ")
    
    if drink_name not in menu_dict:
        print("Item not found.")
        return
    
    try:
        new_price = float(input("Enter the new price: "))
        if new_price < 0:
            print("Invalid price.")
            return
        menu_dict[drink_name] = new_price
        print("Price updated!")
    except ValueError:
        print("Invalid price.")


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    drink_name = input("Which drink do you want to delete? ")
    
    if drink_name in menu_dict:
        del menu_dict[drink_name]
        print("Item deleted.")
    else:
        print("Item not found.")


def search_item(menu_dict):
    """Search for a drink and show its price."""
    drink_name = input("Which drink do you want to search for? ")
    
    if drink_name in menu_dict:
        print(f"{drink_name} costs {menu_dict[drink_name]}₪")
    else:
        print("Not in the menu.")


def apply_discount(menu_dict):
    """Apply a discount percentage to all items."""
    try:
        percent = float(input("Enter discount percentage (0-100): "))
        if percent < 0 or percent > 100:
            print("Invalid percentage.")
            return
        
        for drink in menu_dict:
            menu_dict[drink] = round(menu_dict[drink] * (1 - percent / 100), 2)
        print(f"Applied {percent}% discount to all items!")
    except ValueError:
        print("Invalid percentage.")


def show_options():
    """Print the available actions."""
    print("\nWhat would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Search item")
    print("6. Apply discount")
    print("7. Exit")


def run_coffee_shop():
    """Main loop of the program."""
    while True:
        show_options()
        choice = input("> ")
        
        if choice == "1":
            show_menu(menu)
        elif choice == "2":
            add_item(menu)
        elif choice == "3":
            update_price(menu)
        elif choice == "4":
            delete_item(menu)
        elif choice == "5":
            search_item(menu)
        elif choice == "6":
            apply_discount(menu)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


# Start the program
run_coffee_shop()