import random;

name = input("What's your name?\n")
rizz = int(random.random() * 100)
print(name + ", you have " + str(rizz) + "% rizz")

#Personalized commentary
if rizz <= 50:
    print("rip better luck next time")
elif rizz > 50 and rizz < 90:
    print("Ey nice rizz")
elif rizz >= 90:
    print("Woah bro thats TOO much rizz")
