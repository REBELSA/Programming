try:
    with open("hey.txt","r") as file:
        b = file.read()
        print(b)
except FileNotFoundError:
    print("\nError: File not found")