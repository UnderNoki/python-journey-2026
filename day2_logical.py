age = int(input("Your age?"))
english_score = float(input("Your english score?"))

if age >18 and english_score >5:
    print("You meet both conditions")
elif age >18 or english_score >5:
    print("Keep it up")
else:
    print("You're not ready")