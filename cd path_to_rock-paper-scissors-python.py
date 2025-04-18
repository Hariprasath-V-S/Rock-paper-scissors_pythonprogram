import random

choices = ["rock", "paper", "scissors"]
A=0
H=0
print("Rock, Paper, Scissors Game 🪨📄 ✂️\n")
print(" Try to beat Hari \n ") 
while True:
    user = input("Choose rock, paper or scissors (or 'quit' to stop): ").lower()
    if user == 'quit':
        print("Thanks for playing!\n")
        print(" Your Score:\n",A) 
        print(" Hari's Score:\n",H) 
        if(A>H):
            print("You won 🏆 the game by",A-H,"points") 
        elif(A==H): 
            print("The Match Tied 🤝") 
        else:
            print("You lose🥈 the game by",H-A,"points") 
        break
    if user not in choices:
        print("Invalid choice. Try again!")
        continue

    hari = random.choice(choices)
    print("Hari chose:", hari)

    if user == hari:
        print("It's a tie!🤜🤛\n")
    elif (user == "rock" and hari == "scissors") or \
         (user == "paper" and hari == "rock") or \
         (user == "scissors" and hari == "paper"):
        print("You won!👍\n") 
        print(" 🪙1 Points added to your Score\n")
        A+=1
        
    else:
        print("You lose!👎\n") 
        print(" 🪙1 points added to Hari's Score\n") 
        H+=1