try:
    a = int(input("Enter numerator"))
    b = int(input("Enter denominator"))
    result = a / b
    print("Result is ", result)
except ValueError:
    print("Please enter valid integers. ")
except ZeroDivisionError:
    print("Denominator cannot be zero. ")