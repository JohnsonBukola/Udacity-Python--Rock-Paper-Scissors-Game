import random
import time

#Codes to play the game of Rock, Paper, Scissors between a Human player and the Computer. It reports both Player's scores after each round."""

moves = ['rock', 'paper', 'scissors']

#The Player class is the parent class for all of the Players in this game

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)
    
class Player:
    def __init__(self):
        self.count = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class ComputerPlayer(Player):
    def __init__(self):
        self.count = 0

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        self.count = 0

    def move(self):
        Human_choice = input("rock, paper or scissors?")
        while Human_choice.lower() not in moves:
            Human_choice = input("invalid response, 'rock', 'paper' or 'scissors'?")
        return Human_choice.lower()


class ReflectPlayer(Player):
    def __init__(self):
        self.count = 0
        self.mimic = "rock"

    def learn(self, my_move, their_move):
        self.mimic = their_move
        return self.mimic

    def move(self):
        return self.mimic


class CyclePlayer(Player):
    def __init__(self):
        self.count = 0
        self.cycle = "rock"

    def learn(self, my_move, their_move):
        if my_move == "rock":
            self.cycle = "paper"
        elif my_move == "paper":
            self.cycle = "scissors"
        elif my_move == "scissors":
            self.cycle = "rock"

    def move(self):
        return self.cycle


#wins fucntion used to determine who beats who


def wins(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 picks: {move1}  Player 2 picks: {move2}")
        if wins(move1, move2) is True:
            print("Player1 wins this round")
            self.p1.count += 1
        elif move1 == move2:
            print("It is a TIE")
        else:
            print("player2 wins this round")
            self.p2.count += 1
        print(f"Score board Player1: {self.p1.count} vs Player2: {self.p2.count}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        

    def play_game(self):
        rounds = input("Type number of rounds to play")
        while "." in rounds or float(rounds) <= 0:
            rounds = input("Enter a valid NUMBER like 1,2...")

        print(f"Game start! You have {rounds} rounds, let's go!")
        for round in range(int(rounds)):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.count > self.p2.count:
            print("***Final score: Player1 won!***")
        elif self.p1.count == self.p2.count:
            print("***Final score: Tie!***")
        elif self.p1.count < self.p2.count:
            print("***Final result: Player2 won!***")
        print("Game over!")
        play_again()
        
def exit_program():
    print("Exiting the program...")
    random.exit(0)


decision = ['yes' , 'no']

def play_again():
    print_pause("Would you like to play again?")

    response = input("please, say 'yes' or 'no'")
    while response.lower() not in decision:
        response = input("invalid response, please, say 'yes' or 'no' ")
    #return response.lower()
    
    if decision == "no":
        print_pause("Thanks for playing! See you next time.")
        exit_program()
        
    else:# response == "yes":
        print_pause("Excellent. Restarting the game.")
        game.play_game()
        

if __name__ == '__main__':
    player_1 = HumanPlayer()
    player_2 = ComputerPlayer()
    game = Game(player_1, player_2)
    game.play_game()
