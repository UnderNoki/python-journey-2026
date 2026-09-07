
scores = {
    "Santi": 4.5,
    "Budi": 6,
    "Adu": 8.5,
    "Rina": 7.5
}

name = input("Student name: ")
score = float(input("English score: "))

if score>9 or score<0:
     print("error")
else:
    scores[name] = score



def check_score(score):
    if score>9 or score<0:
        return("error")
    elif score<5:
         return("Keep Trying")
    elif score<7:
         return("Keep Preparing")
    elif score<8:
        return("Keep going")
    else:
        return("Excellent")
for student, score in scores.items():
    print(student, score, check_score(score))