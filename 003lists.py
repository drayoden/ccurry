healthy = ['pizza','pop','ice cream']
print(healthy)
print("mooses" in healthy)
print("pop" in healthy)

if "pizza" in healthy:
    print("eating pizza...")

if "salad" not in healthy:
    print("buying salad")

healthy.remove('ice cream')
print(healthy)

