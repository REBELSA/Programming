a = list(map(int,input("Enter the numbers: ").split(" ")))
print(a)
avg = sum(a)/len(a)
print(avg)
for i in a:
    if i > avg:
        print(i,end = " ")