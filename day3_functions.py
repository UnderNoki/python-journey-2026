#introduction
def introduction(name):
         print("Hello", name, "I am learning Python.")     
         print("My goal is to study IT.") 

introduction("santi") 
introduction("budi") 
introduction("adu")


#check_score
def check_score(English_Score):
        if English_Score <0: 
            print("Error.")
        elif English_Score>9:
            print("ERROR, KAMU NYASAR")
        elif English_Score<5:
              print("Keep Trying")
        elif English_Score <7:
             print("Keep Preparing")
        elif English_Score <8:
            print("Keep going")
        else: 
              print("Excellent")

check_score(9.01)


#return
def get_greeting(name):
    return "hello "+ name

name = input("what is your name? ")

message = get_greeting(name)

print(message)

#penggabungan
def check_score(English_Score):
        if English_Score <0: 
            return "Error."
        elif English_Score>9:
            return "ERROR, KAMU NYASAR"
        elif English_Score<5:
            return "= Keep Trying"
        elif English_Score <7:
            return "= Keep Preparing"
        elif English_Score <8:
            return "= Keep going"
        else: 
            return "= Excellent"

English_Score = float(input("Whats your english score now? "))
message = check_score(English_Score)

print(message)

#test
def check_score(English_Score):
        if English_Score <0: 
            return "Error."
        elif English_Score>9:
            return "ERROR, KAMU NYASAR"
        elif English_Score<5:
            return "= Keep Trying"
        elif English_Score <7:
            return "= Keep Preparing"
        elif English_Score <8:
            return "= Keep going"
        else: 
            return "= Excellent"
        
score1 = check_score(4.5)
score2 = check_score(6)
score3 = check_score(7.5)
score4 = check_score(8.5)

print("score : 4.5", score1)
print("score : 6", score2)
print("score : 7.5",score3)
print("score : 8.5 ",score4)