#include <iostream>
#include <cstdlib>
#include <ctime>
#include <map>

using namespace std;

int get_computer_choice() {
    // Get computer's random choice
    return rand() % 3;  // 0 = Rock, 1 = Paper, 2 = Scissors
}

string choice_to_string(int choice) {
    // Convert choice number to string
    map<int, string> choices = {
        {0, "Rock ✊"},
        {1, "Paper ✋"},
        {2, "Scissors ✌️"}
    };
    
    if (choices.find(choice) != choices.end()) {
        return choices[choice];
    }
    return "Invalid, try again duh";
}

int determine_winner(int user_choice, int computer_choice) {
    // Determine the winner of the game
    // Tie
    if (user_choice == computer_choice) {
        return 0;
    }
    
    // User wins cases
    if ((user_choice == 0 && computer_choice == 2) ||  // Rock vs Scissors
        (user_choice == 1 && computer_choice == 0) ||  // Paper vs Rock
        (user_choice == 2 && computer_choice == 1)) {  // Scissors vs Paper
        return 1;
    }
    
    // Computer wins
    return -1;
}

void display_result(int user_choice, int computer_choice, int result) {
    // Displaying the game result
    cout << "\nYour choice: " << choice_to_string(user_choice) << endl;
    cout << "Computer's choice: " << choice_to_string(computer_choice) << endl;
    
    cout << "\nResult: ";
    if (result == 0) {
        cout << "It's a tie!";
    } else if (result == 1) {
        cout << "Yoooo you win! 🎉";
    } else {
        cout << "lol u sux cuz computer wins! 🤖";
    }
    cout << endl;
}

int get_user_choice() {
    // Get and validate user input
    int choice;
    
    while (true) {
        cout << "\nPlease choose:" << endl;
        cout << "0 - Rock ✊" << endl;
        cout << "1 - Paper ✋" << endl;
        cout << "2 - Scissors ✌️" << endl;
        cout << "3 - Quit" << endl;
        
        cout << "Enter your choice (0-3): ";
        cin >> choice;
        
        if (cin.fail()) {
            cin.clear();
            cin.ignore(10000, '\n');
            cout << "Invalid input! Please enter a number." << endl;
        } else if (choice >= 0 && choice <= 3) {
            return choice;
        } else {
            cout << "Invalid choice! Please enter a number between 0 and 3." << endl;
        }
    }
}

int main() {
    // Main game function
    cout << "=== Rock Paper Scissors Game ===" << endl;
    cout << "Welcome to the game! 🎮" << endl;
    
    // Initialize random seed
    srand(time(0));
    
    int user_score = 0;
    int computer_score = 0;
    int ties = 0;
    
    while (true) {
        int user_choice = get_user_choice();
        
        // Check if user wants to rage quit
        if (user_choice == 3) {
            cout << "\n=== Final Score ===" << endl;
            cout << "You: " << user_score << " | Computer: " << computer_score << " | Ties: " << ties << endl;
            cout << "Thanks for playing! Buh bye! 👋" << endl;
            break;
        }
        
        // Get computer's choice
        int computer_choice = get_computer_choice();
        
        // Determine winner
        int result = determine_winner(user_choice, computer_choice);
        
        // Update scores
        if (result == 1) {
            user_score++;
        } else if (result == -1) {
            computer_score++;
        } else {
            ties++;
        }
        
        // Display result
        display_result(user_choice, computer_choice, result);
        
        // Display current score
        cout << "\nCurrent Score - You: " << user_score << " | Computer: " << computer_score << " | Ties: " << ties << endl;
        cout << "--------------------------------------------------" << endl;
    }
    
    return 0;
}
