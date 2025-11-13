score = int(input("Enter the score: "))

if score > 90:
    print("A grade")
elif score >= 80 and score<= 90:
    print("B grade")
elif score >= 70 and score <= 80:
    print("C grade")
elif score >= 60 and score <= 70:
    print("D grade")
elif score <= 60:
    print("You are a FAILURE")
