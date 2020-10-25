# count all elements with list comprehension

bp1 = ['one', 'two', 'one', 'three', 'four', 'two', 'seven', 'two', 'one', 'three']

counts1 = [bp1.count(item) for item in bp1]
counts2 = [bp1.count(item) for item in set(bp1)]
counts3 = [[bp1.count(item), item] for item in set(bp1)]
[print(bp1.count(item), item) for item in set(bp1)]


print(counts1)
print(counts2)
print(counts3)

