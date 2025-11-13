a = 2
b = 0
try:
    c = a/b
except ZeroDivisionError as e:
    print(e)