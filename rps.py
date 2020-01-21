# game of rock paper scissors
# !/usr/bin/env python2

import random
import time

from pip._vendor.distlib.compat import raw_input

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, scissors: paper, paper: rock}

player_score = 0
computer_score = 0


def start():
    print("Let's play a game of rock, paper, scissors")
    while game():
        pass
    scores()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nChoose any of these three numbers : ")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Oops! Please choose 1 or 2 or 3")


def result(player, computer):
    print("Computer chose {0}".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie Game")
    else:
        if rules[player] == computer:
            print("You win")
            player_score += 1
        else:
            print("Comuputer wins")
            computer_score += 1


def play_again():
    answer = raw_input("Would you like to play again? y/n : ")
    if answer in ("y", "Y", "yes", "Yes"):
        return answer
    else:
        print("Thank you for playing so far")


def scores():
    global player_score, computer_score
    print("Scores are: Player = " + str(player_score) + " Computer = " + str(computer_score))

if __name__ == '__main__':
    start()
