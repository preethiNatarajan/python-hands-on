#!usr/bin/env python2

from random import *

from pip._vendor.distlib.compat import raw_input

player_score = 0
computer_score = 0


def start():
    print("Let's play a game of Hangman with fruit names")
    while game():
        pass
    scores()


def game():
    dictionary = ["apple", "banana", "mango", "kiwi", "papaya", "strawberry"]
    word = choice(dictionary)
    word_len = len(word)
    clue = word_len * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score
    # 1
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        # 2
        if len(letter) == 1 and letter.isalpha():
            # 3
            if letters_tried.find(letter) != -1:
                print("This letter ",letter," was already picked")
            # 3
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                # 4
                if first_index == -1:
                    letters_wrong += 1
                    print("Sorry ",letter," is not in the selected word")
                # 4
                else:
                    print('Congratulations ', letter, " is correct")
                    # 5
                    for i in range(word_len):
                        # 6
                        if letter == word[i]:
                            clue[i] = letter
                        # 6 ended
                    # 5 ended
                # 4 ended
            # 3 ended
        # 2
        else:
            print("Choose another letter")
        # 2 ended
        fun_hangedman(letters_wrong)
        print("".join(clue))
        print("Guesses: ", str(letters_tried))

        # 7
        if letters_wrong == tries:
            print("Game over\nThe word was ", word)
            computer_score += 1
            break
        # 7 ended
        # 8
        if "".join(clue) == word:
            print("You win!\nThe word was ", word)
            player_score += 1
            break
        # 8 ended
    # 1 ended
    return play_again()
    # function game ended


def guess_letter():
    print()
    letter = raw_input("Take a guess [letters a-z]: ")
    letter.strip()
    letter.lower()
    print()
    return letter


def play_again():
    answer = raw_input("Would you like to play again? (y/n) : ")
    if answer in ("y", "Y", "yes", "Yes"):
        return answer
    else:
        print("Bye for now")


def scores():
    global player_score, computer_score
    print("Scores are: Player ", str(player_score), " Computer ", str(computer_score))


def fun_hangedman(hangman):
    graphic = [
        """
            +---------+
            |
            |
            |
            |
            |
         ========================
         """,
        """
         +---------+
         |         |
         |
         |
         |
         |
      ========================
       """,
        """
         +---------+
         |         |
         |         O
         |
         |
         |
     ========================
       """,
        """
          +---------+
          |         |
          |         O
          |         |  
          |
          |
     ========================
        """,
        """
          +---------+
          |         |
          |         O
          |       - | - 
          |
          |
        ========================
        """,
        """
         +---------+
         |         |
         |         O
         |       - | - 
         |        /
         |
        ========================
        """,
        """
                 +---------+
                 |         |
                 |         O
                 |       - | - 
                 |        / /
                 |
               ========================
         """
    ]
    print(graphic[hangman])
    return


if __name__ == '__main__':
    start()
