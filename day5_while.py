scores = {}
count = 0

def check_score(score):
    if score<5:
        return("Keep Trying")
    elif score<7:
        return("Keep Preparing")
    elif score<8:
        return("Keep going")
    else:
        return("Excellent")
    
while count<3:
    name = input("Student name: ")
    score = float(input("English score: "))

    if score > 9 or score < 0:
        print("error")
    else:
        scores[name] = score
        count = count + 1

for studen, score in scores.items():
    print(studen, score, check_score(score))