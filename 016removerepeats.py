stuff = [
    'mooses', 'puppies', 'monkey', 'wombat', 'kitties', 'squirrels',
    'monkey', 'wombat', 'kitties', 'squirrels','mooses', 
    'puppies', 'monkey', 'wombat', 'kitties', 'squirrels','unicorns',
    'orks','ogars','fairies',
]

print(stuff)


stuff.remove('wombat') # only removes first instance of 'wombat'
print(stuff)

print(stuff[3:9])  # print the elements 3 to 9 -- [start:end]
print(stuff[:10])  # print elements 0 to 10
print(stuff[:]) # entire list
stuff2 = stuff[:] # COPY of list, not a reference to the same list
print(stuff2)
print(id(stuff))
print(id(stuff2))

stuff[:] = [1,2,4,5,6,6,7,78] # replaces entire list, keeps the reference
print(stuff)
print(id(stuff))






