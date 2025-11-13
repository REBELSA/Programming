#Write a program that handles multiple exceptions: divide by zero, invalid input, and index out of range.
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter 2nd number: "))
    c = a/b
    l = [2,3,7,8,4]
    print(a,"Divided by",b,"=",c)
    ind = int(input("Enter the list index: "))
    D = print("Value at Index ",ind,":",l[ind])
except (ZeroDivisionError,IndexError,ValueError) as e:
    print(e)