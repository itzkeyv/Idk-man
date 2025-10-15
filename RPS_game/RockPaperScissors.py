import random

def get_computer_choice():
    #Get computer's random choice
    return random.randint(0, 2)  # 0 = Rock, 1 = Paper, 2 = Scissors

def choice_to_string(choice):
    #Convert choice number to string
    choices = {
        0: "Rock",
        1: "Paper", 
        2: "Scissors"
    }
    return choices.get(choice, "Invalid, try again duh")

def determine_winner(user_choice, computer_choice):
    #Determine the winner of the game
    # Tie
    if user_choice == computer_choice:
        return 0
    
    # User wins cases
    if ((user_choice == 0 and computer_choice == 2) or  # Rock vs Scissors
        (user_choice == 1 and computer_choice == 0) or  # Paper vs Rock
        (user_choice == 2 and computer_choice == 1)):   # Scissors vs Paper
        return 1
    
    # Computer wins
    return -1

def display_result(user_choice, computer_choice, result):
    #Displaying the game result
    print(f"\nYour choice: {choice_to_string(user_choice)}")
    print(f"Computer's choice: {choice_to_string(computer_choice)}")
    
    print("\nResult: ", end="")
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("Yoooo you win! 🎉")
    else:
        print("lol u sux cuz computer wins! 🤖")

def get_user_choice():
    #Get and validate user input
    while True:
        try:
            print("\nPlease choose:")
            print("0 - Rock ✊")
            print("1 - Paper ✋") 
            print("2 - Scissors ✌️")
            print("3 - Quit")
            
            choice = int(input("Enter your choice (0-3): "))
            
            if 0 <= choice <= 3:
                return choice
            else:
                print("Invalid choice! Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    #Main game function
    print("=== Rock Paper Scissors Game ===")
    print("Welcome to the game! 🎮")
    
    user_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        user_choice = get_user_choice()
        
        # Check if user wants to rage quit
        if user_choice == 3:
            print(f"\n=== Final Score ===")
            print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
            print("Thanks for playing! Buh bye! 👋")
            break
        
        # Get computer's choice
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if result == 1:
            user_score += 1
        elif result == -1:
            computer_score += 1
        else:
            ties += 1
        
        # Display result
        display_result(user_choice, computer_choice, result)
        
        # Display current score
        print(f"\nCurrent Score - You: {user_score} | Computer: {computer_score} | Ties: {ties}")
        print("-" * 50)

if __name__ == "__main__":
    main()
