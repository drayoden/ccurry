# lists are 0 (zero) based but length is correct.

lst = ['mooses', 'whiskers', 'weasle', 'knuckles', 'knees']
print(lst)
print(lst[2])
print(len(lst))

for i in range(len(lst)):
    print(i, lst[i])