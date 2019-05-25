from tic_tac_toe import Board
import copy
import re

class Game(object):

    def __init__(self):

        self._board = Board()
        self.state = 1
        self.turns = 0

    def _get_cell(self):

        while True:
            query = input("Please enter a cell you wish to fill(e.g. x,y): ")
            check = re.compile('[1-3]')
            cell = check.findall(query)
            try:
                
                if cell is None or len(cell) != 2 or any(x == None for x in cell):

                    raise KeyError

                cell = [int(x)- 1 for x in cell]
                if self._board[cell[0]][cell[1]] != 0:

                    raise ValueError

                return cell

            except KeyError:

                print("Incorrect input, please try again")
                continue

            except ValueError:

                print("That cell is already filled, please select another one")
                continue
            
    def play_turn(self):

        cell = self._get_cell()
        self._board.make_move(cell)
        
        print(self)
        print('-'*10)
        state = self._board.has_winner()
        if state == -1:
            self.state = 0
            print(self.victory_scenario(True))
            return True

        elif state == 2:

            return None
        board1 = copy.deepcopy(self._board)
        board1.make_random_move()
        board2 = copy.deepcopy(self._board)
        board2.make_random_move()
        best_result = max(board1, board2, key=lambda x: x.compute_score())
        self._board = best_result
        print(self)

    def victory_scenario(self, is_player=False):
        if is_player == None:
            return "Draw!"
        return "The {} wins!".format("player" if is_player == True else "computer")

    def play_game(self):

        while self.state != 0:

            turn = self.play_turn()
            self.turns += 1
            if turn == True:
                
                print('-'*10)
                return None

            if self.turns == 5:
                
                self.state = 0
                print(self.victory_scenario(None))
                print('-'*10)
                return None
           
            if self._board.has_winner():

                self.state = 0
                print('-'*10)
                print(self.victory_scenario())
                print('-'*10)
                return None

            
    def __str__(self):

        return self._board.__str__()

if __name__ == "__main__":
    
    g1 = Game()
    g1.play_game()
