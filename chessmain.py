class Gamestate:
    def __init__(self):
        self.board = [
                        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["--", "--", "--", "--", "--", "--", "--", "--"],
                        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"] 
                        ]
        self.whittosemove = True
        self.movelog = []
    

class Move(Gamestate):
    def __init__(self, starting_sq, ending_sq, board):
        self.starting_row = starting_sq[0]
        self.starting_col = starting_sq[1]
        self.ending_row = ending_sq[0]
        self.ending_col = ending_sq[1]
        self.piecemove = board[self.starting_row][self.starting_col]
        self.piecedest = board[self.ending_row][self.ending_col]
    def movepiece(self, board):
         if board[self.starting_row][self.starting_col] != "--": 
            board[self.ending_row][self.ending_col] = self.piecemove
            board[self.starting_row][self.starting_col] = "--"
         else:
             return False 
        


