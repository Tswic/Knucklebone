from moves import *
from random import randint
from board import *


def game_with_human(depth, hope=None):
    board1, board2 = setup_boards()
    while not board1 and not board2:
        dice = randint(1, 6)
        board1.add_dice(dice, best_move(board1, dice, depth, hope))
        if board1:
            break

        dice = randint(1, 6)
        print_both_board(board1, board2)
        print("tu as tiré un", dice)
        col = int(input("ou veux tu le mettre ? "))
        if board2.lines[col - 1] == 3:
            raise Exception("la ligne", col, "est deja pleine")
        else:
            board2.add_dice(dice, col-1)
        if board2:
            break

    print_both_board(board1, board2)
    t = board1.score_diff()
    if t >= 0:
        print("le robot a gagne de", t, "points")
    else:
        print("le robot a perdu de", -t,  "points")
    return t


def game_between_robot(depth, other_depth=None, hope=None):
    if hope is None:
        hope = [None, None]
    if other_depth is None:
        other_depth = depth
    board1, board2 = setup_boards()
    while not board1 and not board2:
        dice = randint(1, 6)
        t = best_move(board1, dice, depth, hope[0])
        board1.add_dice(dice, t)
        print(dice, "->", t)
        print_both_board(board1, board2)
        if board1:
            break
        dice = randint(1, 6)
        t = best_move(board2, dice, other_depth, hope[1])
        board2.add_dice(dice, t)
        print(dice, "->", t)
        print_both_board(board1, board2)
        if board2:
            break

    t = board1.score_diff()
    if t >= 0:
        print("le premier robot a gagne de", t, "points")
    else:
        print("le deuxieme robot a gagné de", -t,  "points")
    return t


def game_between_human():
    board1, board2 = setup_boards()
    while not board1 and not board2:
        dice = randint(1, 6)
        print()
        print()
        print("### Joueur 1 ###")
        print_both_board(board1, board2)
        print("tu as tiré un", dice)
        col = int(input("ou veux tu le mettre ? "))
        if board1.lines[col - 1] == 3:
            raise Exception("la ligne", col, "est deja pleine")
        else:
            board1.add_dice(dice, col - 1)
        if board1:
            break

        dice = randint(1, 6)
        print()
        print()
        print("### Joueur 2 ###")
        print_both_board(board1, board2)
        print("tu as tiré un", dice)
        col = int(input("ou veux tu le mettre ? "))
        if board2.lines[col - 1] == 3:
            raise Exception("la ligne", col, "est deja pleine")
        else:
            board2.add_dice(dice, col - 1)
        if board2:
            break

    print_both_board(board1, board2)
    t = board1.score_diff()
    if t >= 0:
        print("le Joueur 1 a gagné de", t, "points")
    else:
        print("le Joueur 2 a gagné de", -t, "points")
    return t
