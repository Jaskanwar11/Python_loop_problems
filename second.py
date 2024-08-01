n = int(input("Enter a number: "))
sum = 0
for num in range(n+1):
    if num % 2 == 0:
        sum = sum + num

print(sum)