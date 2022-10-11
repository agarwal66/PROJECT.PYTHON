from optparse import Option
from random import choice
while True:
    #computer input
    pick=['R','P','S']
    computer_input=choice(pick)
    #user input
    user_input=input("choose your move([R]rock/[P]paper/[S]scissior)")
    #all possibilities
    if computer_input == 'R' and user_input == 'R':
        print("It's a draw")
    elif computer_input == 'P' and user_input == 'P':
        print("It's a draw")
    elif computer_input == 'S' and user_input == 'S':
        print("It's a draw")
    elif computer_input == 'R' and user_input == 'P':
        print("You won")
    elif computer_input == 'P' and user_input == 'S':
        print("You won")
    elif computer_input == 'S' and user_input == 'R':
        print("You won")
    elif computer_input == 'R' and user_input == 'S':
        print("You loose")
    elif  computer_input == 'S' and user_input == 'P':
        print("You loose") 
    elif   computer_input == 'P' and user_input == 'R':
        print("You loose")
    else:
        print("Give a valid input")
    Option=int(input("Enter 0 if you want to play again:"))
    if (Option):
        break 