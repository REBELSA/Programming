import random
r = random.randint(1,10)
print(r)
while(1):
    a = int(input("Enter a number: "))
    if a == r:
        print("Same")
        break
    else:
        print("Try again")
    