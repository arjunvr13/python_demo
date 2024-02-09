score = int(input("enter the score of the student ="))
if(score >= 90) and (score <=100) :
    print("A+")
elif(score >= 80) and (score <=90):
    print("A")
elif(score >= 70) and (score <=80):
    print("B+")
elif(score >= 60) and (score <=70):
    print("B")
elif(score < 50):
    print("Failed")
else:
    print("invalid")
                  