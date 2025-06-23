import random
def play_again():
     user_play = input("Do you want to play again Y or N").capitalize()
     if user_play == 'Y':
        return random.choices(a)
a = ['Rock','Paper', 'Scissor']
b=random.choices(a)
print(b)
while (True):
    user_input = input("Enter either rock, paper or scissor").capitalize()
    print(user_input)
    print(b[0])
    if user_input == b[0]:
        print("Draw")
        call = play_again()
        if call != 'Y':
            break

    elif user_input == "Rock" and b[0]== "Paper":
        print("Computer Won")
        call=play_again()
        if call != 'Y':
            break

    elif user_input == "Paper" and b[0] == "Scissor":
        print("Computer Won")
        call=play_again()
        if call != 'Y':
            break
        
    else:
        print("You won")
        call=play_again()
        if call != 'Y':
            break
      
