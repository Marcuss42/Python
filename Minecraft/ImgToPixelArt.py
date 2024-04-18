from mine import Minecraft, block
from sys import argv
from PixelArt import extratcColorImg
from PIL import Image, ImageEnhance
from glob import glob
import math

"""
To use, you need to place your PNG image in the 'PixelArt' folder 
and specify its name in Minecraft (img.png)

It is also necessary to have PIL (Python Imaging Library) installed. (pip install PIL)
"""

def find_color(paleta, cor_referencia):
    cor_mais_proxima = None
    menor_distancia = float('inf')

    for nome_cor, cor in paleta.items():
        distancia = math.sqrt(
            (cor_referencia[0] - cor[0])**2 +
            (cor_referencia[1] - cor[1])**2 +
            (cor_referencia[2] - cor[2])**2
        )

        if distancia < menor_distancia:
            cor_mais_proxima = nome_cor
            menor_distancia = distancia

    return cor_mais_proxima
    
if len(argv) < 2:
    raise Exception("Provide the img name!!")
if len(argv) < 3:
    raise Exception("Provide the orientation! (up, down)")

IMG = "PixelArt/" + argv[1]
ORIENTATION = argv[2]

if len(argv) > 3:
    img = Image.open(IMG)
    new_img = img.resize((int(argv[3]), int(argv[3])))
    out = "PixelArt/" + "resized.png"
    new_img.save(out)
    IMG = out

palette_dict = {
    block.WOOL_WHITE: (255, 255, 255),
    block.WOOL_ORANGE: (255, 165, 0),
    block.WOOL_MAGENTA: (255, 0, 255),
    block.WOOL_LIGHT_BLUE: (173, 216, 230),
    block.WOOL_YELLOW: (255, 255, 0),
    block.WOOL_LIME: (50, 205, 50),
    block.WOOL_PINK: (255, 192, 203),
    block.WOOL_LIGHT_GRAY: (211, 211, 211),
    block.WOOL_GRAY: (128, 128, 128),
    block.WOOL_CYAN: (0, 255, 255),
    block.WOOL_PURPLE: (128, 0, 128),
    block.WOOL_BLUE: (0, 0, 255),
    block.WOOL_BROWN: (139, 69, 19),
    block.WOOL_GREEN: (0, 128, 0),
    block.WOOL_RED: (255, 0, 0),
    block.WOOL_BLACK: (0, 0, 0),
    block.GLAZED_TERRACOTTA_MAGENTA: (216, 191, 216),
    block.GLAZED_TERRACOTTA_LIGHT_BLUE: (64, 224, 208),
    block.CONCRETE_BLOCK_GRAY: (169, 169, 169),
    block.GRAVEL: (127,124,123),
    block.HARDENED_CLAY_STAINED_BLACK: (37, 23, 16),
    block.HARDENED_CLAY_STAINED_BLUE: (74, 60, 91),
    block.HARDENED_CLAY_STAINED_BROWN: (77, 51, 36),
    block.HARDENED_CLAY_STAINED_CYAN: (87, 91, 91),
    block.HARDENED_CLAY_STAINED_GRAY: (58, 42, 36),
    block.HARDENED_CLAY_STAINED_GREEN: (76, 83, 42),
    block.HARDENED_CLAY_STAINED_LIGHT_BLUE: (113, 109, 138),
    block.HARDENED_CLAY_STAINED_LIGHT_GRAY: (135, 107, 98),
    block.HARDENED_CLAY_STAINED_LIME: (104, 118, 53),
    block.HARDENED_CLAY_STAINED_MAGENTA: (150, 88, 109),
    block.HARDENED_CLAY_STAINED_ORANGE: (162, 84, 38),
    block.HARDENED_CLAY_STAINED_PINK: (162, 78, 79),
    block.HARDENED_CLAY_STAINED_PURPLE: (118, 70, 86),
    block.HARDENED_CLAY_STAINED_RED: (143, 61, 47),
    block.HARDENED_CLAY_STAINED_WHITE: (210, 178, 161),
    block.HARDENED_CLAY_STAINED_YELLOW: (186, 133, 35),
    block.HAY_BLOCK: (158, 117, 18),
    block.HOPPER: (63, 63, 63),
    block.ICE: (125, 173, 255),
    block.ICE_PACKED: (165, 195, 245),
    block.IRON_BLOCK: (219, 219, 219),
    block.IRON_ORE: (136, 130, 127),
    block.JUKEBOX: (101, 68, 51),
    block.DIAMOND_ORE: (60, 90, 102),
    block.DIAMOND_BLOCK: (61, 201, 176),
    block.BOOKSHELF: (122, 86, 46),
    block.COBBLESTONE: (139, 69, 19),
    block.BRICK_BLOCK: (139, 69, 19),
    block.COBBLESTONE: (139, 69, 19),
    block.IRON_BLOCK: (139, 69, 19),
    block.GOLD_BLOCK: (255, 215, 0),
    block.DIAMOND_BLOCK: (61, 201, 176),
    block.EMERALD_BLOCK: (0, 255, 64),
    block.LAPIS_LAZULI_BLOCK: (0, 0, 255),
    block.REDSTONE_BLOCK: (255, 0, 0),
    block.NETHERRACK: (144, 0, 0),
    block.SOUL_SAND: (85, 85, 85),
    block.MAGMA: (255, 0, 0),
    block.END_STONE: (223, 223, 0),
    block.PURPUR_BLOCK: (128, 0, 128),
    block.PURPUR_PILLAR: (128, 0, 128),
    block.NETHER_BRICK: (112, 2, 0),
    block.NETHER_WART_BLOCK: (131, 11, 0),
    block.BONE_BLOCK: (233, 233, 233),
    block.SLIME_BLOCK: (0, 255, 0),
    block.PRISMARINE: (0, 112, 133),
    block.PRISMARINE_DARK: (0, 112, 133),
    block.SEA_LANTERN: (0, 112, 133),
    block.RED_SAND: (217, 83, 79),
    block.RED_SANDSTONE: (217, 83, 79),
    block.RED_SANDSTONE_SMOOTH: (217, 83, 79),
    block.RED_SANDSTONE_CHISELED: (217, 83, 79)
}

imagem = Image.open(IMG if "resized.png" not in glob("PixelArt/*") else "resized.png")
imagem_brilhante = ImageEnhance.Brightness(imagem).enhance(1.1)
imagem_brilhante.save("PixelArt/new.png")

extratcColorImg.IMG = "PixelArt/new.png"
matriz_colors = extratcColorImg.extract_colors()

m = Minecraft()
pos = m.player.getPos()


if  ORIENTATION == "up":
    for height, colors in enumerate(matriz_colors):
        for width, color in enumerate(colors):
            block_name = find_color(palette_dict, color)
            m.setBlock(pos.x+width, pos.y+height, pos.z, block_name)

else:  
    for height, colors in enumerate(matriz_colors):
        for width, color in enumerate(colors):        
            block_name = find_color(palette_dict, color)
            m.setBlock(pos.x+width, pos.y, pos.z+height, block_name)

