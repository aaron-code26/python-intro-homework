
#warmup:1
#score = int(input("Enter your score: "))
 
# if score >= 90:
    # grade = "A"
# elif score >= 80:
    # grade = "B"
# elif score >= 70:
    # grade = "C"
# elif score >= 60:
    # grade = "D"
# else:
    # grade = "F"
#  
# print("Score:", score)
# print("Grade:", grade)

#warmup:2
User_age= int(input(" Enter you age: "))

if User_age <=12:
    print ("Category: Child")
elif User_age >= 13 and User_age <= 18:
    print ("Category: Teen")
elif User_age >= 18 and User_age <= 65:
    print ("Category: Adult")
else:
    print ("Category: Senior")