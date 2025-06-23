# a number is to be create by the random
# give the number of options to make the correct choices.
# break the loop while after completing the no of counts or if the correct choice is made and not wish to continue
import random
a = random.randint(10,50)
print(a)
n=5
count = 0 
while(count < n):
    get_number = int(input("Enter the random number between 10 and 50"))
    if get_number == a:
        print("You guessed the correct number.")
        count=0
        user_play = input("Do you want to play again Y/N?")
        if user_play == "Y":
            a = random.randint(10,50)
            print(a)
        else:
            break
    else:
        count = count + 1
        if (n-count) > 0:
            print(f"You have {n-count} choice to choose the correct number, Try again")
