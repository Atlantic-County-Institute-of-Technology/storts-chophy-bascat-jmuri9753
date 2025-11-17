
# Jayden Murillo
# Made: 11.3.25
# Last Change: 11.16.25

import random
import inquirer3
import os
import time

WORD_LIST = []
WORD_LEN = 5
USER_LIVES = 5
level = ""


def check_diff_level():
    global WORD_LEN
    global level
    global USER_LIVES

    if WORD_LEN == 3 and USER_LIVES == 15:
        level = "Very Easy"
        return level
    elif WORD_LEN == 4 and USER_LIVES == 10:
        level = "Easy"
        return level
    elif WORD_LEN == 5 and USER_LIVES == 5:
        level = "Medium"
        return level
    elif WORD_LEN == 7 and USER_LIVES == 3:
        level = "Hard"
        return level
    elif WORD_LEN == 10 and USER_LIVES == 1:
        level = "Impossible"
        return level
    else:
        level = "Custom"
        return level
    

def extract_words():
    try:
        with open("assets/words_alpha.txt", "r") as file:
            for word in file:
                if len(word.strip()) == WORD_LEN:
                    WORD_LIST.append(word.strip())

        return WORD_LIST

    except FileNotFoundError:
        print("[!] ERROR! FILE NOT FOUND")


def get_random_number():
    value = random.randint(0, len(WORD_LIST))
    return int(value) 


def play_game():
    global USER_LIVES
    global WORD_LEN
    extract_words()
    random_val = get_random_number()
    USER_ATTEMPTS = 1 # This takes into account the first attempt, since it does not on it's own
    print("[-] You Have" , USER_LIVES, "Lives In Order To Try To Guess The Target Word Correctly or Else You Lose! Goodluck!")

    while True:
        target = WORD_LIST[random_val]
        answer = ["Bascat" for i in range(len(target))]


        def validate_user_guess():
            try:
                guess = input(f"[-] Please enter a {str(WORD_LEN)} letter word: ")
                
                if len(guess.strip()) == WORD_LEN:
                    return guess
                
                else:
                    print("[!] ERROR! PLEASE ENTER A", WORD_LEN,"LETTER WORD! IF NOT THEN YOUR GUESS WILL NOT COUNT AND YOU WILL STILL WASTE A LIFE!")
                    guess = ""
                    return guess
                
            except:
                print("[!] ERROR! ENTER A", WORD_LEN, "LETTER WORD!")
        
        USER_GUESS = validate_user_guess()

        if USER_ATTEMPTS == USER_LIVES and USER_GUESS != target:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[!] Incorrect! You Have Now Run Out Of Lives. The Correct Word Was...",target)
            time.sleep(2.5)
            end_options = prompt_menu("You Lost! Would You Like To Play Again? (Hint: If You Do The Target Word Will Be Changed Randomly)", ["YES", "NO"])

            match end_options:
                case "YES":
                    play_game()
                case "NO":
                    print("[!] Thank You For Playing \n")
                    exit()

        elif USER_GUESS == target and USER_ATTEMPTS == USER_LIVES:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[!] Correct! Winner Winner Chicken Dinner!")
            time.sleep(2.5)
            end_options = prompt_menu("You Won! Would You Like To Play Again? (Hint: If You Do The Target Word Will Be Changed Randomly)", ["YES", "NO"])
            
            match end_options:
                case "YES":
                    play_game()
                case "NO":
                    print("[-] Thank You For Playing \n")
                    exit()
        
        else:
            USER_ATTEMPTS += 1
            for g_digit in range(len(USER_GUESS)):
                for t_digit in range(len(target)):
                    if USER_GUESS[g_digit] == target[t_digit]:
                        if g_digit == t_digit:
                            answer[g_digit] = "Chophy"
                        else:
                            answer[g_digit] = "Storts"

        print(answer)
        print("[-] Lives Remaining:", USER_LIVES-USER_ATTEMPTS + 1)     


def prompt_menu(messages, user_choices):
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices)
    ]

    answer = inquirer3.prompt(menu)
    os.system('cls' if os.name == 'nt' else 'clear')

    return answer['choice']


def adjust_game_diff():
    global USER_LIVES
    global WORD_LEN
    answer = prompt_menu("Please Select A Level",["Very Easy","Easy", "Medium","Hard", "Impossible"])

    match answer:
        case "Very Easy":
            USER_LIVES = 15
            WORD_LEN = 3
            return USER_LIVES, WORD_LEN
        case "Easy":
            USER_LIVES = 10
            WORD_LEN = 4
            return USER_LIVES, WORD_LEN
        case "Medium":
            USER_LIVES = 5
            WORD_LEN = 5
            return USER_LIVES, WORD_LEN
        case "Hard":
            USER_LIVES = 3
            WORD_LEN = 7
            return USER_LIVES, WORD_LEN
        case "Impossible":
            USER_LIVES = 1
            WORD_LEN = 10
            return USER_LIVES, WORD_LEN
    

def adjust_game_lives():
    global USER_LIVES
    answer = prompt_menu("Please Select The Amount Of Lives You Want", ["1 Life", "2 Lives","3 Lives","4 Lives", "5 Lives","Custom"])

    match answer:
        case "Custom":
            def validate_custom_lives():
                while True:
                    try:
                        lives = int(input("[-] Please Enter An Integer For The Number Of Lives You Would Like To Have (It Can ONLY Be Between 1 And 20): "))
                        if lives >= 1 and lives <= 20:
                            return lives
                        else:
                            print("[!] ERROR! THE NUMBER OF LIVES CAN ONLY BE BETWEEN 1 AND 20") 
                        
                    except:
                        print("[!] ERROR! PLEASE ENTER AN INTEGER BETWEEN 1 AND 20!")
            
            custom_lives = validate_custom_lives()

            USER_LIVES = custom_lives
            print("[!] You Now Have", USER_LIVES, "Lives...")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES
            
        case "5 Lives":
            USER_LIVES = 5
            print("[-] You Now Have",USER_LIVES,"Lives... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES
        case "4 Lives":
            USER_LIVES = 4
            print("[-] You Now Have",USER_LIVES,"Lives... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES
        case "3 Lives":
            USER_LIVES = 3
            print("[-] You Now Have",USER_LIVES,"Lives... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES

        case "2 Lives":
            USER_LIVES = 2
            print("[-] You Now Have",USER_LIVES,"Lives... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES

        case "1 Life":
            USER_LIVES = 1
            print("[-] You Now Have",USER_LIVES,"Life... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES


def adjust_word_length():
    global WORD_LEN
    answer = prompt_menu("Please Select The Word Length You'd Like For The Target Word", ["2 Letters","3 Letters","4 Letters", "5 Letters","6 Letters","Custom"])

    match answer:
        case "3 Letters":
            WORD_LEN = 3
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return WORD_LEN
        case "4 Letters":
            WORD_LEN = 4
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return WORD_LEN
        case "5 Letters":
            WORD_LEN = 5
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return WORD_LEN
        case "6 Letters":
            WORD_LEN = 6
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return WORD_LEN
        case "7 Letters":
            WORD_LEN = 7
            print("[!] The Target Word Is Now",WORD_LEN, "Letters Long... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return WORD_LEN
        case "Custom":
            def validate_word_length():
                while True:
                    try:
                        length = int(input("[-] Please Enter An Integer For The Word Length You'd Like Your Target Word To Have (It Can ONLY Be Between 3 And 20): "))
                        if length >= 3 and length <= 20:
                            return length
                        else:
                            print("[!] ERROR! THE WORD LENGTH CAN ONLY BE BETWEEN 3 AND 20") 
                        
                    except:
                        print("[!] ERROR! PLEASE ENTER AN INTEGER BETWEEN 3 AND 20!")
            
            WORD_LEN = validate_word_length()
            print("[-] The Target Word Is Now",WORD_LEN, "Letters Long... ")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return WORD_LEN



def main():
    print("Welcome To Jayden's WORDLE! Enjoy! ")
    while True:
            check_diff_level()
            print("[-] Current Settings:")
            print(" - Difficulty Level:", level)
            print(" - Word Length:", WORD_LEN)
            print(" - Lives:",USER_LIVES, "\n")


            response = prompt_menu("Please Select An Option (Use The Arrow Keys, Up & Down, To Go An Option And Press Enter To Select It)", ["Exit", "Change Difficulty Level","Change Lives", "Change Word Length", "Play Game"])

            match response:
                case "Exit":
                    print("[-] Thanks For Visiting! \n")
                    exit()
                case "Change Difficulty Level":
                    adjust_game_diff()
                case "Change Lives":
                    adjust_game_lives()
                case "Change Word Length":
                    adjust_word_length()
                case "Play Game":
                    play_game()
                

if __name__ == "__main__":
    main()
