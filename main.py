from src.algorithms import minimax_search
from src.gameClass import play_game, play_game1
from FiveMiseryGameClass import FiveMisery
from src.players import random_player, smart_player, human_player

from src.TicTacToeGameClass import TicTacToe

play_game(FiveMisery(), dict(X=random_player, O=smart_player(minimax_search)),verbose=True).utility
#play_game(FiveMisery(), dict(O=human_player, X=smart_player(minimax_search)),verbose=True)

#play_game(TicTacToe(),dict(X=random_player,O=smart_player(minimax_search)),verbose=True).utility
