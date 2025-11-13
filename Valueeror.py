name = input("Name: ")
try:
    mark = int(input("Mark: "))
    if(mark < 0 or mark > 100):
        raise ValueError("Enter mark between 0 and 100! ")
except ValueError as e:
    print(e)