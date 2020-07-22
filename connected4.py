# The purpose of this project was to create a GUI based connect 4
# Connect4.py
# By Pranav Rao

import numpy as np # library to work with arrays
import pygame # libary that generates the actual game screen widget
import sys  #access certain perameters for run time efficiency
import math #basic libary to calculate certain math functions

#global color variables used by the pygame graphcis
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#global column and row count
ROW_NUM = 6
COL_NUM = 7


# This function will create matrix
def create_board():
    board = np.zeros((ROW_NUM, COL_NUM))
    return board


# This function will drop the piece in proper location
def drop_piece(board, row, col, pieces):
    board[row][col] = pieces
    pass


# This function will check if the 0 and return it
def is_valid_location(board, col):
    return board[ROW_NUM - 1][col] == 0


# This function find the next open row based on the pieces
def get_next_open_row(board, col):
    for r in range(ROW_NUM):
        if board[r][col] == 0:
            return r
    pass


# Prints the board
def print_board(board):
    print(np.flip(board, 0))


# This function purpose to check the different connect 4 combinations, therefore -3 for col or row
def get_wining_move(board, piece):
    # This will check for horizontal wins
    for c in range(COL_NUM - 3):
        for r in range(ROW_NUM):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # This will check for vertical wins
    for c in range(COL_NUM):
        for r in range(ROW_NUM - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # This will check for diagonal-positive since only 1 piece inside the row or column
    for c in range(COL_NUM - 3):
        for r in range(ROW_NUM - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # This will check for diagonal-negative since only 1 piece inside the row or column
    for c in range(COL_NUM - 3):
        for r in range(3, ROW_NUM):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


# drawing the GUI board
def draw_board(board):
    #This will draw the board of the game blue with black circles
    for c in range(COL_NUM):
        for r in range(ROW_NUM):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), Rad)

    #This will draw yellow and red token/pieces
    for c in range(COL_NUM):
        for r in range(ROW_NUM):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                    height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   Rad)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                    height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   Rad)
    pygame.display.update()


# This will display the board layout
board = create_board()
print_board(board)
game_over = False
turn = 0

# Going to create the game into game library
pygame.init()

# This is the specifications for the window size
SQUARE_SIZE = 100

#This is giving the widght and height of the board size
width = COL_NUM * SQUARE_SIZE
height = (ROW_NUM + 1) * SQUARE_SIZE
size = (width, height)

#This is for the circle radius in the game
Rad = int(SQUARE_SIZE / 2 - 5)

#This command will draw the board size and redraw after each moves
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

#This is the font of the text
myfont = pygame.font.SysFont("monospace", 75)

# While loop to make the game continuing till its over
while not game_over:
    
    # condition when the game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Mouse motion based on the location of the matrix
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE/2)), Rad)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE/2)), Rad)
        pygame.display.update()
        # Mouse button clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE))
            # Player one input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARE_SIZE))

                # This is if cases for player 1 turns
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    # Checks if Player 1 wins and ends the while loop
                    if get_wining_move(board, 1):
                        label = myfont.render("Play 1 Wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            # Player two input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARE_SIZE))

                # if condition to place piece
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    # Checks if Player 1 wins and ends the while loop
                    if get_wining_move(board, 2):
                        label = myfont.render("Player 2 Wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)  # prints the grid
            draw_board(board)

            # This will keep alternating between player 1 and 2
            turn += 1
            turn = turn % 2

            # once the game is over it will wait for about 35 seconds and then terminate
            if game_over:
                pygame.time.wait(3500)
