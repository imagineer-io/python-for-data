# if statement

# score = 85
score = int(input("score? "))
if score > 90:
    print("A")
elif score >= 80:
    print("B")
elif score < 70 and score > 50: # or
    print("test")
else:
    print("F")