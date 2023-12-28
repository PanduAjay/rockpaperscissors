import random  
start = True;
while start:
    player = input("Enter a choice: [rock, paper, scissors]".lower())
    computer = random.choice(["rock", "paper", "scissors"])
    if player == computer:
        print("Draw")
    elif player == "rock":
        print("You Win!" if computer == "scissors" else "You lose try it again...")
    elif player == "paper":
        print("You lose try it again..." if computer == "rock" else "You Win!")
    elif player == "scissors":
        print("You Win!" if computer == "paper" else "You lose try it again...")
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")    
    if not(input("Play again? (y/n): ").lower() == "y"):
        start = False
print("Thanks for playing!")        
        
