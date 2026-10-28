
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
# User_age= int(input(" Enter you age: "))
# 
# if User_age <=12:
    # print ("Category: Child")
# elif User_age >= 13 and User_age <= 18:
    # print ("Category: Teen")
# elif User_age >= 18 and User_age <= 65:
    # print ("Category: Adult")
# else:
    # print ("Category: Senior")
    
#warmup:3

s1=(not True and not False) #value of s1 is False
print(s1, "# The value of s1 is False because not True is False and not False is True")

s2=(True or False and False)
print(s2, )\
    

# warmup:4
# Ask the user for a number
#num = int(input("Enter a number: "))

# if num > 0:
#     print(f"{num} is positive.")
# elif num < 0:
#     print(f"{num} is negative.")
# else:
#     print(f"{num} is zero.")

# if num % 2 == 0:
#     print(f"{num} is even.")
# else:
    # print(f"{num} is odd.")

#Mini_project


# Day Planner Mini-Project


day_input = input("What day is it? ")
time_input = input("What time of day? ")

day = day_input.strip().lower()
time = time_input.strip().lower()


if day == "monday":
    if time == "morning":
        print("Suggestion: Rise and shine! Time to kickstart the week with a planning session.")
    elif time == "afternoon":
        print("Suggestion: Power through your afternoon tasks and take a short walk.")
    elif time == "evening":
        print("Suggestion: Relax with a good book and prepare for tomorrow.")
        
elif day == "tuesday":
    if time == "morning":
        print("Suggestion: Morning Python class - great time to focus!")
    elif time == "afternoon":
        print("Suggestion: Perfect time for collaborative team meetings or group study.")
    elif time == "evening":
        print("Suggestion: Unwind by cooking a delicious, healthy dinner.")
        
elif day == "saturday":
    if time == "morning":
        print("Suggestion: Head over to the local farmer's market or enjoy a slow breakfast.")
    elif time == "afternoon":
        print("Suggestion: Great afternoon to go for a hike or work on a fun hobby.")
    elif time == "evening":
        print("Suggestion: Perfect night for a movie or trying a new recipe.")

else:
    print("Sorry, I don't recognize that day or time combination.")
    print("Try using Monday, Tuesday, or Saturday combined with morning, afternoon, or evening...")
