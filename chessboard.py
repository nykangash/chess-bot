import pygame as p
import chessmain



p.init()                                #   initialize Pygame

DIMENTIONS = 8                          #   we're going to draw a Rect 8 times with the size of SQ_size 
width = height = 512                    #   we choose this because it's on power of two and make the job easy for us
MAX_FPS = 15
SQ_Size = height//DIMENTIONS            #   used for square sizes
images = {}                             #   for store our piece images that is a heavy job for us and need to handle it one time


def imageload():
    '''
        function to load images (do it in one process to have a efficent way)
    '''

    
    pieces = ["wQ", "wK", "wB", "wN", "wR", "bQ", "bK", "bB", "bN", "bR", "bP", "wP"] 
    for piece in pieces: 
        images[piece] = p.image.load("assets/"+ piece +".png")



def drawGameState(screen, gs):
    '''
        main function to handle drawing actual board and piece images that loaded in images dict before
        and actually idk why even we write this function and put another two functions in it 
        but anyway
        maybe it's for readability
    '''


    drawboard(screen)
    drawpieces(screen, gs.board)

    

def drawboard(screen):
        '''
            function for draw the board 
            board color scheme can be handled here in the "colors" variable
            color picking method here is that we can devide Row number of a square to the Column number 
            and some of them are odd and some of them are even and we have a binary situation with (r+c)%2
            that return us a 1 or 0 so with that we can choose the color from colors

        '''


        colors = [p.Color("white"), p.Color("grey")]
        for r in range(DIMENTIONS):
            for c in range(DIMENTIONS):
              color = colors[((r+c)%2)]
              p.draw.rect(screen, color, p.Rect(c*SQ_Size, r*SQ_Size, SQ_Size, SQ_Size))  



def drawpieces(screen, board):
        '''
            draw assests on board bassed on initial game state we have on chessmain.py and blit them
            nothing special
        '''


        for r in range(DIMENTIONS):
             for c in range(DIMENTIONS):
                  piece = board[r][c]
                  if piece != "--":
                        screen.blit(images[piece], p.Rect(c*SQ_Size, r*SQ_Size, SQ_Size, SQ_Size))



def main():
    '''
        main game function

    '''

    
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()                          # nothing special => default pygame command to setup display screen
    
    
    gs = chessmain.Gamestate()  #   create a instace for the game we want to play to have attribute and methods so  
                                #   we use them in game
                                #   it gives us ability to implement more features
    
    imageload() 
    
    sqSelected = ()                 #   variables to store selected squares by mouse so we can move them
    move_positions = []             #   we need two vars so we can have both starting square and ending square the 
                                    #   player wants
    
    running = True
    while running:
    
        for e in p.event.get():
    
            if e.type == p.QUIT:
                running = False
    
            elif e.type == p.MOUSEBUTTONDOWN:
                mouse_location = p.mouse.get_pos()
                col = mouse_location[0] // SQ_Size
                row = mouse_location[1] // SQ_Size
                print(row, '   ', col)
                if sqSelected == (row, col):
                     sqSelected = ()
                     move_positions = []
            
                else: 
                     sqSelected = (row, col)
                     move_positions.append(sqSelected)
    
                     if len(move_positions) == 2:
                        move = chessmain.Move(move_positions[0], move_positions[1], gs)
                        move.white_legal_moves()
                        gs.movepiece(move)
                        sqSelected = ()
                        move_positions = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_LEFT:    
                                            #   TODO :      HERE THE move OBJ THAT WE PASS TO THE undo_move() & do_move() HAS A "is possibly unbound" WARNING.
                                            #               CHECK IT OUT AND FIX IT IF POSSIBLE...
                    gs.undo_move(move)
                elif e.key == p.K_RIGHT:
                    gs.do_move(move)
        drawGameState(screen, gs)
    
        p.display.flip()
        clock.tick(MAX_FPS)

p.quit()



if __name__ == "__main__":
    main()  