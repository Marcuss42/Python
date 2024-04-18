from mine import *
from board2d import Board2D
from time import sleep
from random import randint
import input

width = 30
height = 30
mc = Minecraft()
board = Board2D(mc, width, height, background=block.AIR)

x, y = width//2, height//2
vx, vy = 1, 1
player = block.WOOL_BLUE

while not input.wasPressedSinceLast(input.KEY_Q):
    board.setBlock(x, y, player)
    board.draw()
    board.setBlock(x, y, block.WOOL_BLACK)

    if input.wasPressedSinceLast(input.UP):
        y = (y + vy) % height
    if input.wasPressedSinceLast(input.DOWN):
        y = (y - vy) % height
    if input.wasPressedSinceLast(input.LEFT):
        x = (x - vx) % width
    if input.wasPressedSinceLast(input.RIGHT):
        x = (x + vx) % width
    sleep(.1)