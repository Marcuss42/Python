from mine import Minecraft, block
import mcpi.minecraft as minecraft
from board2d import Board2D
from time import time, sleep
from copy import deepcopy
import random
from keyboard import is_pressed
import fonts
from text import drawText, angleToTextDirection
from mcpi.vec3 import Vec3

# DECLARE ALL THE CONSTANTS
BOARD_SIZE = 18
# Extra two are for the walls, playing area will have size as BOARD_SIZE
EFF_BOARD_SIZE = BOARD_SIZE + 2

# Delayed Auto Shift
DAS = 0.3

PIECES = [
    [[2], [2], [2], [2]],

    [[3, 0],
     [3, 0],
     [3, 3]],

    [[0, 4],
     [0, 4],
     [4, 4]],

    [[5, 5],
     [5, 5]],

    [[0, 6, 0],
     [6, 6, 6]],

    [[0, 7],
     [7, 7],
     [7, 0]],
]

GHOST = -1

FILL_BLOCK = block.WOOL_BLACK
GHOST_COLOR = block.STAINED_GLASS_LIGHT_GRAY
BOARD_COLOR = block.BEDROCK

COLORS = [
    block.WOOL_RED,
    block.WOOL_GREEN,
    block.WOOL_YELLOW,
    block.WOOL_BLUE,
    block.WOOL_MAGENTA,
    block.WOOL_CYAN
]

# Constants for user input
MOVE_LEFT = 'left'
MOVE_RIGHT = 'right' 
ROTATE_ANTICLOCKWISE = 'z'
ROTATE_CLOCKWISE = 'x'
QUIT_GAME = 'q'
HARD_DROP = 'v'
SOFT_DROP = 'down'


def print_board(board, mine_board: Board2D, pieces: tuple[tuple | list, ...]):
    board_copy = deepcopy(board)
    
    for piece in pieces:
        curr_piece, piece_pos = piece
        curr_piece_size_x = len(curr_piece)
        curr_piece_size_y = len(curr_piece[0])
        for i in range(curr_piece_size_x):
            for j in range(curr_piece_size_y):
                board_copy[piece_pos[0] + i][piece_pos[1] + j] = curr_piece[i][j] | board[piece_pos[0] + i][piece_pos[1] + j]

    for i in range(EFF_BOARD_SIZE):
        for j in range(EFF_BOARD_SIZE):
            x, y = j, EFF_BOARD_SIZE-i
            if board_copy[i][j] == 1:
                mine_board.setBlock(x, y, BOARD_COLOR) 
                mc.setBlock(mine_board.left + x, mine_board.bottom + y, mine_board.plane + 1, BOARD_COLOR)
            elif board_copy[i][j] > 1:
                mine_board.setBlock(x, y, COLORS[board_copy[i][j] - 2])
                mc.setBlock(mine_board.left + x, mine_board.bottom + y, mine_board.plane + 1, COLORS[board_copy[i][j] - 2])

            elif board_copy[i][j] == -1:
                mc.setBlock(mine_board.left + x, mine_board.bottom + y, mine_board.plane + 1, GHOST_COLOR)

    mine_board.setBlocks(0, 0, EFF_BOARD_SIZE, 0, block.AIR)
    mine_board.draw()

def init_board():
    board = [[0 for x in range(EFF_BOARD_SIZE)] for y in range(EFF_BOARD_SIZE)]

    for i in range(EFF_BOARD_SIZE):
        board[i][0] = 1
        board[EFF_BOARD_SIZE-1][i] = 1
        board[i][EFF_BOARD_SIZE-1] = 1
        board[0][i] = 1

    return board

def get_random_piece():
    idx = random.randrange(len(PIECES))
    return PIECES[idx]

def get_random_position(curr_piece):
    curr_piece_size = len(curr_piece)
    i = 1
    j = random.randrange(1, EFF_BOARD_SIZE-curr_piece_size-1)
    return [i, j]

def is_game_over(board, curr_piece, piece_pos):
    # If the piece cannot move down and the position is still the first row
    # of the board then the game has ended
    if not can_move_down(board, curr_piece, piece_pos) and piece_pos[0] == 1:
        return True
    return False

def get_left_move(piece_pos, unit = 1):
    # Shift the piece left by 1 unit
    new_piece_pos = [piece_pos[0], piece_pos[1] - unit]
    return new_piece_pos

def get_right_move(piece_pos, unit=1):
    new_piece_pos = [piece_pos[0], piece_pos[1] + unit]
    return new_piece_pos

def get_down_move(piece_pos, unit=1):
    new_piece_pos = [piece_pos[0] + unit, piece_pos[1]]
    return new_piece_pos

def rotate_clockwise(piece):
    piece_copy = deepcopy(piece)
    reverse_piece = piece_copy[::-1]
    return list(list(elem) for elem in zip(*reverse_piece))

def rotate_anticlockwise(piece):
    piece_copy = deepcopy(piece)
    piece_1 = rotate_clockwise(piece_copy)
    piece_2 = rotate_clockwise(piece_1)
    return rotate_clockwise(piece_2)

def merge_board_and_piece(board, curr_piece, piece_pos):
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            board[piece_pos[0] + i][piece_pos[1] + j] = curr_piece[i][j] | board[piece_pos[0] + i][piece_pos[1] + j]

def remove_filled_rows(board):
    empty_row = [0] * EFF_BOARD_SIZE
    empty_row[0] = 1
    empty_row[EFF_BOARD_SIZE - 1] = 1

    filled_row = [1] * EFF_BOARD_SIZE

    rows_to_remove = []
    for row in board[1:EFF_BOARD_SIZE - 1]:
        if list(map(lambda i: int(i>0), row)) == filled_row:
            rows_to_remove.append(row)

    for row in rows_to_remove:
        if row in board:
            board.remove(row)

    for i in range(len(rows_to_remove)):
        board.insert(1, empty_row)

    return len(rows_to_remove)

def overlap_check(board, curr_piece, piece_pos):
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            if board[piece_pos[0]+i][piece_pos[1]+j] >= 1 and curr_piece[i][j] >= 1:
                return False    
    return True

def can_move_left(board, curr_piece, piece_pos, unit=1):
    piece_pos = get_left_move(piece_pos, unit)
    return overlap_check(board, curr_piece, piece_pos)

def can_move_right(board, curr_piece, piece_pos, unit=1):
    piece_pos = get_right_move(piece_pos, unit)
    return overlap_check(board, curr_piece, piece_pos)

def can_move_down(board, curr_piece, piece_pos, unit=1):
    piece_pos = get_down_move(piece_pos, unit)
    return overlap_check(board, curr_piece, piece_pos)

def can_rotate_anticlockwise(board, curr_piece, piece_pos):
    curr_piece = rotate_anticlockwise(curr_piece)
    return overlap_check(board, curr_piece, piece_pos)

def can_rotate_clockwise(board, curr_piece, piece_pos):
    curr_piece = rotate_clockwise(curr_piece)
    return overlap_check(board, curr_piece, piece_pos)

def soft_drop(board, curr_piece, piece_pos):
    if can_move_down(board, curr_piece, piece_pos):
        piece_pos = get_down_move(piece_pos)
    return piece_pos

def hard_drop(board, curr_piece, piece_pos):
    while can_move_down(board, curr_piece, piece_pos):
        piece_pos = get_down_move(piece_pos)
    return piece_pos

def ghost_piece(board, curr_piece, piece_pos):
    curr_copy = deepcopy(curr_piece)
    for i in range(len(curr_piece)):
        for j in range(len(curr_piece[0])):
            if curr_copy[i][j] != 0:
                curr_copy[i][j] = GHOST     

    return curr_copy, hard_drop(board, curr_piece, piece_pos)

def calcular_pontuacao_linhas(linhas_limpas):
    if linhas_limpas == 1:
        pontuacao = 40
    elif linhas_limpas == 2:
        pontuacao = 100
    elif linhas_limpas == 3:
        pontuacao = 300
    elif linhas_limpas == 4:
        pontuacao = 1200
    else:
        pontuacao = 0
    return pontuacao

def atualizar_pontuacao(pontuacao_total, linhas_limpas):
    pontuacao_linhas = calcular_pontuacao_linhas(linhas_limpas)
    pontuacao_total += pontuacao_linhas
    return pontuacao_total

def aumentar_velocidade(vel, incremento, max_v):
    return min(vel + incremento, max_v)

def clear(board, mine_board: Board2D):
    mine_board.fill(FILL_BLOCK)

    for i in range(EFF_BOARD_SIZE-1):
        for j in range(EFF_BOARD_SIZE):
            x, y = j, EFF_BOARD_SIZE-i
            if board[i][j] == 0:
                mc.setBlock(mine_board.left+x, mine_board.bottom+y, mine_board.plane+1, block.AIR)

def welcome(mc):
    mc.postToChat(f"{MOVE_LEFT.upper()} - Move piece left")
    mc.postToChat(f"{MOVE_RIGHT.upper()} - Move piece right")
    mc.postToChat(f"{ROTATE_ANTICLOCKWISE.upper()} - Rotate Counter Clockwise")
    mc.postToChat(f"{ROTATE_CLOCKWISE.upper()} (or UP) - Rotate Clockwise")
    mc.postToChat(f"{HARD_DROP} - Hard Drop")
    mc.postToChat(f"{SOFT_DROP} - Hard Drop")
    mc.postToChat(f"{QUIT_GAME.upper()}: Quit")

def play_game():
    mine_board = Board2D(mc, width = EFF_BOARD_SIZE, height = EFF_BOARD_SIZE, background = block.AIR)
    mine_board.bottom -= 2
    board = init_board()
    
    text_pos =  mine_board.left - (EFF_BOARD_SIZE * 0.50), mine_board.bottom + EFF_BOARD_SIZE + 1, mine_board.plane + 1
    forward = angleToTextDirection(mc.player.getRotation())

    welcome(mc)

    curr_piece = get_random_piece()
    piece_pos = get_random_position(curr_piece)

    vel = 0.05
    incremento_velocidade = 0.0001
    unit = vel
    piece_in_floor = False
    score = 0
    while (not is_game_over(board, curr_piece, piece_pos)):
        
        if is_pressed(MOVE_LEFT):
            if can_move_left(board, curr_piece, piece_pos):
                piece_pos = get_left_move(piece_pos)

        if is_pressed(MOVE_RIGHT):
            if can_move_right(board, curr_piece, piece_pos):
                piece_pos = get_right_move(piece_pos)

        if is_pressed(ROTATE_ANTICLOCKWISE):
            if can_rotate_anticlockwise(board, curr_piece, piece_pos):
                curr_piece = rotate_anticlockwise(curr_piece)

        if is_pressed(ROTATE_CLOCKWISE) or is_pressed('up'):
            if can_rotate_clockwise(board, curr_piece, piece_pos):
                curr_piece = rotate_clockwise(curr_piece)

        if is_pressed(HARD_DROP):
            piece_pos = hard_drop(board, curr_piece, piece_pos)

        if is_pressed(SOFT_DROP):
            piece_pos = soft_drop(board, curr_piece, piece_pos)

        if is_pressed(QUIT_GAME):
            return

        if can_move_down(board, curr_piece, piece_pos, int(unit)):
            piece_pos = get_down_move(piece_pos, int(unit))
            if not piece_in_floor:
                start = time()

        else:
            piece_in_floor = True
            if (time() - start) > DAS:
                merge_board_and_piece(board, curr_piece, piece_pos)
                score = atualizar_pontuacao(score, remove_filled_rows(board))
                curr_piece = get_random_piece()
                piece_pos = get_random_position(curr_piece)
                piece_in_floor = False
        
        curr_ghost, ghost_pos = ghost_piece(board, curr_piece, piece_pos)

        clear(board, mine_board)
        print_board(
            board, 
            mine_board,
            pieces = ((curr_ghost, ghost_pos), (curr_piece, piece_pos))
        )

        unit = (vel + unit)
        if unit >= 1 + vel:
            unit = vel       

        vel = aumentar_velocidade(vel, incremento = incremento_velocidade, max_v = 1)

        sleep(.05)

        text = str(score)
        drawText(mc, fonts.FONTS['metrix7pt'], Vec3(*text_pos), forward, minecraft.Vec3(0,1,0), text, block.AIR, block.AIR)
        drawText(mc, fonts.FONTS['metrix7pt'], Vec3(*text_pos), forward, minecraft.Vec3(0,1,0), text, block.GOLD_BLOCK)


if __name__ == "__main__":
    mc = Minecraft()
    play_game()
