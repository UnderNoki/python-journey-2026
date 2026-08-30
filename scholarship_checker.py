nama = input("name?")
umur = int(input("your age?"))
English_Score = float(input("English score?"))

print("Name:", nama)
print("Age:", umur)

if English_Score <=4.99: 
    print("Keep Trying")
elif English_Score>9:
    print("ERROR, KAMU NYASAR")
elif English_Score <=6:
    print("Keep preparing for the scholarship.")
elif English_Score <=7:
    print("Excellent!")
else: 
    print("KEEP GOING!")