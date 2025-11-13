
# Jayden Murillo
# Made: 11.3.25
# Last Change: 11.12.25

import random
import inquirer3
import os
import time

WORD_LIST = []
WORD_LEN = 5


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
    extract_words()
    random_val = get_random_number()
    USER_ATTEMPTS = 0
    TOTAL_TRIES = 5
    print("[-] Welcome to Jayden's WORDLE. You Have" , TOTAL_TRIES, "Tries In Order To Guess The Word")

    while True:
        if USER_ATTEMPTS == TOTAL_TRIES:
            print("[!] The Correct Word Was..",target)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')

            end_options = prompt_end_menu("You Lost! Would You Like To Play Again?", ["YES", "NO"])

            match end_options:
                case "YES":
                    play_game()
                case "NO":
                    main()
                    

            

        target = WORD_LIST[random_val]
        print(target)
        guess = input("[-] Please enter a 5 letter word :): ")
        answer = ["Bascat" for i in range(len(target))]

        if guess == target:
            print("[!] Winner Winner Chicken Dinner!")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            end_options = prompt_end_menu("You Won! Would You Like To Play Again?", ["YES", "NO"])


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
        print("[-] Tries left:", TOTAL_TRIES-USER_ATTEMPTS )


        
    

def prompt_main_menu(messages, user_choices):
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices)
    ]

    answer = inquirer3.prompt(menu)
    os.system('cls' if os.name == 'nt' else 'clear')

    return answer['choice']


def prompt_end_menu(messages, user_choices):
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices)
    ]

    answer = inquirer3.prompt(menu)
    os.system('cls' if os.name == 'nt' else 'clear')

    return answer['choice']

def main():
    while True:
            response = prompt_main_menu("Please Select an option", ["Exit", "Difficulty", "Word Length", "Play Game"])

            match response:
                case "Exit":
                    print("Thanks For Visiting!")
                    exit()
                case "Difficulty":
                    print("Banana")
                case "Word Length":
                    print("Not Yet")
                case "Play Game":
                    play_game()
                

        



    # user_response = prompt_end_menu("Please Select an Option", "")




if __name__ == "__main__":
    main()
