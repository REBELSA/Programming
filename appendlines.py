l = []
for i in range(5):
    line = input("Enter line: ")
    l.append(line + "\n")
    with open("test.txt","w") as file:
        file.writelines(l)