backpack = ['pizza','pop', 'kale', 'ice cream', 'yogurt']
healthy = ['yogurt', 'kale']

print(backpack)
print(id(backpack))
print(healthy)
print("removing junck from backpack...")

# join lists into backpack with only 'healthy' items.

# this assigns to a new list with name 'backpack' -- see id
#backpack = [item for item in backpack if item in healthy]

# this alters the original list -- see id
backpack[:] = [item for item in backpack if item in healthy]

print(backpack)
print(id(backpack))
print(healthy)