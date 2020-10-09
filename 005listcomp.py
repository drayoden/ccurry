backpack = ['pizza','pop', 'kale', 'ice cream', 'yogurt']
healthy = ['yogurt', 'kale']

print(backpack)

# this alters the original list (list comperhension) -- see id
#backpack[:] = [item for item in backpack if item in healthy]

# list comperhension above exploded...

healthy_backpack = []

for item in backpack:
    if item in healthy:
        healthy_backpack.append(item)        


print(healthy_backpack)