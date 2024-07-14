import random
import os
number = random.randint(0,100)
is_game_over = False

os.system("cls")
ask = input("Do you want to play 'hard' or easy' ")
if ask=='hard':
    lifes = 5
elif ask=='easy':
    lifes = 10
    
def conditions():
    global user_guess,number    #We use global variables in a function
    if number==user_guess:
        print(f"The number is {number} , You got it....")
    elif user_guess>number:
        print("Too high")
    elif user_guess<number:
        print("Too low")
        

while not is_game_over:
    user_guess = int(input("Guess a number in range 0-100 "))
    conditions()
    if number==user_guess:
        is_game_over = True
    if number!= user_guess:
        lifes -= 1
        print(f"You lose a life..Remainig lifes are {lifes}")
        input()
        os.system("cls")
    if lifes==0:
        is_game_over = True
        print(f"You lose.The actual number is {number} ")
input()