import pygame as p
import chessmain


p.init()

DIMENTIONS = 8                          # we're going to draw a Rect 8 times with the size of SQ_size 
width = height = 512                    # we choose this because it's on power of two and make the job easy for us
MAX_FPS = 15
SQ_Size = height//DIMENTIONS            # used for square sizes
images = {}                             # for store our piece images that is a heavy job for us and need to handle it one time

def imageload():
            pieces = ["wQ", "wK", "wB", "wN", "wR", "bQ", "bK", "bB", "bN", "bR", "bP", "wP"] 
            for piece in pieces: 
                images[piece] = p.image.load("assets/"+ piece +".png")

def drawGameState(screen, gs):
    drawboard(screen)
    drawpieces(screen, gs.board)

    
def drawboard(screen):
        colors = [p.Color("white"), p.Color("grey")]
        for r in range(DIMENTIONS):
            for c in range(DIMENTIONS):
              color = colors[((r+c)%2)]
              p.draw.rect(screen, color, p.Rect(c*SQ_Size, r*SQ_Size, SQ_Size, SQ_Size))  


def drawpieces(screen, board):
        for r in range(DIMENTIONS):
             for c in range(DIMENTIONS):
                  piece = board[r][c]
                  if piece != "--":
                        screen.blit(images[piece], p.Rect(c*SQ_Size, r*SQ_Size, SQ_Size, SQ_Size))

def main():
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    gs = chessmain.Gamestate()
    imageload()
    sqSelected = ()
    move_positions = []
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                mouse_location = p.mouse.get_pos()
                col = mouse_location[0] // SQ_Size
                row = mouse_location[1] // SQ_Size
            
                if sqSelected == (row, col):
                     sqSelected = ()
                     move_positions = []
                else: 
                     sqSelected = (row, col)
                     move_positions.append(sqSelected)
                     if len(move_positions) == 2:
                        move = chessmain.Move(move_positions[0], move_positions[1], gs)
                        move.movepiece()
                        sqSelected = ()
                        move_positions = []
        drawGameState(screen, gs)

    
        p.display.flip()
        clock.tick(MAX_FPS)

p.quit()








if __name__ == "__main__":
    main()  