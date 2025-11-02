def get_score_depth(board, depth, hope=0, is_playing=False):
    if depth == 0:
        return board.score_diff()
    avg = []
    for dice in range(1, 7):
        maximum = -100000000
        for col in range(3):
            if board.lines[col] != 3:
                a, b = board.copy()
                a.add_dice(dice, col)
                if a:
                    result = board.score_diff()
                else:
                    result = -get_score_depth(b, depth - 1, hope, not is_playing)
                if result > maximum:
                    maximum = result
        avg.append(maximum)
    if not is_playing:
        return (sum(avg) + hope * max(avg)) / (6 + hope)
    return sum(avg) / 6


def best_move(board, dice, depth, hope=None):
    maximum = None
    index = None
    if hope is None:
        hope = 0
    elif hope == -6:
        hope = -7
    for col in range(3):
        if board.lines[col] != 3:
            a, b = board.copy()
            a.add_dice(dice, col)
            result = -get_score_depth(b, depth, hope)
            if maximum is None:
                maximum = result
                index = col
            elif result > maximum:
                maximum = result
                index = col
    return index
