items = ["apple", "mango", "banana", "apple", "watermelon"]
unique_itmes = set()

for item in items:
    if item in unique_itmes:
        print(item, "is already present in the list")
        continue

    unique_itmes.add(item)

print(unique_itmes)