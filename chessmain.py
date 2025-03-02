'''
            TODO-FIXED:     UNDO FUNCTION BREAKS THE MULTIPLE LINE GAMES
                            LIKE IF WE HAVE A 10 MOVE GAME AND UNDO 3 MOVES 
                            AND THEN PLAY NEW MOVES FROM THAT PART OF GAME
                            THEN undo_move() & do_move() WILL NOT FUNCTION CURRECTLY.
                            IT NEEDS A FIX
            
            TODO-FIXED:     SAME NEEDS LIKE undo_move() FOR do_move()

'''



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
        self.whitetomove = True
        self.movelog = []
        self.moves_cp = []
    
    
    def movepiece(self, move):
        if len(self.moves_cp) > 0:
            self.moves_cp = []

        if self.board[move.starting_row][move.starting_col] != "--": 
            if self.whitetomove and self.board[move.starting_row][move.starting_col][0] == "w":
    
                move.logmoves()
                self.board[move.ending_row][move.ending_col] = move.peiceMoved
                self.board[move.starting_row][move.starting_col] = "--"
                self.whitetomove = not self.whitetomove     
            
            if  self.whitetomove == False and self.board[move.starting_row][move.starting_col][0] == "b":
                move.logmoves()
                self.board[move.ending_row][move.ending_col] = move.peiceMoved
                self.board[move.starting_row][move.starting_col] = "--"
                self.whitetomove = not self.whitetomove
                
        else:
    
            return False        
    
    
    def undo_move(self, move):  
        '''
            simply replace the latest move with the older one...(BROKEN) 

            
            TODO:   GET CORRECT CORDINATION OF SQUARES FROM Move CLASS SO MAKE 
                    undo_move() MORE OPTIMIZED BY REMOVING THOSE  row n col CALCULATIONS 

        '''
        
        
        
        if len(self.movelog) > 0:
                
            move_should_be_reversed = self.movelog.pop() 

            ending_col =    [key for key, val in notation_col.items() if val == move_should_be_reversed[0][0]]      #   the important thing here is ending_* variabels are the cordination  
            ending_row =    [key for key, val in notation_row.items() if val == move_should_be_reversed[0][1]]      #   we want our peice picture in it, so ending_* is 
            starting_col =  [key for key, val in notation_col.items() if val == move_should_be_reversed[1][0]]      #   [0][0] of our "move_should_be_reversed"
            starting_row =  [key for key, val in notation_row.items() if val == move_should_be_reversed[1][1]]
            
            self.board[ending_row[0]][ending_col[0]] = move_should_be_reversed[2]
            self.board[starting_row[0]][starting_col[0]] = move_should_be_reversed[3]
            
            self.moves_cp.append(move_should_be_reversed)    
            self.whitetomove = not self.whitetomove
    
        
    def do_move(self, move):
        '''
            this function works like undo func so nothing new here
            
            TODO:       GET CORRECT CORDINATION OF SQUARES FROM Move CLASS SO MAKE 
                        do_move() MORE OPTIMIZED BY REMOVING THOSE  row n col CALCULATIONS  
        '''
        
        if len(self.moves_cp) > 0:
                
            move_should_be_reversed = self.moves_cp.pop() 
            
            ending_col =    [key for key, val in notation_col.items() if val == move_should_be_reversed[0][0]]   #      the important thing i mentioned before in undo function 
            ending_row =    [key for key, val in notation_row.items() if val == move_should_be_reversed[0][1]]
            starting_col =  [key for key, val in notation_col.items() if val == move_should_be_reversed[1][0]] 
            starting_row =  [key for key, val in notation_row.items() if val == move_should_be_reversed[1][1]]
            
            self.board[starting_row[0]][starting_col[0]] = move_should_be_reversed[2]
            self.board[ending_row[0]][ending_col[0]] = move_should_be_reversed[3]
            
            self.movelog.append(move_should_be_reversed)
            self.whitetomove = not self.whitetomove
            
            
            
            
class Move:
    
    def __init__(self, starting_sq, ending_sq, gamestate_instance):
        
        self.gamestate_instance = gamestate_instance
        self.starting_row = starting_sq[0]
        self.starting_col = starting_sq[1]
        self.ending_row = ending_sq[0]
        self.ending_col = ending_sq[1]
        self.peiceMoved = self.gamestate_instance.board[self.starting_row][self.starting_col]
        self.peiceCaptured = self.gamestate_instance.board[self.ending_row][self.ending_col]


    def logmoves(self):
        
        main_move = (notation_col[self.starting_col]+notation_row[self.starting_row], notation_col[self.ending_col]+ notation_row[self.ending_row ], self.peiceMoved, self.peiceCaptured )
        self.gamestate_instance.movelog.append(main_move)
