from mine import Minecraft, block
from sys import argv
from time import sleep

# Marcuss42

if len(argv) < 4:
    raise Exception("Faltam coordenadas! x y z")
else:
    x, y, z = [int(pos) for pos in argv[1:]]
    
m = Minecraft()

while True:
    pos = m.player.getPos()

    m.setBlocks(pos.x-x, pos.y, pos.z-z, 
                        pos.x+x, y+y, pos.z+z, block.AIR)
    sleep(.1)
    