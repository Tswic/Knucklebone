class Board:
    def __init__(self, cont_line=None, lines=None, nbr_dices=0, opponent=None):
        if cont_line is None:
            cont_line = [{i: 0 for i in range(1, 7)} for _ in range(3)]
        self.cont_line = cont_line
        if lines is None:
            lines = [0, 0, 0]
        self.lines = lines
        self.nbr = nbr_dices
        self.opponent = opponent

    def add_dice(self, dice, col):
        if col < 0 or 3 <= col:
            raise Exception("impossible to place in col "+str(col))
        if self.lines[col] == 3:
            raise Exception("the col "+str(col)+" is already full")
        if dice < 1 or 6 < dice:
            raise Exception("the dice "+str(dice)+" can't be placed")
        if self.opponent is not None:
            n = self.opponent.cont_line[col][dice]
            self.opponent.cont_line[col][dice] = 0
            self.opponent.lines[col] -= n
            self.opponent.nbr -= n
        self.cont_line[col][dice] += 1
        self.lines[col] += 1
        self.nbr += 1

    def __bool__(self):
        return self.nbr == 9

    def score(self):
        return sum([sum([i*(j[i]**2) for i in j]) for j in self.cont_line])

    def score_diff(self):
        return self.score()-self.opponent.score()

    def copy(self):
        rep = [{i: j[i] for i in j} for j in self.cont_line]
        a = Board(rep, [i for i in self.lines], self.nbr)
        op = self.opponent
        rep1 = [{i: j[i] for i in j} for j in op.cont_line]
        b = Board(rep1, [i for i in op.lines], op.nbr, a)
        a.opponent = b
        return a, b

    def print_board(self):
        col = [[], [], []]
        for i in range(3):
            for k in range(1, 7):
                for des in range(self.cont_line[i][k]):
                    col[i].append(str(k))
            for k in range(3 - self.lines[i]):
                col[i].append(' ')
        for i in range(3):
            rep = ""
            for k in range(3):
                rep += "#"
                rep += col[k][i]
            print(rep+"#")


def setup_boards():
    a = Board()
    b = Board()
    a.opponent = b
    b.opponent = a
    return a, b


def print_both_board(board1, board2):
    board1.print_board()
    print("#######")
    board2.print_board()
    print()


"""
B = Board()
B.add_dice(4,1)
B.add_dice(4,1)
B.add_dice(5,2)
B.add_dice(2,0)
print(B)
print(B.score())
"""