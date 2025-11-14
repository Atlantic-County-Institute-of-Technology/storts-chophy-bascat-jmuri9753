
# Jayden Murillo
# Made: 11.3.25
# Last Change: 11.12.25

import random
import inquirer3
import os
import time

WORD_LIST = []
WORD_LEN = 5
DEFAULT_ATTEMPTS = 5


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
    global DEFAULT_ATTEMPTS
    extract_words()
    random_val = get_random_number()
    USER_ATTEMPTS = 0
    print("[-] Welcome to Jayden's WORDLE. You Have" , DEFAULT_ATTEMPTS, "Tries In Order To Guess The Word! Goodluck ;).")

    while True:
        target = WORD_LIST[random_val]
        print(target)
        guess = input("[-] Please enter a 5 letter word :): ")
        answer = ["Bascat" for i in range(len(target))]

        if USER_ATTEMPTS == DEFAULT_ATTEMPTS:
            print("[!] The Correct Word Was..",target)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')

            end_options = prompt_menu("You Lost! Would You Like To Play Again?", ["YES", "NO"])

            match end_options:
                case "YES":
                    play_game()
                case "NO":
                    main()
                    

        if guess == target:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[!] Winner Winner Chicken Dinner!")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            end_options = prompt_menu("You Won! Would You Like To Play Again?", ["YES", "NO"])
            
            match end_options:
                case "YES":
                    play_game()
                case "NO":
                    main()


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
        print("[-] Tries left:", DEFAULT_ATTEMPTS-USER_ATTEMPTS )


        
    

def prompt_menu(messages, user_choices):
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices)
    ]

    answer = inquirer3.prompt(menu)
    os.system('cls' if os.name == 'nt' else 'clear')

    return answer['choice']


def adjust_game_diff():
    global DEFAULT_ATTEMPTS
    answer = prompt_menu("Please Select An Option", ["Level 1 - 5 Lives","Level 2 - 4 Lives", "Level 3 - 3 Lives","Level 4 - 2 Lives", "Level 5 - 1 Life"])


    match answer:
        case "Level 1 - 5 Lives":
            print("[-] You Are Now On Level 1.l. ")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        case "Level 2 - 4 Lives":
            DEFAULT_ATTEMPTS = 4
            print("[-] You Are Now On Level 2... ")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return DEFAULT_ATTEMPTS

        case "Level 3 - 3 Lives":
            DEFAULT_ATTEMPTS = 3
            print("[-] You Are Now On Level 3... ")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return DEFAULT_ATTEMPTS

        case "Level 4 - 2 Lives":
            DEFAULT_ATTEMPTS = 2
            print("[-] You Are Now On Level 4... ")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return DEFAULT_ATTEMPTS

        case "Level 5 - 1 Lives":
            DEFAULT_ATTEMPTS = 1
            print("[-] You Are Now On Level 5... ")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            return DEFAULT_ATTEMPTS

        


def main():
    while True:
            response = prompt_menu("Please Select an option", ["Exit", "Difficulty", "Word Length", "Play Game"])

            match response:
                case "Exit":
                    print("Thanks For Visiting!")
                    exit()
                case "Difficulty":
                    adjust_game_diff()
                case "Word Length":
                    print("Not Yet")
                case "Play Game":
                    play_game()
                

        





if __name__ == "__main__":
    main()
