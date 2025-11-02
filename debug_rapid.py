from moves import *
from board import *
from random import randint


def robot_printless(depth, other_depth=None, hope=None):
    if hope is None:
        hope = [None, None]
    if other_depth is None:
        other_depth = depth
    board1, board2 = setup_boards()
    while not board1 and not board2:
        dice = randint(1, 6)
        t = best_move(board1, dice, depth, hope[0])
        board1.add_dice(dice, t)
        if board1:
            break
        dice = randint(1, 6)
        t = best_move(board2, dice, other_depth, hope[1])
        board2.add_dice(dice, t)
        if board2:
            break

    t = board1.score_diff()
    return t
