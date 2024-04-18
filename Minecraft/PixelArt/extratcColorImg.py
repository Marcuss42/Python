from PIL import Image

IMG = ""
TAMANHO_CELULA = 2
matriz_cores = []

def extract_colors():
    # Abra a imagem
    imagem = Image.open(IMG)

    # Converta a imagem para o modo RGB (garante que ela seja uma imagem colorida)
    imagem_rgb = imagem.convert("RGB")

    # Obtenha as dimensões da imagem
    largura_imagem, altura_imagem = imagem.size

    matriz_cores.clear()

    # Itere sobre os pixels da imagem
    for y in range(altura_imagem):
        linha = []
        for x in range(largura_imagem):
            pixel = imagem_rgb.getpixel((x, y))
            linha.append(pixel)
        matriz_cores.append(linha)

    return matriz_cores

def draw_img():
    import pygame
    from pygame.locals import QUIT

    # Inicialize o Pygame
    pygame.init()

    altura, largura = Image.open(IMG).size

    # Crie a janela
    janela = pygame.display.set_mode((altura*TAMANHO_CELULA, largura*TAMANHO_CELULA))

    # Loop principal
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False

        # Limpe a tela
        janela.fill((0, 0, 0))

        # Desenhe a matriz de cores na janela
        for y, linha in enumerate(matriz_cores):
            for x, cor_rgb in enumerate(linha):
                pygame.draw.rect(janela, cor_rgb, (x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

        pygame.display.flip()

    # Encerre o Pygame
    pygame.quit()

if __name__ == "__main__":
    IMG = "out.png"

    print(extract_colors()[0])
    draw_img()