students = ["Santi", "Budi", "Adu"]
scores = [4.5, 6, 8.5]

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

    
for i in range(len(students)):   
    print(students[i], scores[i], check_score(scores[i]))
