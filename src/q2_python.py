# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

# Both functions use this shared list to store items in insertion order.
inventory = []


# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."

def addItem(itemName):
    # Check existing items before adding a new one.
    for item in inventory:
        if item == itemName:
            print(f"{itemName} is already in inventory.")
            return  # Stop here so the duplicate is not added.

    # Add the item only after checking the entire list for duplicates.
    inventory.append(itemName)


# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

def listInventory():
    # An empty list is false, so 'not inventory' detects an empty inventory.
    if not inventory:
        print("Inventory is empty.")
    else:
        # Display all stored items in the order they were added.
        print("Inventory:", inventory)


# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
