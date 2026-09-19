# user1=computer 
# user2=you
# -1=snake
# 1=water
# 0=gun
import random
computer = random.choice([0,1,-1])
you = int(input("enter your choice:"))
dict={1:"water",-1:"snake",0:"gun"}

print(f"your choice:{dict[you]}\ncomputer choice:{dict[computer]}")

if(computer==you):
    print("Its draw")
else:
    if(computer==1 and you==-1):
        print("you win")
    elif(computer==1 and you==0):
        print("you lose")
    elif(computer==-1 and you==1):
        print("you lose")
    elif(computer==-1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    else:
        print("something went wrong")