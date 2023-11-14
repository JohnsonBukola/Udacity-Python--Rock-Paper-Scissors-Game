import random

# Codes to play the game of Rock, Paper, Scissors between a Human player
# and the Computer. It reports both Player's scores after each round.

moves = ['rock', 'paper', 'scissors']


# The Player class is the parent class for all of the Players in this game
class Player:
    def __init__(self):
        self.count = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.count = 0

    def move(self):
        return random.choice(moves)


class RepeatPlayer(Player):
    def move(self):
        #  Always plays rock
        return 'rock'


class HumanPlayer(Player):
    def __init__(self):
        self.count = 0

    def move(self):
        Human_choice = input("rock, paper or scissors?")
        while Human_choice.lower() not in moves:
            Human_choice = input(
                "invalid response, 'rock', 'paper' or 'scissors'?")
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


# wins fucntion used to determine who beats who
def wins(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def results(self):
        if self.p1.count > self.p2.count:
            print("\n\n*** PLAYER ONE WINS THE GAME!! *** ")
        elif self.p2.count > self.p1.count:
            print("\n\n*** PLAYER TWO WINS THE GAME!! *** ")

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
        print(
            f"Score line Player1: {self.p1.count} vs Player2: {self.p2.count}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("*** Game start! ***")
        for round in range(3):
            print(f"\n\nRound {round}:")
            self.play_round()
        self.results()
        # Another loop in case there was a tie in the first three rounds.
        for round in range(3, 9):
            if self.p1.count == self.p2.count:
                print(f"\n\nRound {round}:")
                self.play_round()
                self.results()
        print("Game over!\n\n")


if __name__ == '__main__':
    player_1 = HumanPlayer()
    player_2 = RandomPlayer()
    game = Game(player_1, player_2)
    game.play_game()
