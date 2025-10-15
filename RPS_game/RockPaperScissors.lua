math.randomseed(os.time())

function get_computer_choice()
    -- Get computer's random choice
    return math.random(0, 2)  -- 0 = Rock, 1 = Paper, 2 = Scissors
end

function choice_to_string(choice)
    -- Convert choice number to string
    local choices = {
        [0] = "Rock ✊",
        [1] = "Paper ✋",
        [2] = "Scissors ✌️"
    }
    
    return choices[choice] or "Invalid, try again duh"
end

function determine_winner(user_choice, computer_choice)
    -- Determine the winner of the game
    -- Tie
    if user_choice == computer_choice then
        return 0
    end
    
    -- User wins cases
    if ((user_choice == 0 and computer_choice == 2) or  -- Rock vs Scissors
        (user_choice == 1 and computer_choice == 0) or  -- Paper vs Rock
        (user_choice == 2 and computer_choice == 1)) then  -- Scissors vs Paper
        return 1
    end
    
    -- Computer wins
    return -1
end

function display_result(user_choice, computer_choice, result)
    -- Displaying the game result
    print("\nYour choice: " .. choice_to_string(user_choice))
    print("Computer's choice: " .. choice_to_string(computer_choice))
    
    io.write("\nResult: ")
    if result == 0 then
        print("It's a tie!")
    elseif result == 1 then
        print("Yoooo you win! 🎉")
    else
        print("lol u sux cuz computer wins! 🤖")
    end
end

function get_user_choice()
    -- Get and validate user input
    while true do
        print("\nPlease choose:")
        print("0 - Rock ✊")
        print("1 - Paper ✋")
        print("2 - Scissors ✌️")
        print("3 - Quit")
        
        io.write("Enter your choice (0-3): ")
    
        local input = io.read()
        local choice = tonumber(input)
        
        if choice and choice >= 0 and choice <= 3 then
            return choice
        else
            print("Invalid choice! Please enter a number between 0 and 3.")
        end
    end
end

function main()
    -- Main game function
    print("=== Rock Paper Scissors Game ===")
    print("Welcome to the game! 🎮")
    
    local user_score = 0
    local computer_score = 0
    local ties = 0
    
    while true do
        local user_choice = get_user_choice()
        
        -- Check if user wants to rage quit
        if user_choice == 3 then
            print("\n=== Final Score ===")
            print("You: " .. user_score .. " | Computer: " .. computer_score .. " | Ties: " .. ties)
            print("Thanks for playing! Buh bye! 👋")
            break
        end
        
        -- Get computer's choice
        local computer_choice = get_computer_choice()
        
        -- Determine winner
        local result = determine_winner(user_choice, computer_choice)
        
        -- Update scores
        if result == 1 then
            user_score = user_score + 1
        elseif result == -1 then
            computer_score = computer_score + 1
        else
            ties = ties + 1
        end
        
        -- Display result
        display_result(user_choice, computer_choice, result)
        
        -- Display current score
        print("\nCurrent Score - You: " .. user_score .. " | Computer: " .. computer_score .. " | Ties: " .. ties)
        print(string.rep("-", 50))
    end
end

main()
