
# Jayden Murillo
# Made: 11.3.25
# Last Change: 11.17.25

import random 
import inquirer3 # Imports the random, inquirer3, os, and time pacakges so that they can be used in the code
import os
import time

WORD_LIST = [] # The placeholder list for all of our words from words.alpha.txt
WORD_LEN = 5 # The default word length when the user enters the program
USER_LIVES = 5 # The default number of lives/attempts the user hasin order to guess the target word when they first enter the program
level = "" # The placeholder string for the level on which the user is on, this will be determined based on their word lengths and lives


def check_diff_level():  # This function checks what difficulty level the user is currently at-
    #-(Based on the pre-set levels given to them) and returns it into the level variable so that it can be displayed to the user
    global WORD_LEN
    global level # This refrences the variables we already have outside the function and lets us use them properly without error.
    global USER_LIVES

    if WORD_LEN == 3 and USER_LIVES == 15:
        level = "Very Easy" # If the Word length is 3 and the lives the user has is 15, then the level they're on is "Very Easy"
        return level # It then returns that level they're on, so level now actually equals the level the user's on as a string, so that it can be displayed to the user
    elif WORD_LEN == 4 and USER_LIVES == 10:
        level = "Easy" # If the word length is equal to 4 and the lives the user has is 10, then the level they're on is "Easy"
        return level # It then returns that level they're on, so level now actually equals the level the user's on as a string, so that it can be displayed to the user
    elif WORD_LEN == 5 and USER_LIVES == 5:
        level = "Medium" # If the word length is 5 and the lives the user has is 5, then the level they're on is "Medium"
        return level # It then returns that level they're on, so level now actually equals the level the user's on as a string, so that it can be displayed to the user
    elif WORD_LEN == 7 and USER_LIVES == 3:
        level = "Hard" # If the word length is 7 and the lives the user has is 3, then the level they're on is "Hard"
        return level # It then returns that level they're on, so level now actually equals the level the user's on as a string, so that it can be displayed to the user
    elif WORD_LEN == 10 and USER_LIVES == 1:
        level = "Impossible" # If the word length is 10 and the lives the user has is 1, then the level they're on is "Impossible"
        return level # It then returns that level they're on, so level now actually equals the level the user's on as a string, so that it can be displayed to the user
    else:
        level = "Custom" # If the word length and the lives the user has is anything other than these conditions then the user is on a 
        return level # "Custom" level because they changed the word length or lives manually so that it does not equal the pre-set
        # Levels above. It then returns that level they're on, so level now actually equals the level the user's on as a string, so that
        # It can be displayed to the user
    

def extract_words(): # This function appends/puts words into WORD_LIST from the file words_alpha.txt based on current word length
    try: # try - executes code that should work but can potentially raise an exception or error 
        with open("assets/words_alpha.txt", "r") as file:
            for word in file: # Opens the file in read mode and automatically closes it when were done, reads every word in the file,
                            # then if a word is equal to the word length, the word will go into the WORD_LIST
                if len(word.strip()) == WORD_LEN:
                    WORD_LIST.append(word.strip())

        return WORD_LIST # Then after it goes through every word in words_alpha.txt, checks the word length and either appends the word 
        # In the WORD_LIST or not, it returns the WORD_LIST, so the the list is made up of words at a certain word length

    except FileNotFoundError: # This only executes when the file is not found for this code, when the file does not exist and causes a error
        print("[!] ERROR! FILE NOT FOUND") # What it prints if the file is not found to the user


def get_random_number(): # This function gets a random number between 0 and the length of the WORD_LIST, so that we can get a random word from the list
    value = random.randint(0, len(WORD_LIST)) # Creates a variable that equals the random number between 0 and the length of WORD_LIST
    return int(value)  # Returns the variable/random number as a integer or number rather than a string


def play_game(): # This function is what happens when the user decides to select the option to play the game
    global USER_LIVES # References the variables outside the function so that we can use them without errors
    global WORD_LEN
    extract_words() # Calls the extract_words function to generate a word list based on the current word length
    random_val = get_random_number() # Makes random_val equal the random number from the function get_random_number
    USER_ATTEMPTS = 1 # This is the number of attempts the user has  done. It's currently at 1 so that the number of lives
    # the user has remaining is displayed cleaner and makes more sense.
    print("[-] You Have" , USER_LIVES, "Lives In Order To Try To Guess The Target Word Correctly or Else You Lose! Goodluck!")
    # Tells the user how many lives/tries they have total in order to guess the target word

    while True: # This makes it so that the code continues forever until something is returned 
        target = WORD_LIST[random_val] # Makes target equal a word in the word list based on the random number generated, so it's randomized.
        answer = ["Bascat" for i in range(len(target))] # This helps us later to give letter feedback to the user from what they incorrectly guessed
        # compared to the target word by printing out Chopy (Right letter in the right spot), Storts(Right letter but wrong spot), or Bascat (Letter is not in target word) for each of the letters in the incorrect guess. 
        # Bascat is in every single index  for answer unless changed so if an index does not have chopy or storts in it then it proves bascat to be true and just keeps it there to make it easier


        def validate_user_guess(): # Function that checks the users guess length and make sure it's equal to the word length
            try: # try - executes code that should work but can potentially raise an exception or error
                guess = input(f"[-] Please enter a {str(WORD_LEN)} letter word: ") # Lets the user input their guess
                
                if len(guess.strip()) == WORD_LEN: # If the length of the users guess is equal to the word length then it returns the user's guess
                    return guess
                
                else: # If the length of the users guess is not equal to the word length then this code executes
                    print("[!] ERROR! PLEASE ENTER A", WORD_LEN,"LETTER WORD! IF NOT THEN YOUR GUESS WILL NOT COUNT AND YOU WILL STILL WASTE A LIFE!") # Prints out an error to the user and still wastes one of the users lives
                    guess = "" # The users guess is now nothing so that it does not count and gets no feedback since it does not equal word length
                    return guess # Returns that empty guess so the user does not get letter feedback since their guess was not equal to the word length
                
            except: # Prints out a error message to the user if anything they did caused an error in the code
                print("[!] ERROR! ENTER A", WORD_LEN, "LETTER WORD!")
        
        USER_GUESS = validate_user_guess() # Sets the users guess equal to the varibale USER_GUESS

        # If the users attemps and the lives are equal and the users guess does not equal the target word then this code executes
        if USER_ATTEMPTS == USER_LIVES and USER_GUESS != target:
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            print("[!] Incorrect! You Have Now Run Out Of Lives. The Correct Word Was...",target) 
            # Prints that the users guess was wrong and that they're out of lives, then prints what the correct word was
            time.sleep(1) # Delays the next code execution by 1s
            # Prompts the user if they want to play again after they lost and creates an inquirer3 menu for them to use by calling the prompt_menu function
            end_options = prompt_menu("You Lost! Would You Like To Play Again?", ["YES", "NO"]) 

            match end_options: # Executes code based on what the user selects
                case "YES": # If the user selects the YES option on the menu, they're taken back to the main menu so that they can change their settings(If they want) and play again
                    main()
                case "NO": # If the user selects the NO option on the menu, we thank them for playing the game and then exits them from the program
                    print("[!] Thank You For Playing \n")
                    exit()

        # If the users guess equals to target word then this code executes
        elif USER_GUESS == target:
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            print("[!] Correct! Winner Winner Chicken Dinner!") # Prints that the user correctly guessed the word
            time.sleep(1) # Delays the next code execution by 1s
            # Calls the prompt_menu function to make a menu for the user that prompts the user if they want to play again and gives them YES or NO options
            end_options = prompt_menu("You Won! Would You Like To Play Again?", ["YES", "NO"])
            
            match end_options: # Executes code based on what the user selects
                case "YES": # If the user selects the YES option on the menu, they're taken back to the main menu so that they can change their settings(If they want) and play again
                    main()
                case "NO": # If the user selects the NO option on the menu, we thank them for playing the game and then exits them from the program
                    print("[-] Thank You For Playing \n")
                    exit()
        
        else: # If the user still has lives but still incorrectly guesses the target word then this code executes
            USER_ATTEMPTS += 1 # Increases the users attempts accordingly
            for g_digit in range(len(USER_GUESS)): # g_digit is the index for each letter in the users guess
                for t_digit in range(len(target)): # t_digit is the index for each letter in the target word 
                    if USER_GUESS[g_digit] == target[t_digit]: # If the one of users letters in their guess is equal to one of the target word letters
                        if g_digit == t_digit: # And if they both letters have the same index/in the same spot
                            answer[g_digit] = "Chophy" # Then it stores chopy for that same index for the letter feedback to the user
                        else: # If they don't have the same index but since one of letters in the guess is equal to one of the letters in the target word
                            answer[g_digit] = "Storts" # Then it stores storts in that index for letter feedback to the user

        print(answer) # Prints the users letter feedback for their guess compared to the target word
        print("[-] Lives Remaining:", USER_LIVES-USER_ATTEMPTS + 1) # Prints out how many lives the user has remaining.
        # The + 1 is there to make display the lives remaining to the user cleaner and in a way that makes more sense. 
        # It makes it so that it doesn't say 0 lives remaining and still lets the user guess, instead it says 1 life remaining, which makes sense.


def prompt_menu(messages, user_choices): # Function that uses inquirer3 list to make it easy to print out a menu for the user with options.
    # messages and user_choices are parameters that we can give values when we call the function to make a menu as we want it
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices) # Makes the menu using inquirer3 list and by using the 
        # parameters we can just assign values to them in order to make the menu/inquirer3 list say what we want and give whatever options we want it to.
    ]

    answer = inquirer3.prompt(menu) # This prompts the menu so it prints it out to the user and they can use it to select what they want
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code

    return answer['choice'] # This basically returns the inquirere3 list menu so we can just assign values for the parameters to make our menu say what we need and have the options we want to give


def adjust_game_diff(): # Function that allows the user to change the games difficulty by allowing them to select pre-set levels
    global USER_LIVES
    global WORD_LEN # References the variables outside the function so that we can use them without errors
    # Calls the prompt_menu function in order to make a menu for the user that prompts them to select a difficulty level and gives them pre-set difficulty level options they can choose from
    answer = prompt_menu("Please Select A Level",["Very Easy","Easy", "Medium","Hard", "Impossible"])

    match answer: # Executes code based on what the user selects
        case "Very Easy":
            USER_LIVES = 15
            WORD_LEN = 3 # If the user selects "Very Easy" then their lives are 15 and their word length is 3. Then it returns these values so that USER_LIVES and WORD_LEN is changed to the these numbers. 
            return USER_LIVES, WORD_LEN
        case "Easy":
            USER_LIVES = 10
            WORD_LEN = 4 # If the user selects "Easy" then their lives are 10 and their word length is 4. Then it returns these values so that USER_LIVES and WORD_LEN is changed to the these numbers.
            return USER_LIVES, WORD_LEN
        case "Medium":
            USER_LIVES = 5
            WORD_LEN = 5 # If the user selects "Medium" then their lives are 5 and their word length is 5. Then it returns these values so that USER_LIVES and WORD_LEN is changed to the these numbers.
            return USER_LIVES, WORD_LEN
        case "Hard":
            USER_LIVES = 3
            WORD_LEN = 7 # If the user selects "Hard" then their lives are 3 and their word length is 7. Then it returns these values so that USER_LIVES and WORD_LEN is changed to the these numbers.
            return USER_LIVES, WORD_LEN
        case "Impossible":
            USER_LIVES = 1
            WORD_LEN = 10 # If the user selects "Impossible" then their lives are 1 and their word length is 10. Then it returns these values so that USER_LIVES and WORD_LEN is changed to the these numbers.
            return USER_LIVES, WORD_LEN
    

def adjust_game_lives(): # Function that allows the user to change how many lives they have
    global USER_LIVES # References the variable outside the function so that we can use them without errors
    # Calls the prompt_menu function in order to make a menu for the user that prompts them to select the number of lives they want and gives them options to do that (including a custom option).
    answer = prompt_menu("Please Select The Amount Of Lives You Want", ["1 Life", "2 Lives","3 Lives","4 Lives", "5 Lives","Custom"])

    match answer: # Executes code based on what the user selects
        case "Custom": # If the user selects the "Custom" option then it first validates the users input for the number of lives they 
        # want and if their input passes certain condtions then they get that number of lives but it not then they keep inputting until they fulfill the conditions
            def validate_custom_lives(): # Function that validates the number of lives that a user can get in the custom option
                while True: # This makes it so that the code continues forever until something is returned 
                    try: # try - executes code that should work but can potentially raise an exception or error
                        # Lets the user input the number of lives they want as long as it's between 1-20
                        lives = int(input("[-] Please Enter An Integer For The Number Of Lives You Would Like To Have (It Can ONLY Be Between 1 And 20): "))
                        if lives >= 1 and lives <= 20:
                            return lives       # If the users input is between 1-20, then it returns their input
                        else: # If their input is not between 1-20 then they get an error message and have to keep inputting until their input fulfills the conditions (a number between 1-20)
                            print("[!] ERROR! THE NUMBER OF LIVES CAN ONLY BE BETWEEN 1 AND 20") 
                        
                    except: # Prints out a error message to the user if anything they did caused an error in the code such as enter a string instead of an integer
                        print("[!] ERROR! PLEASE ENTER AN INTEGER BETWEEN 1 AND 20!")
            
            custom_lives = validate_custom_lives() # Sets the variable custom_lives equal to the returned number of lives the user wanted

            USER_LIVES = custom_lives # Makes the users lives equal to the number of lives they want
            print("[!] You Now Have", USER_LIVES, "Lives...") # Tells the user how many lives they now have 
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return USER_LIVES # Returns the users lives which is now equal to the number of lives they wanted
            
        case "5 Lives":
            USER_LIVES = 5 # Makes the users lives equal to the number of lives they want
            print("[-] You Now Have",USER_LIVES,"Lives... ") # Tells the user how many lives they now have 
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return USER_LIVES # Returns the users lives which is now equal to the number of lives they wanted
        case "4 Lives":
            USER_LIVES = 4 # Makes the users lives equal to the number of lives they want
            print("[-] You Now Have",USER_LIVES,"Lives... ") # Tells the user how many lives they now have 
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return USER_LIVES # Returns the users lives which is now equal to the number of lives they wanted
        case "3 Lives":
            USER_LIVES = 3 # Makes the users lives equal to the number of lives they want
            print("[-] You Now Have",USER_LIVES,"Lives... ") # Tells the user how many lives they now have 
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return USER_LIVES # Returns the users lives which is now equal to the number of lives they wanted

        case "2 Lives":
            USER_LIVES = 2 # Makes the users lives equal to the number of lives they want
            print("[-] You Now Have",USER_LIVES,"Lives... ") # Tells the user how many lives they now have 
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return USER_LIVES # Returns the users lives which is now equal to the number of lives they wanted

        case "1 Life":
            USER_LIVES = 1 # Makes the users lives equal to the number of lives they want
            print("[-] You Now Have",USER_LIVES,"Life... ") # Tells the user how many lives they now have
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return USER_LIVES # Returns the users lives which is now equal to the number of lives they wanted


def adjust_word_length():
    global WORD_LEN # References the variable outside the function so that we can use them without errors
    # Calls the prompt_menu function in order to make a menu for the user that prompts them to select the word length they want and gives them options to do that (including a custom option).
    answer = prompt_menu("Please Select The Word Length You'd Like For The Target Word", ["2 Letters","3 Letters","4 Letters", "5 Letters","6 Letters","Custom"])

    match answer: # Executes code based on what the user selects
        case "3 Letters":
            WORD_LEN = 3 # Makes the users word length equal to the word length they want
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ") # Tells the user the word length they now have
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return WORD_LEN # Returns the users word length which is now equal to the word length they wanted
        case "4 Letters":
            WORD_LEN = 4 # Makes the users word length equal to the word length they want
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ") # Tells the user the word length they now have
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return WORD_LEN # Returns the users word length which is now equal to the word length they wanted
        case "5 Letters":
            WORD_LEN = 5 # Makes the users word length equal to the word length they want
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ") # Tells the user the word length they now have
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return WORD_LEN # Returns the users word length which is now equal to the word length they wanted
        case "6 Letters":
            WORD_LEN = 6 # Makes the users word length equal to the word length they want
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ") # Tells the user the word length they now have
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return WORD_LEN # Returns the users word length which is now equal to the word length they wanted
        case "7 Letters":
            WORD_LEN = 7 # Makes the users word length equal to the word length they want
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ") # Tells the user the word length they now have
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return WORD_LEN # Returns the users word length which is now equal to the word length they wanted
        case "Custom":
            def validate_word_length(): # Function that validates the word length that a user can get in the custom option
                while True: # This makes it so that the code continues forever until something is returned
                    try: # try - executes code that should work but can potentially raise an exception or error
                        # Lets the user input the word length they want as long as it's between 3-20
                        length = int(input("[-] Please Enter An Integer For The Word Length You'd Like Your Target Word To Have (It Can ONLY Be Between 3 And 20): "))
                        if length >= 3 and length <= 20:
                            return length # If the users input is between 3-20, then it returns their input
                        else:# If their input is not between 3-20 then they get an error message and have to keep inputting until their input fulfills the conditions (a number between 3-20)
                            print("[!] ERROR! THE WORD LENGTH CAN ONLY BE BETWEEN 3 AND 20") 
                        
                    except: # Prints out a error message to the user if anything they did caused an error in the code such as enter a string instead of an integer
                        print("[!] ERROR! PLEASE ENTER AN INTEGER BETWEEN 3 AND 20!")
            
            WORD_LEN = validate_word_length() # Makes the users word length equal to the word length they want
            print("[-] The Target Word Is Now",WORD_LEN, "Letters Long... ") # Tells the user the word length they now have
            time.sleep(1) # Delays the next code execution by 1s
            os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code
            return WORD_LEN # Returns the users word length which is now equal to the word length they wanted



def main(): # Function where everything is called/function that contains the entire programs/project
    print("Welcome To Jayden's WORDLE! Enjoy! ") # Welcomes the user into the program
    while True: # This makes it so that the code continues forever until the program is exitted by the user
            check_diff_level() # Calls the check difficulty level in order to display to the user what their difficulty is currently on
            print("[-] Current Settings:")
            print(" - Difficulty Level:", level)
            print(" - Word Length:", WORD_LEN) # Displays to the user their difficulty level, their word length, and the number of lvies they have
            print(" - Lives:",USER_LIVES, "\n")

            # Calls the prompt_menu function in order to make a menu for the user that prompts them to select an option for the main program and it gives the user the options of what they can do in the main program
            response = prompt_menu("Please Select An Option (Use The Arrow Keys, Up & Down, To Go An Option And Press Enter To Select It)", ["Exit", "Change Difficulty Level","Change Lives", "Change Word Length", "Play Game"])

            match response: # Executes code based on what the user selects
                case "Exit":
                    print("[-] Thanks For Visiting! \n") # If the user chooses the "Exit" option then it thanks the user for visting the program and exits the user
                    exit()
                case "Change Difficulty Level":
                    adjust_game_diff() # If the user chooses the "Change Difficulty Level" option then the adjust_game_diff() function is called where the user can change the difficulty of the program
                case "Change Lives":
                    adjust_game_lives() # If the user chooses the "Change Lives" option then the adjust_game_lives() function is called where the user can change their number of lives in the program manually as they want
                case "Change Word Length":
                    adjust_word_length() # If the user chooses the "Change Word Length" option then the adjust_word_length() function is called where the user can change their word length in the program manually as they want
                case "Play Game":
                    play_game() # If the user chooses the "Play Game" option then play_game() function is called where the user can actually play the game (which is basically like wordle)
                

if __name__ == "__main__":
    main()  # Immediately calls the program/main function when it's the main program being run
