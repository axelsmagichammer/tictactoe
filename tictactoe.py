import pygame
import sys

WIDTH = 320
HEIGHT = 320

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((0,0,0))
pygame.display.set_caption("TicTacToe")
running = True
piece = 0 # state of the game, 0 is 0's turn and 1 is x's turn

# draw the board
pygame.draw.rect(screen,(255,255,255),(100,0,10,320),0)
pygame.draw.rect(screen,(255,255,255),(210,0,10,320),0)
pygame.draw.rect(screen,(255,255,255),(0,100,320,10),0)
pygame.draw.rect(screen,(255,255,255),(0,210,320,10),0)
pygame.display.update()

# load up the images of noughts and crosses, and scale them
cross = pygame.image.load('cross.png').convert()
cross = pygame.transform.scale(cross,(100, 100))
nought = pygame.image.load('nought.png').convert()
nought = pygame.transform.scale(nought,(100, 100))

# set-up matrix to hold the game as it progresses, 0 for no entry, 1 for nought and 2 for cross
gameboard = [[0] * 3 for i in range(3)]

# check the position of the mouse and return which of the 9 squares it is in
def mousezone(Xmouse, Ymouse):
    if Xmouse<=100:
        column = 0
    elif Xmouse>=110 and Xmouse<=210:
        column = 1
    elif Xmouse>=220:
        column = 2
    else:
        column = 3
    if Ymouse<=100:
        row = 0
    elif Ymouse>=110 and Ymouse<=210:
        row = 1
    elif Ymouse>=220:
        row = 2
    else:
        row = 3
    return (row, column)

# updates the board following a possible move
def updateboard(board,row,column):
    if board[row][column] == 0:
        updatetheboard = True
        if piece == 0: # 0 for a nought
            board[row][column] = 1
        else:
            board[row][column] = 2
    else:
        updatetheboard = False
    return(board, updatetheboard)

# check for win by looking at all the combinations
# return False for no win and True for win
def checkforwin(board):
    win = False
    # check rows
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0]>0:
            win = True
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0]>0:
            win = True
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0]>0:
            win = True
    # check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0]>0:
            win = True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1]>0:
            win = True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2]>0:
            win = True
    # check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0]>0:
            win = True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2]>0:
            win = True       
    else:
        win = False
    return(win)
    
def drawboard(board,row,column,state):
    board[row][column] = state + 1
    if state == 0:
        stamp = nought
    else:
        stamp = cross
    if row == 0:
        ypos = 0
    if row == 1:
        ypos = 110
    if row == 2:
        ypos = 220
    if column == 0:
        xpos = 0
    if column == 1:
        xpos = 110
    if column == 2:
        xpos = 220
    return (stamp, xpos, ypos)

def checkfordraw(board):
    draw = False
    if board[0][0]>0 and board[0][1]>0 and board[0][2]>0 and board[1][0]>0 and board[1][1]>0 and board[1][2]>0 and board[2][0]>0 and board[2][1]>0 and board[2][2]>0:
        draw = True
    else:
        draw = False
    return(draw)

def aimove(board):
    # check for the win
    # rows
    updated = False
    if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 0 and updated == False:
        updated = True
        row = 0
        column = 2
        board[0][2] = 2
    elif board[0][0] == 0 and board[0][1] == 2 and board[0][2] == 2 and updated == False:
        updated = True
        row = 0
        column = 0
        board[0][0] = 2
    elif board[0][0] == 2 and board[0][1] == 0 and board[0][2] == 2 and updated == False:
        updated = True
        row = 0
        column = 1
        board[0][1] = 2
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 0 and updated == False:
        updated = True
        row = 1
        column = 2
        board[1][2] = 2
    elif board[1][0] == 0 and board[1][1] == 2 and board[1][2] == 2 and updated == False:
        updated = True
        row = 1
        column = 0
        board[1][0] = 2
    elif board[1][0] == 2 and board[1][1] == 0 and board[1][2] == 2 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 0 and updated == False:
        updated = True
        row = 2
        column = 2
        board[2][2] = 2
    elif board[2][0] == 0 and board[2][1] == 2 and board[2][2] == 2 and updated == False:
        updated = True
        row = 2
        column = 0
        board[2][0] = 2
    elif board[2][0] == 2 and board[2][1] == 0 and board[2][2] == 2 and updated == False:
        updated = True
        row = 2
        column = 1 
        board[2][1] = 2
    # columns
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 0 and updated == False:
        updated = True
        row = 2
        column = 0
        board[2][0] = 2
    elif board[0][0] == 0 and board[1][0] == 2 and board[2][0] == 2 and updated == False:
        updated = True
        row = 0
        column = 0
        board[0][0] = 2
    elif board[0][0] == 2 and board[1][0] == 0 and board[2][0] == 2 and updated == False:
        updated = True
        row = 1
        column = 0
        board[1][0] = 2
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 0 and updated == False:
        updated = True
        row = 2
        column = 1
        board[2][1] = 2
    elif board[0][1] == 0 and board[1][1] == 2 and board[2][1] == 2 and updated == False:
        updated = True
        row = 0
        column = 1
        board[0][1] = 2
    elif board[0][1] == 2 and board[1][1] == 0 and board[2][1] == 2 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 0 and updated == False:
        updated = True
        row = 2
        column = 2
        board[2][2] = 2
    elif board[0][2] == 0 and board[1][2] == 2 and board[2][2] == 2 and updated == False:
        updated = True
        row = 0
        column = 2
        board[0][2] = 2
    elif board[0][2] == 2 and board[1][2] == 0 and board[2][2] == 2 and updated == False:
        updated = True
        row = 1
        column = 2
        board[1][2] = 2
    # diagonals
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 0 and updated == False:
        updated = True
        row = 2
        column = 2
        board[2][2] = 2
    elif board[0][0] == 0 and board[1][1] == 2 and board[2][2] == 2 and updated == False:
        updated = True
        row = 0
        column = 0
        board[0][0] = 2
    elif board[0][0] == 2 and board[1][1] == 0 and board[2][2] == 2 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    elif board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 0 and updated == False:
        updated = True
        row = 0
        column = 2
        board[0][2] = 2
    elif board[2][0] == 0 and board[1][1] == 2 and board[0][2] == 2 and updated == False:
        updated = True
        row = 2
        column = 0
        board[2][0] = 2
    elif board[2][0] == 2 and board[1][1] == 0 and board[0][2] == 2 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    # check to save game
    # rows
    elif board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 0 and updated == False:
        updated = True
        row = 0
        column = 2
        board[0][2] = 2
    elif board[0][0] == 0 and board[0][1] == 1 and board[0][2] == 1 and updated == False:
        updated = True
        row = 0
        column = 0
        board[0][0] = 2
    elif board[0][0] == 1 and board[0][1] == 0 and board[0][2] == 1 and updated == False:
        updated = True
        row = 0
        column = 1
        board[0][1] = 2
    elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 0 and updated == False:
        updated = True
        row = 1
        column = 2
        board[1][2] = 2
    elif board[1][0] == 0 and board[1][1] == 1 and board[1][2] == 1 and updated == False:
        updated = True
        row = 1
        column = 0
        board[1][0] = 2
    elif board[1][0] == 1 and board[1][1] == 0 and board[1][2] == 1 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 0 and updated == False:
        updated = True
        row = 2
        column = 2
        board[2][2] = 2
    elif board[2][0] == 0 and board[2][1] == 1 and board[2][2] == 1 and updated == False:
        updated = True
        row = 2
        column = 0
        board[2][0] = 2
    elif board[2][0] == 1 and board[2][1] == 0 and board[2][2] == 1 and updated == False:
        updated = True
        row = 2
        column = 1 
        board[2][1] = 2
    # columns
    elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 0 and updated == False:
        updated = True
        row = 2
        column = 0
        board[2][0] = 2
    elif board[0][0] == 0 and board[1][0] == 1 and board[2][0] == 1 and updated == False:
        updated = True
        row = 0
        column = 0
        board[0][0] = 2
    elif board[0][0] == 1 and board[1][0] == 0 and board[2][0] == 1 and updated == False:
        updated = True
        row = 1
        column = 0
        board[1][0] = 2
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 0 and updated == False:
        updated = True
        row = 2
        column = 1
        board[2][1] = 2
    elif board[0][1] == 0 and board[1][1] == 1 and board[2][1] == 1 and updated == False:
        updated = True
        row = 0
        column = 1
        board[0][1] = 2
    elif board[0][1] == 1 and board[1][1] == 0 and board[2][1] == 1 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 0 and updated == False:
        updated = True
        row = 2
        column = 2
        board[2][2] = 2
    elif board[0][2] == 0 and board[1][2] == 1 and board[2][2] == 1 and updated == False:
        updated = True
        row = 0
        column = 2
        board[0][2] = 2
    elif board[0][2] == 1 and board[1][2] == 0 and board[2][2] == 1 and updated == False:
        updated = True
        row = 1
        column = 2
        board[1][2] = 2
    # diagonals
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 0 and updated == False:
        updated = True
        row = 2
        column = 2
        board[2][2] = 2
    elif board[0][0] == 0 and board[1][1] == 1 and board[2][2] == 1 and updated == False:
        updated = True
        row = 0
        column = 0
        board[0][0] = 2
    elif board[0][0] == 1 and board[1][1] == 0 and board[2][2] == 1 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    elif board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 0 and updated == False:
        updated = True
        row = 0
        column = 2
        board[0][2] = 2
    elif board[2][0] == 0 and board[1][1] == 1 and board[0][2] == 1 and updated == False:
        updated = True
        row = 2
        column = 0
        board[2][0] = 2
    elif board[2][0] == 1 and board[1][1] == 0 and board[0][2] == 1 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    # place in corners
    elif board[0][0] == 0 and updated == False:
        updated = True
        row = 0
        column = 0
        board[0][0] = 2
    elif board[0][2] == 0 and updated == False:
        updated = True
        row = 0
        column = 2
        board[0][2] = 2
    elif board[2][2] == 0 and updated == False:
        updated = True
        row = 2
        column = 2
        board[2][2] = 2
    elif board[2][0] == 0 and updated == False:
        updated = True
        row = 2
        column = 0
        board[2][0] = 2
    # place in centre
    elif board[1][1] == 0 and updated == False:
        updated = True
        row = 1
        column = 1
        board[1][1] = 2
    # place on sides
    elif board[0][1] == 0 and updated == False:
        updated = True
        row = 0
        column = 1
        board[0][1] = 2
    elif board[1][2] == 0 and updated == False:
        updated = True
        row = 1
        column = 2
        board[1][2] = 2
    elif board[2][1] == 0 and updated == False:
        updated = True
        row = 2
        column = 1
        board[2][1] = 2
    else:
        row = 1
        column = 0
        board[1][0] = 2
    return(board,row, column)


def main():
    global running
    global gameboard
    global piece
    global cross
    global nought
    # firstorsecond = input("First or second? ")
    # if firstorsecond == "First":
    #     piece = 0
    # elif firstorsecond =="Second":
    #     piece = 1
    # else:
    #     print("You can go first")
    #     piece = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposition = pygame.mouse.get_pos()
                mousearea = mousezone(mouseposition[0],mouseposition[1])
                if mousearea[0] < 3 and mousearea[1] < 3: 
                    newboard = updateboard(gameboard,mousearea[0],mousearea[1])
                    gameboard = newboard[0]
                    if newboard[1]:
                        newdrawboard = drawboard(gameboard,mousearea[0],mousearea[1],piece)
                        screen.blit(newdrawboard[0],(newdrawboard[1],newdrawboard[2]))
                        pygame.display.update()
                        if checkforwin(gameboard):
                            basicfont = pygame.font.SysFont(None, 48)
                            if piece == 0:
                                text = basicfont.render('Noughts Win', True, (0, 255, 0), (255, 255, 255))
                            else:
                                text = basicfont.render('Crosses Win', True, (0, 255, 0), (255, 255, 255))
                            textrect = text.get_rect()
                            textrect.centerx = screen.get_rect().centerx
                            textrect.centery = screen.get_rect().centery
                            screen.blit(text, textrect)
                            pygame.display.update()
                            running = False
                        if checkforwin(gameboard) == False and checkfordraw(gameboard):
                            basicfont = pygame.font.SysFont(None, 48)
                            text = basicfont.render('Draw', True, (0, 255, 0), (255, 255, 255))
                            textrect = text.get_rect()
                            textrect.centerx = screen.get_rect().centerx
                            textrect.centery = screen.get_rect().centery
                            screen.blit(text, textrect)
                            pygame.display.update()
                            running = False
                        piece = (piece + 1) % 2
                        # a move for the computer
                        if checkfordraw(gameboard) == False and checkforwin(gameboard) == False:
                            computermove = aimove(gameboard)
                            newboard = updateboard(computermove[0],computermove[1],computermove[2])
                            gameboard = newboard[0]
                            newdrawboard = drawboard(gameboard,computermove[1],computermove[2],piece)
                        screen.blit(newdrawboard[0],(newdrawboard[1],newdrawboard[2]))
                        pygame.display.update()
                        if checkforwin(gameboard):
                            basicfont = pygame.font.SysFont(None, 48)
                            if piece == 0:
                                text = basicfont.render('Noughts Win', True, (0, 255, 0), (255, 255, 255))
                            else:
                                text = basicfont.render('Crosses Win', True, (0, 255, 0), (255, 255, 255))
                            textrect = text.get_rect()
                            textrect.centerx = screen.get_rect().centerx
                            textrect.centery = screen.get_rect().centery
                            screen.blit(text, textrect)
                            pygame.display.update()
                            running = False
                        if checkforwin(gameboard) == False and checkfordraw(gameboard):
                            basicfont = pygame.font.SysFont(None, 48)
                            text = basicfont.render('Draw', True, (0, 255, 0), (255, 255, 255))
                            textrect = text.get_rect()
                            textrect.centerx = screen.get_rect().centerx
                            textrect.centery = screen.get_rect().centery
                            screen.blit(text, textrect)
                            pygame.display.update()
                            running = False
                        piece = (piece + 1) % 2
    pygame.quit()
    sys.exit()
                            
                            
if __name__ == "__main__":
    main()