scores = [4.5, 6, 7.5, 8.5]


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

for score in scores:
    print(score, check_score(score))
