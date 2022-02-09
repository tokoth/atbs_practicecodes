# List to Dictionary Function for Fantasy Game Inventory

# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# 
# Write a function named addToInventory(inventory, addedItems), where the 
# inventory parameter is a dictionary representing the player’s inventory (like 
# in the previous project) and the addedItems parameter is a list like dragonLoot.


#Solutions

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1

    print("Inventory:")
    item_total = 0
    for n, i in inventory.items():
        print(str(i) + ' ' + n)
        item_total += i
    print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)