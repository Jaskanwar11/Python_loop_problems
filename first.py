numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
print(len(numbers))
count = 0
for i in numbers:
    if i > 0:
        count += 1
    
print("Total positive numbers in the list are: ",count)