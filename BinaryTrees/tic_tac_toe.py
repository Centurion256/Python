from Trees_easy import linked_binary_tree
import copy
import random

def generate_winning_combinations():
    combinations = []
    for i in range(3):
        combination1 = []
        combination2 = []
        for j in range(3):
            combination1.append((i, j))
            combination2.append((j, i))
        combinations.append(combination1)
        combinations.append(combination2)

    combinations.append([(0, 0), (1, 1), (2, 2)])
    combinations.append([(0, 2), (1, 1), (2, 0)])
    return combinations

class Board:
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0

    NOUGHT_WINNER = 1
    CROSS_WINNER = -1
    DRAW = 2
    NOT_FINISHED = 0

    WINNING_COMBINATIONS = generate_winning_combinations()

    def __init__(self):
        self.cells = [[0] * 3 for _ in range(3)]
        self.last_move = Board.NOUGHT
        self.number_of_moves = 0

    def __getitem__(self, pos):

        return self.cells[pos]

    def make_move(self, cell):
        if self.cells[cell[0]][cell[1]] != 0:
            return False
        self.last_move = -self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        self.number_of_moves += 1
        return True

    def has_winner(self):
       for combination in self.WINNING_COMBINATIONS:
            lst = []
            for cell in combination:
                lst.append(self.cells[cell[0]][cell[1]])
            if max(lst) == min(lst) and max(lst) != Board.EMPTY:
                return max(lst)
       if self.number_of_moves == 9:
           return Board.DRAW

       return Board.NOT_FINISHED

    def make_random_move(self):
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Board.EMPTY:
                    possible_moves.append((i, j))
        cell = random.choice(possible_moves)
        self.last_move = -self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        self.number_of_moves += 1
        return True
    
    def compute_score(self):
        has_winner = self.has_winner()
        if has_winner:
            winner_scores = { Board.NOUGHT_WINNER: 1, Board.CROSS_WINNER: -1, Board.DRAW: 0}
            return winner_scores[has_winner]
        left_board = copy.deepcopy(self)
        right_board = copy.deepcopy(self)
        left_board.make_random_move()
        right_board.make_random_move()
        return left_board.compute_score() + right_board.compute_score()


    def __str__(self):
        transform = {0: " ", 1: "O", -1:"X"}
        return "\n".join(["|".join(map(lambda x: transform[x], row)) for row in self.cells])

if __name__ == "__main__":
    board1 = Board()
    board1.make_random_move()
    board2 = Board()
    board2.make_random_move()
    print(board1)
    print(board1.compute_score())
    print(board2)
    print(board2.compute_score())