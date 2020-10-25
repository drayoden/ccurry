stuff = ['mooses', 'puppies', 'unicorn', 'wombat','kitties','squirrels']
print(stuff)

del stuff[2]  # deletes 'unicorn'
print(stuff)

stuff.insert(2,'monkey')
print(stuff)

del stuff[-1] # removes last element
print(stuff)

stuff.insert(2,'gremlin')
print(stuff)

del stuff[1:] # removes everything starting at [1]: 'puppies'
print(stuff)

stuff.insert(1,['puppies', 'unicorn', 'wombat','kitties','squirrels'])
print(stuff)