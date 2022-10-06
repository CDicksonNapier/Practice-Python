##Quiz Game#

print("Welcome to the quiz")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay lets begin: ")

score = 0
answer = input("what does CPU stand for?")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else: 
    print("Incorrect!")

answer = input("What Does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else: 
    print("Incorrect!")

answer = input("What Does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else: 
    print("Incorrect!")

answer = input("What Does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct")
    score += 1
else: 
    print("Incorrect!")

print("You got " +str(score)+ " questions correct!")
print("You got " +str((score / 4) * 100)+ "%")