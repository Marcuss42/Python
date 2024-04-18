from mine import Minecraft, block
from sys import argv
from time import sleep

# Marcuss42

if len(argv) > 1:
    SIZE = int(argv[1])-1
else:
    SIZE = 3

m = Minecraft()

player = m.player
pos = player.getPos()
player.setTilePos(pos.x, pos.y+3, pos.z)

while True:
    pos = player.getPos()

    #player.setTilePos(pos.x, pos.y+1, pos.z)

    m.setBlocks(pos.x-SIZE, pos.y-1, pos.z-SIZE, 
                pos.x+SIZE, pos.y-1, pos.z+SIZE, block.STONE)
    m.setBlocks(pos.x-SIZE, pos.y-2, pos.z-SIZE, 
                pos.x+SIZE, pos.y-2, pos.z+SIZE, block.AIR)
    sleep(0.00005)
