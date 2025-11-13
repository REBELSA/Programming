s=input("Enter a sentence")
C = 0
for i in s:
    if i in ['a','e','i','o','u']:
        C = C+1
print(C)