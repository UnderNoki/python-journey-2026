students = ["Santi", "Budi", "Adu"]
scores = [4.5, 6, 8.5, 9]

def check_score(scor):
    if scor>9 or scor<0:
        return("error")
    elif scor<5:
         return("Keep Trying")
    elif scor<7:
         return("Keep Preparing")
    elif scor<8:
        return("Keep going")
    else:
        return("Excellent")
    
for student, scor in zip(students, scores):
    print(student, scor,check_score(scor) )