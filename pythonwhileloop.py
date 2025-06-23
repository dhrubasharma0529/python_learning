# infinite loop
# because it can run until the infinite loop under the conditions.
import random
a = random.randint(10,50)
print(a)

while(True):
     b = int(input("Enter the guessed number between 10 and 50"))
     if b == a:
        print("You won")
        user_play = input("Do you want to play again Y/N ?")

        if user_play == "Y":
            a = random.randint(10,50)
            print(a)



        else:
            break
    else:
        print("number doesnot match try again.")
        