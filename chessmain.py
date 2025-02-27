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
        self.moves_cp = []
    
    
    
    def undo_move(self):
        if len(self.movelog) > 0:
                
            move_should_be_reversed = self.movelog.pop() 
            
            ending_col =    [key for key, val in notation_col.items() if val == move_should_be_reversed[0][0]] 
            ending_row =    [key for key, val in notation_row.items() if val == move_should_be_reversed[0][1]]
            starting_col =  [key for key, val in notation_col.items() if val == move_should_be_reversed[1][0]] 
            starting_row =  [key for key, val in notation_row.items() if val == move_should_be_reversed[1][1]]
            
            self.board[ending_row[0]][ending_col[0]] = self.board[starting_row[0]][starting_col[0]]
            self.board[starting_row[0]][starting_col[0]] = "--"
            
            self.moves_cp.append(move_should_be_reversed)    
        
    
        
    def do_move(self):
        
        if len(self.moves_cp) > 0:
                
            move_should_be_reversed = self.moves_cp.pop() 
            
            ending_col =    [key for key, val in notation_col.items() if val == move_should_be_reversed[0][0]] 
            ending_row =    [key for key, val in notation_row.items() if val == move_should_be_reversed[0][1]]
            starting_col =  [key for key, val in notation_col.items() if val == move_should_be_reversed[1][0]] 
            starting_row =  [key for key, val in notation_row.items() if val == move_should_be_reversed[1][1]]
            
            self.board[starting_row[0]][starting_col[0]] = self.board[ending_row[0]][ending_col[0]]
            self.board[ending_row[0]][ending_col[0]] = "--"
            
            self.movelog.append(move_should_be_reversed)    
        


class Move:
    
    def __init__(self, starting_sq, ending_sq, gamestate_instance):
        
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
        
        if self.gamestate_instance.board[self.starting_row][self.starting_col] != "--" and len(self.gamestate_instance.moves_cp) == 0: 
            
            self.logmoves()
            self.gamestate_instance.board[self.ending_row][self.ending_col] = self.piecemove
            self.gamestate_instance.board[self.starting_row][self.starting_col] = "--"

        else:
            
            return False


