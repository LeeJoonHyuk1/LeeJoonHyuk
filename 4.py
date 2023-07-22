scores=[]
while(True):
    score=input("input score\n")
    if(score=="stop"):
        break
    try:
        score=int(score)
        scores.append(score)
    except ValueError:
        print("please enter the valid score")

total=0
total = sum(scores)        
averageScore=total/len(scores)
print(averageScore)
    

aboveAverageStudentCount=0
for score in scores:   
    if (score>averageScore):
        aboveAverageStudentCount += 1
        print(aboveAverageStudentCount)
        
 