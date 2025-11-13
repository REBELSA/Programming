a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("1: addition, 2: subtraction, 3:multiplication, 4: division")
choice = int(input("Enter your choice: "))
while(1):
    if(choice == 1):
        print(a+b)
        break
    elif(choice == 2):
        print(a-b)
        break
    elif(choice == 3):
        print(a*b)
        break
    elif(choice == 4):
        print(a/b)
        break
    else:
        print("Invalid choice")
        break 

        
    
    