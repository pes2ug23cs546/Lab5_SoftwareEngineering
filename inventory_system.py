import ast  

inventory = {}


def add_item(name, quantity=0):
    """Add a new item or update an existing one in the inventory."""
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantity must be a non-negative integer.")
    inventory[name] = inventory.get(name, 0) + quantity
    print(f"✅ Added/updated '{name}' with quantity {quantity}.")


def remove_item(name):
    """Remove an item from the inventory."""
    try:
        del inventory[name]
        print(f"❌ Removed '{name}' from inventory.")
    except KeyError as err:
        print(f"⚠️ Cannot remove '{name}': {err}")


def get_qty(name):
    """Get the quantity of a specific item."""
    try:
        return inventory[name]
    except KeyError:
        print(f"⚠️ Item '{name}' not found in inventory.")
        return None


def load_data(filename="inventory.txt"):
    """Load inventory data from a file and return it as a dictionary."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            file_content = file.read().strip()
            if file_content:
                return ast.literal_eval(file_content)
            return {}
    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found. Starting with empty inventory.")
        return {}
    except (SyntaxError, ValueError) as err:
        print(
            f"⚠️ Could not load data from {filename}: {err}"
        )
        return {}


def save_data(filename="inventory.txt"):
    """Save the current inventory to a file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(inventory))
        print(f"💾 Inventory data saved to {filename}.")
    except OSError as err:
        print(f"⚠️ Failed to save data: {err}")


def print_data():
    """Display all inventory items and their quantities."""
    print("\n📋 Current Inventory:")
    if not inventory:
        print("  (empty)")
    for name, qty in inventory.items():
        print(f"  - {name}: {qty}")


def check_low_items(threshold=5):
    """Print items that have quantities below the given threshold."""
    print(f"\n🔍 Items below threshold ({threshold}):")
    low_items = [item for item, qty in inventory.items() if qty < threshold]
    if not low_items:
        print("  None! All items sufficiently stocked.")
    else:
        for item in low_items:
            print(f"  - {item}: {inventory[item]}")


def main():
    """Run a simple menu-driven inventory system."""
    global inventory  # local inventory variable
    inventory = load_data()

    while True:
        print("\nSelect an option:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Get item quantity")
        print("4. Show all items")
        print("5. Check low-stock items")
        print("6. Save and exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            qty = input("Quantity: ").strip()
            try:
                qty = int(qty)
                add_item(name, qty)
            except ValueError:
                print("❌ Invalid quantity. Must be an integer.")

        elif choice == "2":
            name = input("Item name to remove: ").strip()
            remove_item(name)

        elif choice == "3":
            name = input("Item name: ").strip()
            qty = get_qty(name)
            if qty is not None:
                print(f"✅ Quantity of '{name}': {qty}")

        elif choice == "4":
            print_data()

        elif choice == "5":
            try:
                threshold = int(input("Enter threshold: "))
                check_low_items(threshold)
            except ValueError:
                print("❌ Invalid threshold. Must be an integer.")

        elif choice == "6":
            save_data()
            print("👋 Exiting inventory system. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose between 1–6.")


if __name__ == "__main__":
    main()
