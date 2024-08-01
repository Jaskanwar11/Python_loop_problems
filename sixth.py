number = 5

while True:
    num = int(input("Enter a number b/w 1 and 10: "))
    if 0 < num < 11:
        print("Correct!")
        break
    else:
        print("Wrong\nTry again!")
