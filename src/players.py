import random

def smart_player(search_algorithm):
    """A game player who uses the specified search algorithm"""
    return lambda game, state: search_algorithm(game, state)[1]


def random_player(game, state):
    """A game player who  uses random choice to do a next move"""
    return random.choice(list(game.actions(state)))

def human_player(game,state):
    move = int(input("Enter the amount you'd like to add: "))
    while move not in game.actions():
        move = int(input(f"Invalid input, please add one of {game.actions()}: "))
    return move