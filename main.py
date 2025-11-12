
# Jayden Murillo
# Made: 11.3.25
# Last Change: 11.12.25

import random
import inquirer3

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
    print("[-] Welcome to Jayden's WORDLE.")

def prompt_end_menu(messages, user_choices):

    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices)
    ]

    answer = inquirer3.prompt(menu)

    return answer['choice']


def main():
    extract_words()
    random_val = get_random_number()
    play_game()
    target = WORD_LIST[random_val]
    print(target)
    guess = input("[-] Please enter a 5 letter word :). ")
    response = ["Bascat" for i in range(len(target))]

    if guess == target:
        print("You got it!")
    else:
        for g_digit in range(len(guess)):
            for t_digit in range(len(target)):
                if guess[g_digit] == target[t_digit]:
                    if g_digit == t_digit:
                        response[g_digit] = "Chophy"
                    else:
                        response[g_digit] = "Storts"

    print(response)



    # user_response = prompt_end_menu("Please Select an Option", "")




if __name__ == "__main__":
    main()
