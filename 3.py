# personalInfo = []

# count = 0
# value = input("please enter your name\n")
# while(True):
#     if(value == "stop"):
#         break
#     if(count == 0):
#         personalInfo.insert(count, value)
#         count+=1
#     if (count == 1):
#         value = input("pelase enter SSN\n")
#         personalInfo.insert(count, value)
#         count+=1
#     if (count == 2):
#         value = input("pelase enter PN\n")
#         personalInfo.insert(count, value)
#         count+=1
#         print(personalInfo)
#         break

scores = []
while(True):
    score = input("input score\n")
    if(score == "stop"):
        break
    scores.append(score)
    print(scores)
    
# aboveAverageStudentCount = 0
# avergeScore = 0
# middleScore = 0
# total = 0 
# middle = int(len(scores)/2)
# # 차순을 만들어야 된다
# # 오름차순
# scores.sort()
# # 내림차순
# # scores.sort(reverse=True)
# print(scores)
# print(scores[middle],"is medial score")
# for score in scores:
#     total = total + int(score)
# avergeScore = total / len(scores)
# print(avergeScore)

# for score in scores:
#     if (int(score) > avergeScore):
#         aboveAverageStudentCount += 1
# print(aboveAverageStudentCount)

# # stack queue
# value = scores.pop() # stack 게시판
# print(value)
# value = scores.pop(0) # queue 선착순
# print(value)
# # list인데 FIFO 면 queue
# # list인데 LIFO 면 stack 



    


    

#  이름 주민번호 전화번호 

# a = 3 

# a == 3 