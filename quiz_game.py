print("Welcome to my computer quiz!")

playing = input("do you wanna play? ")

if playing.lower() != "yes":
    quit()

print("okay! Lets play")
score = 0

ans = input("Wofür steht CPU? ")
if ans.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("Wofür steht GPU? ")
if ans.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("Wofür seht RAM? ")
if ans.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("Wofür steht PSU? ")
if ans.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " question correct!")
print("you got " + str(score/4 * 100) + "%.")
