# Implement the game rock, paper, scissors
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
import random
def getUserChoice():
    choice = input("Enter the choice as rock/paper/scissors:").lower()
    while choice not in ['rock','paper','scissors']:
        print("Invalid entry,re-enter")
        choice = input("Enter the choice as rock/paper/scissors:").lower()
    return choice

def getCompChoice():
    return random.choice(['paper','scissors','rock'])

def determineWinner(user_choice,comp_choice):
    print(f"\nUser choice:{user_choice}\nComputer Choice:{comp_choice}")
    if getUserChoice == getCompChoice:
        return "its a tie!"
    elif((user_choice == "rock" and comp_choice =="scissors")or
         (user_choice == "paper" and user_choice =="rock")or
         (user_choice == "scissors" and comp_choice =="paper")):
        return "You Won" 
    else:
        return "Computer Won"
        
def play():
    while True:
        user_score = 0
        comp_score = 0
        print("Lets play --Rock Paper Scissors--")
        for _ in range(0,5):
            print("\nRock smashes scissors.\nPaper covers rock.\nScissors cut paper.")
            user_choice = getUserChoice()
            comp_choice = getCompChoice()
            result = determineWinner(user_choice,comp_choice)
            if result == "You Won":
                user_score += 1
            elif result == "Computer Won":
                comp_score += 1

        print("\n\n##Game Over##")
        if user_score > comp_score:
            print(f"You Won the Match!!!\nScore:{user_score}")
        elif user_score < comp_score:
            print(f"Computer Won the Match!!!\nScore:{comp_score}")
        else:
            print("It's a Tie")
        again = input("Play Again(yes/no):")
        if again != 'yes':
            break
play()
