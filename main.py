
# Jayden Murillo
# Made: 11.3.25
# Last Change: 11.12.25

import random
import inquirer3
import os
import time

WORD_LIST = []
WORD_LEN = 5
USER_LIVES = 5
level = 1

def check_level():
    pass
    

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
    USER_ATTEMPTS = 1 # This take into account the first attempt, since if it's equal to 
    print("[-] Welcome to Jayden's WORDLE. You Have" , USER_LIVES, "Lives In Order To Try To Guess The Word Correctly or Else You Lose! Goodluck ;).")

    while True:
        target = WORD_LIST[random_val]
        print(target)
        guess = input(f"[-] Please enter a {str(WORD_LEN)} letter word :): ")
        answer = ["Bascat" for i in range(len(target))]

        if USER_ATTEMPTS == USER_LIVES and guess != target:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[!] Incorrect! You Have Now Run Out Of Lives. The Correct Word Was...",target)
            time.sleep(2.5)
            end_options = prompt_menu("You Lost! Would You Like To Play Again?", ["YES", "NO"])

            match end_options:
                case "YES":
                    play_game()
                case "NO":
                    exit()

        elif guess == target:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[!] Correct! Winner Winner Chicken Dinner!")
            time.sleep(2.5)
            end_options = prompt_menu("You Won! Would You Like To Play Again? (If You Do The Target Word Will Be Changed)", ["YES", "NO"])
            
            match end_options:
                case "YES":
                    play_game()
                case "NO":
                    exit()
        
        elif USER_ATTEMPTS == USER_LIVES and guess == target:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[!] Correct! Winner Winner Chicken Dinner!")
            time.sleep(2.5)
            end_options = prompt_menu("You Won! Would You Like To Play Again? (If You Do The Target Work Will Be Changed)", ["YES", "NO"])
            
            match end_options:
                case "YES":
                    play_game()
                case "NO":
                    exit()

        else:
            USER_ATTEMPTS += 1
            for g_digit in range(len(guess)):
                for t_digit in range(len(target)):
                    if guess[g_digit] == target[t_digit]:
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
    answer = prompt_menu("Please Select A Level",["Very Easy","Easy", "Medium ","Hard", "Impossible"])

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
    answer = prompt_menu("Please Select The Amount Of Lives You Want", ["1 Life", "2 Lives","3 Lives","4 Lives", "5 Lives"])


    match answer:
        case "5 Lives":
            print("[-] You Now Have 5 Lives... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        case "4 Lives":
            USER_LIVES = 4
            print("[-] You Now Have 4 Lives... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES

        case "3 Lives":
            USER_LIVES = 3
            print("[-] You Now Have 3 Lives... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES

        case "2 Lives":
            USER_LIVES = 2
            print("[-] You Now Have 2 Lives... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES

        case "1 Lives":
            USER_LIVES = 1
            print("[-] You Now Have 1 Life... ")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            return USER_LIVES

def adjust_word_length():
    pass
        


def main():
    while True:
            print("[-] Current Difficulty Level: Medium")
            print("[-] Current Word Length:", WORD_LEN)
            print("[-] Current Lives:",USER_LIVES)


            response = prompt_menu("Please Select an option", ["Exit", "Difficulty Levels","Change Lives", "Change Word Length", "Play Game"])

            match response:
                case "Exit":
                    print("Thanks For Visiting!")
                    exit()
                case "Difficulty Levels":
                    adjust_game_diff()
                case "Change Lives":
                    adjust_game_lives()
                case "Change Word Length":
                    adjust_word_length()
                case "Play Game":
                    play_game()
                

        





if __name__ == "__main__":
    main()
