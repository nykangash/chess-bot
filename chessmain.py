notation_row = {
    7:"1",
    6:"2",
    5:"3",
    4:"4",
    3:"5",
    2:"6",
    1:"7",
    0:"8"
}
notation_col = {
    0:"a",
    1:"b",
    2:"c",
    3:"d",
    4:"e",
    5:"f",
    6:"g",
    7:"h"
}

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
    

class Move:
    def __init__(self, starting_sq, ending_sq, gamestate_instance):
        super().__init__()
        self.gamestate_instance = gamestate_instance
        self.starting_row = starting_sq[0]
        self.starting_col = starting_sq[1]
        self.ending_row = ending_sq[0]
        self.ending_col = ending_sq[1]
        self.piecemove = self.gamestate_instance.board[self.starting_row][self.starting_col]
        self.piecedest = self.gamestate_instance.board[self.ending_row][self.ending_col]
    
    def logmoves(self):
        main_move = (notation_col[self.starting_col]+notation_row[self.starting_row], notation_col[self.ending_col]+ notation_row[self.ending_row ])
        self.gamestate_instance.movelog.append(main_move)
    def movepiece(self):
         if self.gamestate_instance.board[self.starting_row][self.starting_col] != "--": 
            self.logmoves()
            self.gamestate_instance.board[self.ending_row][self.ending_col] = self.piecemove
            self.gamestate_instance.board[self.starting_row][self.starting_col] = "--"
         else:
             return False 
        


